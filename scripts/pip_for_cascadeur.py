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
from typing import Optional, List, Dict, Any
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


def install_packages(
    packages: List[str],
    cascadeur_path: Path,
    upgrade: bool = False,
    force_reinstall: bool = False,
    no_deps: bool = False,
    requirements: Optional[Path] = None
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
    for package in packages:
        print(f"Installing {package}...")
        
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
        
        cmd.append(package)
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}:")
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
        # Find package directories
        package_dirs = []
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
        
        if not package_dirs:
            print(f"Package '{package}' is not installed")
            continue
        
        # Confirm uninstall
        if not yes:
            print(f"Found the following directories for '{package}':")
            for d in package_dirs:
                print(f"  - {d}")
            response = input(f"Uninstall '{package}'? [y/N] ")
            if response.lower() != 'y':
                print(f"Skipping {package}")
                continue
        
        # Remove package directories
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


def cmd_install(args) -> int:
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
        requirements=args.requirements
    )
    
    return 0 if success else 1


def cmd_uninstall(args) -> int:
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


def cmd_list(args) -> int:
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


def main():
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
        help='Package(s) to install (e.g., requests, numpy==1.24.0)'
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