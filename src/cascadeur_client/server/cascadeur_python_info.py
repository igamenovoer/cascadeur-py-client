"""
Utility to inspect and save Cascadeur's Python interpreter information.

This script collects comprehensive information about the Python environment
and saves it to a JSON file. Designed to work within Cascadeur's restricted
Python environment where console output and sockets are unavailable.
"""

import os
import sys
import json
import platform
import tempfile
import datetime
import sysconfig
from pathlib import Path
from typing import Dict, List, Any, Optional


def get_python_info() -> Dict[str, Any]:
    """
    Collect comprehensive Python interpreter information.
    
    Returns:
        Dictionary containing all Python environment details
    """
    info: Dict[str, Any] = {}
    
    # Basic Python version info
    info['python'] = {
        'version': sys.version,
        'version_info': {
            'major': sys.version_info.major,
            'minor': sys.version_info.minor,
            'micro': sys.version_info.micro,
            'releaselevel': sys.version_info.releaselevel,
            'serial': sys.version_info.serial
        },
        'implementation': platform.python_implementation(),
        'compiler': platform.python_compiler(),
        'build': platform.python_build(),
        'branch': platform.python_branch() if hasattr(platform, 'python_branch') else None,
        'revision': platform.python_revision() if hasattr(platform, 'python_revision') else None
    }
    
    # System platform information
    info['platform'] = {
        'system': platform.system(),
        'node': platform.node(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'architecture': platform.architecture(),
        'platform': platform.platform()
    }
    
    # Python paths and locations
    info['paths'] = {
        'executable': sys.executable,
        'prefix': sys.prefix,
        'exec_prefix': sys.exec_prefix,
        'base_prefix': getattr(sys, 'base_prefix', None),
        'base_exec_prefix': getattr(sys, 'base_exec_prefix', None),
        'path': sys.path,
        'stdlib': sysconfig.get_path('stdlib'),
        'platstdlib': sysconfig.get_path('platstdlib'),
        'purelib': sysconfig.get_path('purelib'),
        'platlib': sysconfig.get_path('platlib'),
        'include': sysconfig.get_path('include'),
        'scripts': sysconfig.get_path('scripts'),
        'data': sysconfig.get_path('data')
    }
    
    # System configuration
    info['sysconfig'] = {
        'platform': sysconfig.get_platform(),
        'python_version': sysconfig.get_python_version(),
        'config_vars': dict(sysconfig.get_config_vars())
    }
    
    # Environment variables (filter for relevant ones)
    cascadeur_env_vars: Dict[str, str] = {}
    python_env_vars: Dict[str, str] = {}
    path_vars: Dict[str, str] = {}
    
    for key, value in os.environ.items():
        if 'CASCADEUR' in key.upper():
            cascadeur_env_vars[key] = value
        elif 'PYTHON' in key.upper() or 'PY' in key.upper():
            python_env_vars[key] = value
        elif 'PATH' in key.upper():
            path_vars[key] = value
    
    info['environment'] = {
        'cascadeur': cascadeur_env_vars,
        'python': python_env_vars,
        'paths': path_vars,
        'all_keys': list(os.environ.keys())
    }
    
    # Runtime flags and features
    info['runtime'] = {
        'interactive': hasattr(sys, 'ps1'),
        'debugging': sys.flags.debug,
        'optimized': sys.flags.optimize,
        'dont_write_bytecode': sys.flags.dont_write_bytecode,
        'no_user_site': sys.flags.no_user_site,
        'no_site': sys.flags.no_site,
        'ignore_environment': sys.flags.ignore_environment,
        'verbose': sys.flags.verbose,
        'bytes_warning': sys.flags.bytes_warning,
        'quiet': sys.flags.quiet,
        'hash_randomization': sys.flags.hash_randomization,
        'isolated': sys.flags.isolated if hasattr(sys.flags, 'isolated') else None,
        'dev_mode': sys.flags.dev_mode if hasattr(sys.flags, 'dev_mode') else None,
        'utf8_mode': sys.flags.utf8_mode if hasattr(sys.flags, 'utf8_mode') else None
    }
    
    # Module availability check
    check_modules: List[str] = [
        'cascadeur', 'csc', 'numpy', 'scipy', 'PIL', 'cv2',
        'mathutils', 'bpy', 'PySide2', 'PyQt5', 'tkinter'
    ]
    
    available_modules: Dict[str, bool] = {}
    for module_name in check_modules:
        try:
            __import__(module_name)
            available_modules[module_name] = True
        except ImportError:
            available_modules[module_name] = False
    
    info['modules'] = {
        'builtin': list(sys.builtin_module_names),
        'available_check': available_modules,
        'path_hooks': [str(hook) for hook in sys.path_hooks],
        'meta_path': [str(finder) for finder in sys.meta_path]
    }
    
    # Memory and limits
    info['limits'] = {
        'maxsize': sys.maxsize,
        'maxunicode': sys.maxunicode,
        'float_info': {
            'max': sys.float_info.max,
            'min': sys.float_info.min,
            'epsilon': sys.float_info.epsilon,
            'dig': sys.float_info.dig,
            'mant_dig': sys.float_info.mant_dig
        },
        'int_info': {
            'bits_per_digit': sys.int_info.bits_per_digit,
            'sizeof_digit': sys.int_info.sizeof_digit
        } if hasattr(sys, 'int_info') else None,
        'hash_info': {
            'width': sys.hash_info.width,
            'modulus': sys.hash_info.modulus,
            'inf': sys.hash_info.inf,
            'nan': sys.hash_info.nan,
            'imag': sys.hash_info.imag
        } if hasattr(sys, 'hash_info') else None,
        'recursion_limit': sys.getrecursionlimit()
    }
    
    # Encoding information
    info['encoding'] = {
        'default': sys.getdefaultencoding(),
        'filesystem': sys.getfilesystemencoding(),
        'filesystem_errors': sys.getfilesystemencodeerrors() if hasattr(sys, 'getfilesystemencodeerrors') else None,
        'stdin': sys.stdin.encoding if hasattr(sys.stdin, 'encoding') else None,
        'stdout': sys.stdout.encoding if hasattr(sys.stdout, 'encoding') else None,
        'stderr': sys.stderr.encoding if hasattr(sys.stderr, 'encoding') else None
    }
    
    # Timestamp
    info['timestamp'] = {
        'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'local': datetime.datetime.now().isoformat(),
        'timezone': str(datetime.datetime.now().astimezone().tzinfo)
    }
    
    return info


def get_output_path() -> Path:
    """
    Determine the output directory based on environment variable or default to temp.
    
    Returns:
        Path object for the output file location
    """
    output_dir_str: Optional[str] = os.environ.get('CASCADEUR_PYTHON_OUTPUT_DIR')
    
    if output_dir_str:
        output_dir = Path(output_dir_str)
        # Create directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        # Use system temp directory
        output_dir = Path(tempfile.gettempdir())
    
    return output_dir / 'cascadeur_python_info.json'


def save_python_info() -> str:
    """
    Main function to collect and save Python interpreter information.
    
    Returns:
        Path to the saved JSON file as string
    """
    # Collect all Python info
    info: Dict[str, Any] = get_python_info()
    
    # Get output path
    output_path: Path = get_output_path()
    
    # Add output path to info
    info['output'] = {
        'file': str(output_path),
        'directory': str(output_path.parent),
        'env_var_used': 'CASCADEUR_PYTHON_OUTPUT_DIR' in os.environ
    }
    
    # Save to JSON file with pretty formatting
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(info, f, indent=2, default=str, ensure_ascii=False)
    
    return str(output_path)


# Execute when script is run
# Note: No if __name__ == "__main__" block per Cascadeur requirements
# This will execute directly when imported or run in Cascadeur's interactive environment

try:
    output_file: str = save_python_info()
    # Since Cascadeur doesn't allow console output, we save the result path to a marker file
    marker_path = Path(tempfile.gettempdir()) / 'cascadeur_python_info_result.txt'
    with open(marker_path, 'w', encoding='utf-8') as f:
        f.write(f"Python info saved to: {output_file}\n")
        f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
except Exception as e:
    # Save error information to a file since we can't print
    error_path = Path(tempfile.gettempdir()) / 'cascadeur_python_info_error.txt'
    with open(error_path, 'w', encoding='utf-8') as f:
        f.write(f"Error collecting Python info: {str(e)}\n")
        f.write(f"Error type: {type(e).__name__}\n")
        f.write(f"Timestamp: {datetime.datetime.now().isoformat()}\n")
        import traceback
        f.write(f"Traceback:\n{traceback.format_exc()}\n")