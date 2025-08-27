#!/usr/bin/env python
"""
Pip-like package manager for Cascadeur's embedded Python environment.

Since Cascadeur uses an embedded Python without python.exe, we use an external
Python environment to manage packages in Cascadeur's site-packages.

Usage:
    python pip_for_cascadeur.py install <package>
    python pip_for_cascadeur.py uninstall <package>
    python pip_for_cascadeur.py list
"""

import os
import sys
import json
import shutil
import tempfile
import argparse
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
import platformdirs


def find_cascadeur_path() -> Optional[Path]:
    """
    Find Cascadeur installation path from environment or platform-specific locations.
    
    Returns:
        Path to Cascadeur installation or None if not found
    """
    # Check environment variable first
    env_path = os.environ.get('CASCADEUR_PATH')
    if env_path:
        path = Path(env_path)
        if path.exists():
            return path
    
    # Use platformdirs to find standard application paths
    app_name = 'Cascadeur'
    
    # Check user-specific application data directory (most common on Windows)
    user_data_path = Path(platformdirs.user_data_dir(app_name, appauthor=False))
    if user_data_path.exists():
        return user_data_path
    
    # Check system-wide application data directories
    site_data_paths = platformdirs.site_data_dir(app_name, appauthor=False, multipath=True)
    for site_path_str in site_data_paths.split(os.pathsep):
        site_path = Path(site_path_str)
        if site_path.exists():
            return site_path
    
    # Fall back to OS-specific default paths
    if sys.platform == 'win32':
        # Windows-specific paths
        default_paths = [
            Path('C:/Program Files/Cascadeur'),
            Path('C:/Program Files (x86)/Cascadeur'),
        ]
    elif sys.platform == 'darwin':
        # macOS-specific paths
        default_paths = [
            Path('/Applications/Cascadeur.app'),
            Path.home() / 'Applications' / 'Cascadeur.app',
        ]
    else:
        # Linux-specific paths
        default_paths = [
            Path('/opt/cascadeur'),
            Path('/usr/local/cascadeur'),
            Path.home() / '.cascadeur',
        ]
    
    for path in default_paths:
        if path.exists():
            return path
    
    return None


def get_cascadeur_site_packages(cascadeur_path: Path, verbose: bool = True) -> List[Path]:
    """
    Get all possible site-packages directories in Cascadeur.
    
    Based on Cascadeur's Python configuration:
    - {cascadeur}/Lib/site-packages - sysconfig purelib/platlib location
    - {cascadeur}/python/Lib/site-packages - sys.path location
    
    Args:
        cascadeur_path: Path to Cascadeur installation
        verbose: Whether to print diagnostic information
        
    Returns:
        List of existing site-packages paths
    """
    # These paths are based on actual Cascadeur Python environment analysis
    possible_paths = [
        cascadeur_path / 'Lib' / 'site-packages',  # sysconfig: purelib/platlib
        cascadeur_path / 'python' / 'Lib' / 'site-packages',  # sys.path entry
    ]
    
    if verbose:
        print("\nCascadeur site-packages directories:")
        print("-" * 50)
    
    existing_paths = []
    for path in possible_paths:
        if path.exists():
            if verbose:
                role = "sysconfig location" if "python" not in str(path) else "sys.path location"
                print(f"  [FOUND] {path}")
                print(f"          ({role})")
            existing_paths.append(path)
        else:
            if verbose:
                print(f"  [MISS]  {path}")
    
    if verbose and not existing_paths:
        print("\n[WARNING] No site-packages directories found!")
        print("  This means Cascadeur's Python installation may be incomplete.")
        print("  Expected locations based on standard Cascadeur setup:")
        for path in possible_paths:
            print(f"    - {path}")
    elif verbose:
        print(f"\n  Active site-packages: {existing_paths[0]}")
    
    return existing_paths


def is_local_package(package_spec: str) -> Tuple[bool, Optional[Path]]:
    """
    Check if a package specification refers to a local path.
    
    Args:
        package_spec: Package specification (name or path)
        
    Returns:
        Tuple of (is_local, resolved_path)
    """
    # Check for editable install prefix
    if package_spec.startswith('-e '):
        package_spec = package_spec[3:].strip()
    
    # Common indicators of local paths
    if package_spec in ['.', '..'] or package_spec.startswith(('./','../', '/', '\\')):
        path = Path(package_spec).resolve()
        if path.exists():
            return True, path
    
    # Check if it's an existing path without indicators
    path = Path(package_spec)
    if path.exists() and (path.is_dir() or path.suffix in ['.whl', '.tar.gz', '.zip']):
        return True, path.resolve()
    
    return False, None


def create_pth_file(
    project_path: Path,
    site_packages: Path,
    package_name: Optional[str] = None
) -> bool:
    """
    Create a .pth file for editable installation.
    
    Args:
        project_path: Path to the project directory
        site_packages: Path to site-packages directory
        package_name: Optional package name for the .pth file
        
    Returns:
        True if successful
    """
    # Find the source directory (usually 'src' or the project root)
    src_dirs = []
    
    # Check for src layout
    src_path = project_path / 'src'
    if src_path.exists() and src_path.is_dir():
        src_dirs.append(str(src_path.resolve()))
    
    # Check for flat layout (packages directly in project root)
    pyproject = project_path / 'pyproject.toml'
    setup_py = project_path / 'setup.py'
    if pyproject.exists() or setup_py.exists():
        # Add project root for flat layout
        if not src_dirs:  # Only if src layout wasn't detected
            src_dirs.append(str(project_path.resolve()))
    
    if not src_dirs:
        print(f"Error: Could not determine source directory for {project_path}")
        return False
    
    # Determine package name if not provided
    if not package_name:
        if pyproject.exists():
            try:
                import tomllib  # type: ignore
            except ImportError:
                try:
                    import tomli as tomllib  # type: ignore
                except ImportError:
                    # Fallback to basic parsing
                    package_name = project_path.name
                    tomllib = None  # type: ignore
            
            if tomllib is not None:
                try:
                    with open(pyproject, 'rb') as f:
                        data = tomllib.load(f)
                    package_name = data.get('project', {}).get('name', project_path.name)
                except:
                    package_name = project_path.name
        else:
            package_name = project_path.name
    
    # Create .pth file
    pth_file = site_packages / f"{package_name}.pth"
    try:
        with open(pth_file, 'w') as f:
            for src_dir in src_dirs:
                f.write(f"{src_dir}\n")
        print(f"Created .pth file: {pth_file}")
        print(f"  Pointing to: {', '.join(src_dirs)}")
        return True
    except Exception as e:
        print(f"Error creating .pth file: {e}")
        return False


def install_packages(
    packages: List[str],
    cascadeur_path: Path,
    upgrade: bool = False,
    force_reinstall: bool = False,
    no_deps: bool = False,
    requirements: Optional[Path] = None,
    editable: bool = False
) -> bool:
    """
    Install packages into Cascadeur's Python environment.
    
    Args:
        packages: List of package specifications
        cascadeur_path: Path to Cascadeur installation
        upgrade: Whether to upgrade existing packages
        force_reinstall: Whether to reinstall packages
        no_deps: Whether to skip dependencies
        requirements: Path to requirements file
        
    Returns:
        True if all installations succeeded
    """
    site_packages = get_cascadeur_site_packages(cascadeur_path, verbose=False)
    if not site_packages:
        print(f"Error: No site-packages found in {cascadeur_path}")
        print("Please ensure Cascadeur is properly installed.")
        return False
    
    # Use the first valid site-packages
    target = site_packages[0]
    
    # Handle requirements file
    if requirements:
        if not requirements.exists():
            print(f"Error: Requirements file not found: {requirements}")
            return False
        with open(requirements, 'r') as f:
            packages = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not packages:
        print("Error: No packages specified")
        return False
    
    success = True
    for package_spec in packages:
        # Check if package is editable (starts with -e)
        is_editable = editable or package_spec.startswith('-e ')
        if package_spec.startswith('-e '):
            package_spec = package_spec[3:].strip()
        
        # Check if this is a local package
        is_local, local_path = is_local_package(package_spec)
        
        if is_local and is_editable:
            # Handle editable installation with .pth file
            print(f"Installing {local_path} in editable mode...")
            
            # First, install dependencies only
            if not no_deps:
                print("Installing dependencies...")
                cmd = [
                    sys.executable, '-m', 'pip', 'install',
                    '--target', str(target),
                    '--no-user',
                    '--disable-pip-version-check',
                    '--only-deps',  # This might not work with all pip versions
                ]
                cmd.append(str(local_path))
                
                # Try installing dependencies
                try:
                    # First attempt with --only-deps (if supported)
                    result = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        check=False  # Don't raise on error
                    )
                    
                    if result.returncode != 0 and '--only-deps' in result.stderr:
                        # --only-deps not supported, try alternative approach
                        # Read dependencies from pyproject.toml or setup.py
                        if local_path:
                            pyproject = local_path / 'pyproject.toml'
                            if pyproject.exists():
                                print("Installing dependencies from pyproject.toml...")
                                try:
                                    import tomllib  # type: ignore
                                except ImportError:
                                    try:
                                        import tomli as tomllib  # type: ignore
                                    except ImportError:
                                        print("Warning: Could not read pyproject.toml dependencies")
                                        tomllib = None  # type: ignore
                                
                                if tomllib:
                                    try:
                                        with open(pyproject, 'rb') as f:
                                            data = tomllib.load(f)
                                        deps = data.get('project', {}).get('dependencies', [])
                                        if deps:
                                            for dep in deps:
                                                dep_cmd = [
                                                    sys.executable, '-m', 'pip', 'install',
                                                    '--target', str(target),
                                                    '--no-user',
                                                    '--disable-pip-version-check',
                                                    dep
                                                ]
                                                subprocess.run(dep_cmd, capture_output=True, text=True)
                                    except Exception as e:
                                        print(f"Warning: Could not install dependencies: {e}")
                        else:
                            print("Warning: local_path is None, skipping dependency installation")
                except subprocess.CalledProcessError as e:
                    print(f"Warning: Could not install dependencies: {e.stderr}")
            
            # Create .pth file for editable install
            if local_path and not create_pth_file(local_path, target):
                success = False
            elif local_path:
                print(f"Successfully installed {local_path} (editable)")
        
        elif is_local and local_path:
            # Regular local package installation
            print(f"Installing {local_path}...")
            
            # Build pip install command for local package
            cmd = [
                sys.executable, '-m', 'pip', 'install',
                '--target', str(target),
                '--no-user',
                '--disable-pip-version-check',
            ]
            
            if upgrade:
                cmd.append('--upgrade')
            
            if force_reinstall:
                cmd.append('--force-reinstall')
            
            if no_deps:
                cmd.append('--no-deps')
            
            cmd.append(str(local_path))
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(result.stdout)
                print(f"Successfully installed {local_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {local_path}:")
                print(e.stderr)
                success = False
        
        else:
            # Regular PyPI package installation
            print(f"Installing {package_spec}...")
            
            # Build pip install command
            cmd = [
                sys.executable, '-m', 'pip', 'install',
                '--target', str(target),
                '--no-user',
                '--disable-pip-version-check',
            ]
            
            if upgrade:
                cmd.append('--upgrade')
            
            if force_reinstall:
                cmd.append('--force-reinstall')
            
            if no_deps:
                cmd.append('--no-deps')
            
            cmd.append(package_spec)
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error installing {package_spec}:")
                print(e.stderr)
                success = False
    
    return success


def uninstall_packages(
    packages: List[str],
    cascadeur_path: Path,
    yes: bool = False
) -> bool:
    """
    Uninstall packages from Cascadeur's Python environment.
    
    Args:
        packages: List of package names to uninstall
        cascadeur_path: Path to Cascadeur installation
        yes: Skip confirmation prompt
        
    Returns:
        True if all uninstalls succeeded
    """
    site_packages = get_cascadeur_site_packages(cascadeur_path, verbose=False)
    if not site_packages:
        print(f"Error: No site-packages found in {cascadeur_path}")
        return False
    
    # Use the first valid site-packages
    target = site_packages[0]
    
    success = True
    for package in packages:
        # Check if this is a path (for uninstalling local packages)
        is_local, local_path = is_local_package(package)
        if is_local and local_path:
            # For local packages, try to determine the package name
            pyproject = local_path / 'pyproject.toml'
            if pyproject.exists():
                try:
                    import tomllib  # type: ignore
                except ImportError:
                    try:
                        import tomli as tomllib  # type: ignore
                    except ImportError:
                        tomllib = None  # type: ignore
                
                if tomllib:
                    try:
                        with open(pyproject, 'rb') as f:
                            data = tomllib.load(f)
                        package = data.get('project', {}).get('name', local_path.name)
                    except:
                        package = local_path.name
                else:
                    package = local_path.name
            else:
                package = local_path.name
        # Find package directories
        package_dirs: List[Path] = []
        dist_info_pattern = f"{package}*.dist-info"
        egg_info_pattern = f"{package}*.egg-info"
        
        for pattern in [dist_info_pattern, egg_info_pattern]:
            package_dirs.extend(target.glob(pattern))
        
        # Also look for the package directory itself
        package_dir = target / package
        if package_dir.exists():
            package_dirs.append(package_dir)
        
        # Convert package name to normalized form (replace - with _)
        normalized_package = package.replace('-', '_')
        if normalized_package != package:
            normalized_dir = target / normalized_package
            if normalized_dir.exists():
                package_dirs.append(normalized_dir)
        
        # Also check for .pth files (editable installs)
        pth_files = list(target.glob(f"{package}*.pth"))
        pth_files.extend(list(target.glob(f"{normalized_package}*.pth")))
        
        if not package_dirs and not pth_files:
            print(f"Package '{package}' is not installed")
            continue
        
        # Confirm uninstall
        if not yes:
            print(f"Found the following items for '{package}':")
            for d in package_dirs:
                print(f"  - {d}")
            for pth in pth_files:
                print(f"  - {pth} (.pth file for editable install)")
            response = input(f"Uninstall '{package}'? [y/N] ")
            if response.lower() != 'y':
                print(f"Skipping {package}")
                continue
        
        # Remove package directories and .pth files
        print(f"Uninstalling {package}...")
        for d in package_dirs:
            try:
                if d.is_dir():
                    shutil.rmtree(d)
                else:
                    d.unlink()
                print(f"  Removed {d}")
            except Exception as e:
                print(f"  Error removing {d}: {e}")
                success = False
        
        # Remove .pth files
        for pth_file in pth_files:
            try:
                pth_file.unlink()
                print(f"  Removed {pth_file} (editable install)")
            except Exception as e:
                print(f"  Error removing {pth_file}: {e}")
                success = False
    
    return success


def print_cascadeur_info(cascadeur_path: Path) -> None:
    """
    Print detailed information about Cascadeur's Python environment.
    
    Args:
        cascadeur_path: Path to Cascadeur installation
    """
    print(f"\nCascadeur Installation Info:")
    print("=" * 60)
    print(f"Installation path: {cascadeur_path}")
    print(f"Note: Cascadeur uses embedded Python (runs through cascadeur.exe)")
    
    # Always show site-packages discovery
    get_cascadeur_site_packages(cascadeur_path, verbose=True)


def list_installed_packages(cascadeur_path: Path, verbose: bool = True) -> Dict[str, str]:
    """
    List packages installed in Cascadeur's Python environment.
    
    Args:
        cascadeur_path: Path to Cascadeur installation
        verbose: Whether to print diagnostic information
        
    Returns:
        Dictionary of package name to version
    """
    packages = {}
    site_packages = get_cascadeur_site_packages(cascadeur_path, verbose=verbose)
    
    for sp_dir in site_packages:
        # Look for .dist-info directories
        for dist_info in sp_dir.glob('*.dist-info'):
            metadata_file = dist_info / 'METADATA'
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.startswith('Name:'):
                                name = line.split(':', 1)[1].strip()
                            elif line.startswith('Version:'):
                                version = line.split(':', 1)[1].strip()
                                packages[name] = version
                                break
                except Exception:
                    pass
    
    return packages


def cmd_install(args: argparse.Namespace) -> int:
    """Handle install command."""
    cascadeur_path = args.cascadeur_path or find_cascadeur_path()
    if not cascadeur_path:
        print("Error: Could not find Cascadeur installation")
        print("Please set CASCADEUR_PATH environment variable or use --cascadeur-path")
        return 1
    
    print(f"Using Cascadeur at: {cascadeur_path}")
    
    success = install_packages(
        args.packages,
        cascadeur_path,
        upgrade=args.upgrade,
        force_reinstall=args.force_reinstall,
        no_deps=args.no_deps,
        requirements=args.requirements,
        editable=args.editable
    )
    
    return 0 if success else 1


def cmd_uninstall(args: argparse.Namespace) -> int:
    """Handle uninstall command."""
    cascadeur_path = args.cascadeur_path or find_cascadeur_path()
    if not cascadeur_path:
        print("Error: Could not find Cascadeur installation")
        print("Please set CASCADEUR_PATH environment variable or use --cascadeur-path")
        return 1
    
    print(f"Using Cascadeur at: {cascadeur_path}")
    
    success = uninstall_packages(
        args.packages,
        cascadeur_path,
        yes=args.yes
    )
    
    return 0 if success else 1


def cmd_list(args: argparse.Namespace) -> int:
    """Handle list command."""
    cascadeur_path = args.cascadeur_path or find_cascadeur_path()
    if not cascadeur_path:
        print("Error: Could not find Cascadeur installation")
        print("Please set CASCADEUR_PATH environment variable or use --cascadeur-path")
        return 1
    
    print(f"Using Cascadeur at: {cascadeur_path}")
    
    # Show site-packages info if verbose
    if args.verbose:
        print_cascadeur_info(cascadeur_path)
    
    packages = list_installed_packages(cascadeur_path, verbose=False)
    
    if args.format == 'json':
        print(json.dumps({name: version for name, version in packages.items()}, indent=2))
    elif args.format == 'freeze':
        for name, version in sorted(packages.items()):
            print(f"{name}=={version}")
    else:  # default format
        if packages:
            print("\nPackage                        Version")
            print("-" * 40)
            for name, version in sorted(packages.items()):
                print(f"{name:<30} {version}")
        else:
            print("No packages installed")
    
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='pip_for_cascadeur',
        description='Pip-like package manager for Cascadeur\'s embedded Python'
    )
    
    # Global options
    parser.add_argument(
        '--cascadeur-path',
        type=Path,
        help='Path to Cascadeur installation (auto-detected if not specified)'
    )
    
    # Create subparsers
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Install command
    install_parser = subparsers.add_parser('install', help='Install packages')
    install_parser.add_argument(
        'packages',
        nargs='+',
        help='Package(s) to install (e.g., requests, numpy==1.24.0, . , /path/to/project)'
    )
    install_parser.add_argument(
        '-e', '--editable',
        action='store_true',
        help='Install packages in editable/development mode (for local packages)'
    )
    install_parser.add_argument(
        '-U', '--upgrade',
        action='store_true',
        help='Upgrade packages to latest version'
    )
    install_parser.add_argument(
        '--force-reinstall',
        action='store_true',
        help='Reinstall packages even if they are already up-to-date'
    )
    install_parser.add_argument(
        '--no-deps',
        action='store_true',
        help='Don\'t install package dependencies'
    )
    install_parser.add_argument(
        '-r', '--requirements',
        type=Path,
        help='Install from requirements file'
    )
    
    # Uninstall command
    uninstall_parser = subparsers.add_parser('uninstall', help='Uninstall packages')
    uninstall_parser.add_argument(
        'packages',
        nargs='+',
        help='Package(s) to uninstall'
    )
    uninstall_parser.add_argument(
        '-y', '--yes',
        action='store_true',
        help='Don\'t ask for confirmation'
    )
    
    # List command
    list_parser = subparsers.add_parser('list', help='List installed packages')
    list_parser.add_argument(
        '--format',
        choices=['default', 'json', 'freeze'],
        default='default',
        help='Output format'
    )
    list_parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed information'
    )
    
    args = parser.parse_args()
    
    # Show help if no command specified
    if not args.command:
        parser.print_help()
        return 1
    
    # Route to appropriate command handler
    if args.command == 'install':
        return cmd_install(args)
    elif args.command == 'uninstall':
        return cmd_uninstall(args)
    elif args.command == 'list':
        return cmd_list(args)
    else:
        parser.print_help()
        return 1


if __name__ == '__main__':
    sys.exit(main())