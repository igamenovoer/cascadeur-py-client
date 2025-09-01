# How to Configure Pixi for Platform-Specific PyTorch Dependencies

This guide explains how to configure Pixi to use PyTorch with CUDA on Linux and Windows, but CPU-only PyTorch on macOS platforms.

## Problem Statement

When developing cross-platform applications with PyTorch, you often need:
- CUDA-enabled PyTorch on Linux and Windows (for GPU acceleration)
- CPU-only PyTorch on macOS (since CUDA isn't available on Apple platforms)

Pixi's platform-specific configuration features make this straightforward to implement.

## Solution Methods

### Method 1: Target-Specific Dependencies (Recommended)

Use Pixi's `[target.PLATFORM.dependencies]` syntax to specify different PyTorch variants per platform:

```toml
[project]
name = "your-project"
channels = ["conda-forge", "pytorch", "nvidia"]
platforms = ["linux-64", "win-64", "osx-64", "osx-arm64"]

[dependencies]
python = ">=3.9"
numpy = "*"

# CUDA PyTorch for Linux and Windows
[target.linux-64.dependencies]
pytorch = { version = ">=2.0", channel = "pytorch" }
pytorch-cuda = "12.1"
torchvision = { channel = "pytorch" }
torchaudio = { channel = "pytorch" }

[target.win-64.dependencies]
pytorch = { version = ">=2.0", channel = "pytorch" }
pytorch-cuda = "12.1"
torchvision = { channel = "pytorch" }
torchaudio = { channel = "pytorch" }

# CPU-only PyTorch for macOS
[target.osx-64.dependencies]
pytorch = { version = ">=2.0", channel = "pytorch" }
torchvision = { channel = "pytorch" }
torchaudio = { channel = "pytorch" }
cpuonly = { channel = "pytorch" }

[target.osx-arm64.dependencies]
pytorch = { version = ">=2.0", channel = "pytorch" }
torchvision = { channel = "pytorch" }
torchaudio = { channel = "pytorch" }
cpuonly = { channel = "pytorch" }
```

### Method 2: Features and Environments

Create separate environments for CPU and GPU configurations:

```toml
[project]
name = "your-project"
channels = ["conda-forge", "pytorch", "nvidia"]
platforms = ["linux-64", "win-64", "osx-64", "osx-arm64"]

[dependencies]
python = ">=3.9"
# Default to CPU-only PyTorch
pytorch = { version = ">=2.0", channel = "pytorch" }
torchvision = { channel = "pytorch" }
cpuonly = { channel = "pytorch" }

# GPU feature (only for Linux/Windows)
[feature.gpu]
platforms = ["linux-64", "win-64"]
system-requirements = { cuda = "12.1" }

[feature.gpu.dependencies]
pytorch = { version = ">=2.0", channel = "pytorch" }
pytorch-cuda = "12.1"
torchvision = { channel = "pytorch" }
torchaudio = { channel = "pytorch" }

[environments]
default = []
gpu = ["gpu"]
```

Usage:
- `pixi run` - Uses CPU-only PyTorch (works on all platforms)
- `pixi run -e gpu` - Uses GPU PyTorch (only on Linux/Windows)

### Method 3: PyPI with Platform-Specific Indexes

Use PyPI packages with CUDA-specific wheel indexes:

```toml
[project]
name = "your-project"
channels = ["conda-forge"]
platforms = ["linux-64", "win-64", "osx-64", "osx-arm64"]

[dependencies]
python = ">=3.9"

# CUDA PyTorch via PyPI
[target.linux-64.pypi-dependencies]
torch = { version = ">=2.0", index = "https://download.pytorch.org/whl/cu121" }
torchvision = { version = ">=0.15", index = "https://download.pytorch.org/whl/cu121" }

[target.win-64.pypi-dependencies]
torch = { version = ">=2.0", index = "https://download.pytorch.org/whl/cu121" }
torchvision = { version = ">=0.15", index = "https://download.pytorch.org/whl/cu121" }

# CPU-only PyTorch for macOS
[target.osx-64.pypi-dependencies]
torch = { version = ">=2.0", index = "https://download.pytorch.org/whl/cpu" }
torchvision = { version = ">=0.15", index = "https://download.pytorch.org/whl/cpu" }

[target.osx-arm64.pypi-dependencies]
torch = { version = ">=2.0", index = "https://download.pytorch.org/whl/cpu" }
torchvision = { version = ">=0.15", index = "https://download.pytorch.org/whl/cpu" }
```

## Key Configuration Elements

### Platform Identifiers
- `linux-64` - Linux x86_64
- `win-64` - Windows x86_64
- `osx-64` - macOS Intel (x86_64)
- `osx-arm64` - macOS Apple Silicon (ARM64)

### Required Channels
For conda-based installations, include these channels:
```toml
channels = ["conda-forge", "pytorch", "nvidia"]
```

### CUDA Version Specification
Specify CUDA version explicitly:
```toml
pytorch-cuda = "12.1"  # or "11.8", etc.
```

### CPU-Only Enforcement
Use the `cpuonly` package to ensure CPU-only installation:
```toml
cpuonly = { channel = "pytorch" }
```

## Common Issues and Solutions

### Cross-Platform Resolution Problems
If you encounter resolution issues when developing on macOS for Linux/Windows CUDA targets, use Method 2 (Features) to isolate platform-specific dependencies.

### CUDA Version Compatibility
Ensure your CUDA version matches your system:
- Check available versions: `pixi search pytorch-cuda`
- Common versions: `11.8`, `12.1`, `12.4`

### Mixed Package Sources
Avoid mixing conda and PyPI PyTorch packages in the same environment as they may conflict.

## Verification

Test your configuration works correctly:

```python
import torch
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU count: {torch.cuda.device_count()}")
```

Expected results:
- **Linux/Windows**: CUDA should be available
- **macOS**: CUDA should be unavailable (CPU-only)

## References

- [Pixi Multi-Platform Configuration](https://prefix-dev.github.io/pixi/dev/workspace/multi_platform_configuration/)
- [Pixi PyTorch Installation Guide](https://prefix-dev.github.io/pixi/dev/python/pytorch/)
- [PyTorch Installation Selector](https://pytorch.org/get-started/locally/)
- [Pixi Target Configuration](https://prefix-dev.github.io/pixi/dev/reference/configuration/#the-target-table)
- [Pixi Features and Environments](https://prefix-dev.github.io/pixi/dev/reference/configuration/#the-feature-and-environments-tables)
