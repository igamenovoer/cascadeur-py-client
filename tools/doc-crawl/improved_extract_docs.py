#!/usr/bin/env python
"""Improved Cascadeur API HTML → Markdown converter.

Goals / Improvements over existing scripts:
* Structure aware: preserves heading hierarchy & API object grouping.
* Accurate signatures: normalises Sphinx signatures (→ becomes ->, removes excess whitespace).
* Field lists (Parameters, Returns, Raises, See Also) converted to clear subsections.
* Tables converted to GitHub markdown tables.
* Code blocks language inferred from class on <code> tag (defaults to python).
* Definition lists (<dl class~="sig">) converted to headings + fenced signature blocks when useful.
* De-navigation: strips nav/aside/header/footer/script/style & hidden elements.
* Stable IDs: outputs front‑matter with source_url, html_file, module.
* Fallback: if structured extraction yields too little content, falls back to markitdown or html2text.

Usage:
  pixi run -e dev python tools/doc-crawl/improved_extract_docs.py --all
  pixi run -e dev python tools/doc-crawl/improved_extract_docs.py --file casey-docs/html/<hash>.html
  pixi run -e dev python tools/doc-crawl/improved_extract_docs.py --limit 20

Dependencies: beautifulsoup4 (already), markitdown (cli), html2text (already in deps).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple

from bs4 import BeautifulSoup, NavigableString, Tag
import logging

try:
    import html2text  # type: ignore
except Exception:  # pragma: no cover - fallback if not available
    html2text = None  # type: ignore

LOG = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

PROJECT_ROOT = Path(__file__).parent.parent.parent
DOC_ROOT = PROJECT_ROOT / "casey-docs"
HTML_DIR = DOC_ROOT / "html"
OUTPUT_DIR = DOC_ROOT / "markdown"
TMP_DIR = PROJECT_ROOT / "tmp" / "doc_extraction"

SKIP_CLASSES = {"sidebar", "navigation", "breadcrumb", "toc", "sphinxsidebar"}
REMOVE_TAGS = {"nav", "script", "style", "header", "footer", "form"}

FIELD_LIST_SECTION_MAP = {
    "parameters": "Parameters",
    "parameter": "Parameters",
    "returns": "Returns",
    "return": "Returns",
    "yields": "Yields",
    "yield": "Yields",
    "raises": "Raises",
    "raise": "Raises",
    "see also": "See Also",
    "note": "Notes",
    "notes": "Notes",
}


@dataclass
class PageInfo:
    url: str
    filename: str

    @property
    def html_path(self) -> Path:
        return HTML_DIR / self.filename

    @property
    def module_stem(self) -> str:
        # Normalise URL path to module-ish slug
        path = self.url.replace("https://cascadeur.com/python-api/", "")
        path = path.replace("_generate/", "")
        path = path.replace(".html", "")
        return path.replace("/", "_") or "index"

    @property
    def output_path(self) -> Path:
        return OUTPUT_DIR / f"{self.module_stem}.md"


def read_pages_index(limit: Optional[int]) -> List[PageInfo]:
    idx_file = DOC_ROOT / "pages_index.json"
    with open(idx_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    if limit:
        data = data[:limit]
    return [PageInfo(url=d["url"], filename=d["filename"]) for d in data]


def load_main_soup(path: Path) -> Optional[Tag]:
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
        soup = BeautifulSoup(html, "lxml")

        # Remove unwanted structural tags early
        for t in soup.find_all(list(REMOVE_TAGS)):
            t.decompose()
        # Remove elements carrying any skip class
        for c in list(SKIP_CLASSES):
            for t in soup.find_all(attrs={"class": re.compile(rf"\b{re.escape(c)}\b")}):
                t.decompose()
        # Also remove elements hidden via style=display:none
        for t in soup.select("[style*='display:none']"):
            t.decompose()

        main = (
            soup.find("div", role="main")
            or soup.find("section", class_="document")
            or soup.find("div", class_="body")
            or soup.body
        )
        # Ensure we only return Tag (not NavigableString)
        return main if isinstance(main, Tag) else None
    except Exception as e:  # pragma: no cover - defensive
        LOG.error("Failed to parse %s: %s", path.name, e)
        return None


def normalise_signature_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    # Replace unicode arrow variants
    text = text.replace("→", "->").replace("⇒", "->")
    # Remove duplicate self param patterns like (self, self)
    text = re.sub(r"\bself,\s*self\b", "self", text)
    return text


def extract_field_list(field_dl: Tag) -> List[str]:
    lines: List[str] = []
    for dt in field_dl.find_all("dt", recursive=False):
        term = dt.get_text(" ", strip=True).lower()
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
        heading = FIELD_LIST_SECTION_MAP.get(term, None)
        body_lines: List[str] = []

        # Parameter style: <strong>name</strong> (<em>type</em>) – desc
        for p in dd.find_all(["p", "li"], recursive=True):
            txt = p.get_text(" ", strip=True)
            if not txt:
                continue
            # Split simple "name (type) – desc" pattern
            m = re.match(r"^(?P<name>[A-Za-z0-9_]+)\s*\((?P<type>[^)]+)\)\s*[–-]\s*(?P<desc>.+)$", txt)
            if m:
                body_lines.append(f"- `{m.group('name')}` ({m.group('type')}): {m.group('desc')}")
            else:
                body_lines.append(f"- {txt}")

        if heading and body_lines:
            lines.append(f"#### {heading}")
            lines.extend(body_lines)
            lines.append("")
    return lines


def codeblock(code: str, language: str = "python") -> str:
    code = code.rstrip()
    return f"```{language}\n{code}\n```"


def extract_tables(parent: Tag) -> None:
    for table in parent.find_all("table"):
        headers: List[str] = []
        rows: List[List[str]] = []
        thead = table.find("thead")
        if thead:
            headers = [th.get_text(" ", strip=True) for th in thead.find_all("th")]
        tbody = table.find("tbody") or table
        for tr in tbody.find_all("tr", recursive=False):
            cells = [td.get_text(" ", strip=True) for td in tr.find_all(["td", "th"], recursive=False)]
            if cells:
                rows.append(cells)
        # Build markdown table
        if headers and rows:
            md = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
            for r in rows:
                r = [c.replace("|", "\\|") for c in r]
                md.append("| " + " | ".join(r) + " |")
            container = BeautifulSoup("", "lxml").new_tag("div")
            container.string = "\n" + "\n".join(md) + "\n"
            table.replace_with(container)


def extract_content(main: Tag) -> str:
    extract_tables(main)

    lines: List[str] = []

    def flush_para(buf: List[str]):
        if buf:
            lines.append(" ".join(buf).strip())
            buf.clear()

    paragraph_buf: List[str] = []

    for element in main.descendants:
        if isinstance(element, NavigableString):
            continue  # Raw text handled at tag level for better control
        if not isinstance(element, Tag):
            continue

        name = element.name

        # Signatures (Sphinx style definition lists)
        if name == "dl" and element.get("class") and any("sig" in c for c in element.get("class", [])):
            flush_para(paragraph_buf)
            dt = element.find("dt")
            if dt and isinstance(dt, Tag):
                sig_text = normalise_signature_text(dt.get_text(" ", strip=True))
                # Determine type (class vs func) heuristically
                level_header = "###"
                if re.search(r"\bclass\b", sig_text):
                    level_header = "##"
                lines.append(f"{level_header} {sig_text}")
                # If signature long, also show fenced code for clarity
                if len(sig_text) > 80:
                    lines.append(codeblock(sig_text))
                lines.append("")
            dd = element.find("dd")
            if dd and isinstance(dd, Tag):
                # Field lists inside dd (class contains 'field-list')
                for field_dl in dd.find_all("dl", class_=re.compile(r"field-list")):
                    lines.extend(extract_field_list(field_dl))
                # Remaining paragraphs
                for p in dd.find_all("p", recursive=False):
                    if not isinstance(p, Tag):
                        continue
                    txt = p.get_text(" ", strip=True)
                    if txt:
                        lines.append(txt)
                lines.append("")
            continue

        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            flush_para(paragraph_buf)
            level = int(name[1])
            title = element.get_text(" ", strip=True)
            if title:
                lines.append("#" * level + f" {title}")
                lines.append("")
            continue

        if name == "pre":
            flush_para(paragraph_buf)
            code_el = element.find("code") or element
            language = "python"
            if isinstance(code_el, Tag):
                classes = code_el.get("class", [])
                for c in classes:
                    if c.startswith("language-"):
                        language = c.split("-", 1)[1]
                code_text = code_el.get_text("\n", strip=True)
            else:
                code_text = str(code_el).strip()
            if code_text:
                lines.append(codeblock(code_text, language))
                lines.append("")
            continue

        if name == "p":
            txt = element.get_text(" ", strip=True)
            if txt:
                paragraph_buf.append(txt)
            continue

        if name in {"ul", "ol"}:
            flush_para(paragraph_buf)
            for i, li in enumerate(element.find_all("li", recursive=False), 1):
                li_txt = li.get_text(" ", strip=True)
                if not li_txt:
                    continue
                if name == "ul":
                    lines.append(f"- {li_txt}")
                else:
                    lines.append(f"{i}. {li_txt}")
            lines.append("")
            continue

        if name == "blockquote":
            flush_para(paragraph_buf)
            txt = element.get_text("\n", strip=True)
            if txt:
                bq = "\n".join("> " + ln for ln in txt.splitlines())
                lines.append(bq)
                lines.append("")
            continue

    flush_para(paragraph_buf)

    content = "\n".join(line.rstrip() for line in lines if line is not None)
    # Normalise blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)
    return cleanup_text(content.strip())


UNICODE_REPLACEMENTS = {
    "\u00a0": " ",  # non-breaking space
    "Â": "",  # stray Latin-1 decode artifacts
    "Â¶": "",  # paragraph anchor
    "¶": "",  # paragraph anchor
    "â": "–",  # en dash
    "â": "—",  # em dash
    "â": "'",  # apostrophe
    "â¦": "…",  # ellipsis
}


def cleanup_text(text: str) -> str:
    # Unicode artifact fixes
    for bad, good in UNICODE_REPLACEMENTS.items():
        text = text.replace(bad, good)

    # Remove duplicate spaces
    text = re.sub(r"[ \t]{2,}", " ", text)

    # Collapse duplicated blank lines again (after replacements)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Heuristic: ensure newline before occurrences of '<identifier> class' or ' enumeration'
    text = re.sub(
        r"(?<!\n)(?=\b[A-Za-z_][\w\.]+ (?:class|enumeration)\b)",
        "\n",
        text,
    )

    # Remove trailing 'Members:' lines duplication (keep first list)
    text = re.sub(r"(Members:\n(?:> .+\n)+)(?:\1)+", r"\1", text)

    # Strip leftover anchor section symbols
    text = re.sub(r"\s+Â¶", "", text)

    return text.strip()


def markitdown_convert(html_path: Path) -> Optional[str]:
    try:
        # Use binary capture then decode manually to survive mixed encodings
        result = subprocess.run(["markitdown", str(html_path)], capture_output=True)
        if result.returncode != 0:
            return None
        stdout_bytes = result.stdout if isinstance(result.stdout, (bytes, bytearray)) else bytes(str(result.stdout), 'utf-8', 'ignore')
        try:
            text_out = stdout_bytes.decode('utf-8')
        except Exception:
            # Fallback latin-1 then replace undecodable
            text_out = stdout_bytes.decode('latin-1', errors='ignore')
        text_out = text_out.strip()
        if text_out:
            return text_out
    except FileNotFoundError:
        LOG.warning("markitdown not found on PATH; skipping fallback.")
    except Exception as e:  # pragma: no cover
        LOG.warning("markitdown conversion failed for %s: %s", html_path.name, e)
    return None


def html2text_convert(html_path: Path) -> Optional[str]:
    if not html2text:
        return None
    try:
        with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
            html = f.read()
        conv = html2text.HTML2Text()
        conv.ignore_links = False
        conv.images_to_alt = True
        conv.skip_internal_links = True
        conv.ignore_emphasis = False
        return conv.handle(html).strip()
    except Exception:
        return None


def build_front_matter(page: PageInfo, body: str) -> str:
    meta = (
        f"---\nsource_url: {page.url}\nhtml_file: {page.filename}\nmodule: {page.module_stem}\n---\n\n"
    )
    return meta + body


def process_page(page: PageInfo, min_length: int = 200) -> Tuple[bool, Optional[Path]]:
    main = load_main_soup(page.html_path)
    if not main:
        LOG.warning("No main content for %s", page.filename)
        return False, None
    body = extract_content(main)
    if len(body) < min_length:
        # Attempt fallback conversions
        LOG.info("Fallback conversion for %s (length=%d)", page.filename, len(body))
        md = markitdown_convert(page.html_path) or html2text_convert(page.html_path) or body
        body = md
    if not body.strip():
        return False, None
    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = page.output_path
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(build_front_matter(page, body))
    return True, out_path


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Convert Cascadeur HTML docs to Markdown (improved)")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--all", action="store_true", help="Process all pages in pages_index.json")
    g.add_argument("--file", type=str, help="Path to a single HTML file to convert")
    p.add_argument("--limit", type=int, help="Limit number of pages (for --all mode)")
    p.add_argument("--min-length", type=int, default=200, help="Minimum char length before fallback triggers")
    return p.parse_args()


def main():  # pragma: no cover - CLI
    args = parse_args()
    successes = 0
    failures = 0
    processed: List[Path] = []

    if args.file:
        # Derive URL placeholder
        html_path = Path(args.file)
        if not html_path.is_file():
            raise SystemExit(f"File not found: {html_path}")
        dummy_url = "https://cascadeur.com/python-api/" + html_path.stem + ".html"
        page = PageInfo(url=dummy_url, filename=html_path.name)
        ok, out = process_page(page, args.min_length)
        if ok:
            successes += 1
            processed.append(out)  # type: ignore
        else:
            failures += 1
    else:
        pages = read_pages_index(args.limit if args.all or args.limit else 10)
        if args.all and not args.limit:
            LOG.info("Processing all %d pages", len(pages))
        else:
            LOG.info("Processing %d pages (limit/testing mode)", len(pages))
        for i, page in enumerate(pages, 1):
            ok, out = process_page(page, args.min_length)
            if ok:
                successes += 1
                processed.append(out)  # type: ignore
                LOG.info("[%d/%d] ✓ %s", i, len(pages), page.module_stem)
            else:
                failures += 1
                LOG.warning("[%d/%d] ✗ %s", i, len(pages), page.module_stem)

    LOG.info("Done. Success=%d Failures=%d OutputDir=%s", successes, failures, OUTPUT_DIR)
    if processed:
        LOG.info("First outputs: %s", ", ".join(p.name for p in processed[:5]))


if __name__ == "__main__":  # pragma: no cover
    main()
