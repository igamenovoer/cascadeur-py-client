# About SMPLX Python 3.13 Compatibility

## The Problem

SMPLX (Expressive Body Capture: 3D Hands, Face, and Body from a Single Image) currently fails to install on Python 3.13 due to a dependency conflict with the `dataclasses` backport package.

## Root Cause

The main issue preventing SMPLX from working with Python 3.13 is the inclusion of `dataclasses>=0.6` in its `requirements.txt` file:

```python
# requirements.txt
numpy>=1.16.2
torch>=1.0.1.post2
dataclasses>=0.6  # <-- This is the problem
```

### Why This Breaks

1. **dataclasses is built-in since Python 3.7**: The `dataclasses` module was added to Python's standard library in version 3.7
2. **The backport package is Python 3.6 only**: The `dataclasses` package on PyPI is specifically a backport for Python 3.6 and explicitly restricts installation to `>=3.6, <3.7`
3. **Installation fails on Python 3.13**: When trying to install SMPLX on Python 3.13, pip fails with an error like:
   ```
   ERROR: Package 'dataclasses' requires a different Python: 3.13.x not in '>=3.6, <3.7'
   ```

## Solution

### Quick Fix (For Users)

To use SMPLX with Python 3.13, you have several options:

#### Option 1: Install without dataclasses dependency
```bash
# Install other requirements first
pip install numpy>=1.16.2 torch>=1.0.1.post2

# Clone and modify the repository
git clone https://github.com/vchoutas/smplx
cd smplx

# Remove dataclasses from requirements.txt
# Then install
pip install -e .
```

#### Option 2: Create a modified requirements file
```bash
# Create a new requirements file without dataclasses
cat requirements.txt | grep -v dataclasses > requirements-py313.txt
pip install -r requirements-py313.txt
```

#### Option 3: Force install ignoring dependencies
```bash
pip install smplx --no-deps
pip install numpy torch  # Install actual dependencies manually
```

### Proper Fix (For Maintainers)

The SMPLX repository should update its dependencies to conditionally install the dataclasses backport:

#### Option 1: Update setup.py with environment markers
```python
# setup.py
install_requires=[
    'numpy>=1.16.2',
    'torch>=1.0.1.post2',
    'dataclasses>=0.6; python_version < "3.7"',  # Only for Python 3.6
]
```

#### Option 2: Use try/except for imports
```python
# In smplx/utils.py and other files
try:
    from dataclasses import dataclass, asdict, fields
except ImportError:
    # For Python 3.6 with backport installed
    from dataclasses import dataclass, asdict, fields
```

#### Option 3: Drop Python 3.6 support
Since Python 3.6 reached end-of-life in December 2021, the simplest solution would be to:
- Remove `dataclasses` from requirements
- Update `REQUIRES_PYTHON` in setup.py to `'>=3.7.0'`

## Verification

After fixing the dataclasses issue, verify SMPLX works correctly:

```python
import smplx
import torch

# Test basic model loading
model = smplx.create(
    model_path='path/to/models',
    model_type='smplx',
    gender='neutral',
    use_face_contour=False,
    num_betas=10,
    num_expression_coeffs=10,
    ext='npz'
)

# Test forward pass
output = model(
    betas=torch.zeros([1, 10]),
    body_pose=torch.zeros([1, 63]),
    global_orient=torch.zeros([1, 3])
)
print("Vertices shape:", output.vertices.shape)
```

## Other Considerations

While the dataclasses issue is the primary blocker, be aware that:

1. **PyTorch compatibility**: Ensure your PyTorch version supports Python 3.13
2. **NumPy compatibility**: Recent NumPy versions work fine with Python 3.13
3. **No other deprecated features**: The codebase doesn't use other removed Python features like `distutils` or `imp`

## References

- [SMPLX GitHub Repository](https://github.com/vchoutas/smplx)
- [dataclasses PyPI Package](https://pypi.org/project/dataclasses/)
- [Python 3.7 dataclasses Documentation](https://docs.python.org/3/library/dataclasses.html)
- [PyTorch Issue #46930](https://github.com/pytorch/pytorch/issues/46930) - Similar dataclasses compatibility discussion