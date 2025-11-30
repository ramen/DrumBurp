# Building DrumBurp with uv (Modern Python 3 Build)

This document describes how to build DrumBurp using the modern `uv` package manager, with Python 3 and PyQt5 support.

## Prerequisites

### Required Software

- **Python 3.8 or later** (Python 3.9+ recommended)
- **uv** package manager
- **Git** (for cloning the repository)

### Installing uv

#### Quick Install (Linux/macOS)
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Alternative Install (using pip)
```bash
pip install uv
```

#### Verify Installation
```bash
uv --version
```

## Building DrumBurp

### Quick Start

The simplest way to build and run DrumBurp:

```bash
# 1. Clone the repository (if you haven't already)
git clone https://github.com/Whatang/DrumBurp.git
cd DrumBurp

# 2. Run the build script
chmod +x build/build_with_uv.sh
./build/build_with_uv.sh

# 3. Activate the virtual environment and run
source .venv/bin/activate
python src/DrumBurp.py
```

### Manual Build Steps

If you prefer to build manually:

```bash
# 1. Create a virtual environment
uv venv

# 2. Activate the virtual environment
source .venv/bin/activate

# 3. Install dependencies
uv pip install -e ".[dev]"

# 4. Run DrumBurp
python src/DrumBurp.py
```

## Building a Standalone Executable

To create a distributable executable that doesn't require Python to be installed:

```bash
# 1. Ensure you're in the virtual environment
source .venv/bin/activate

# 2. Run the executable build script
chmod +x build/build_executable.sh
./build/build_executable.sh

# 3. The executable will be in dist/DrumBurp/
./dist/DrumBurp/DrumBurp
```

### Creating a Distribution Archive

```bash
cd dist
tar czf DrumBurp-Linux-x86_64.tar.gz DrumBurp/
```

Users can then extract and run:
```bash
tar xzf DrumBurp-Linux-x86_64.tar.gz
./DrumBurp/DrumBurp
```

## Development

### Installing Development Dependencies

Development dependencies include tools like pylint, autopep8, and pre-commit:

```bash
source .venv/bin/activate
uv pip install -e ".[dev]"
```

### Running Tests

The tests use Python's built-in `unittest` framework (not pytest):

```bash
source .venv/bin/activate
PYTHONPATH=src python -m unittest discover -s src/test -p "test*.py"
```

For verbose output:
```bash
PYTHONPATH=src python -m unittest discover -s src/test -p "test*.py" -v
```

Alternatively, run from the src directory:
```bash
cd src
python -m unittest discover -s test -p "test*.py"
```

### Code Quality

```bash
# Run pylint
pylint src/

# Auto-format code
autopep8 --in-place --recursive src/
```

## Migration from Python 2 to Python 3

This fork includes automated migration from Python 2 to Python 3 and PyQt4 to PyQt5. The migration scripts are in the `build/` directory:

- `build/migrate_py3_qt5.py` - Main migration script (already run)
- `build/fix_qtgui_qtwidgets.py` - Fixes QtGui/QtWidgets split (already run)

These scripts have already been executed on the codebase. If you need to re-run them or apply them to modifications:

```bash
python3 build/migrate_py3_qt5.py
python3 build/fix_qtgui_qtwidgets.py
```

## What Changed from Original DrumBurp

### Python Changes
- **Python 2 → Python 3**
  - `print` statements → `print()` functions
  - `unicode()` → `str()`
  - `except Exception, e:` → `except Exception as e:`
  - `xrange()` → `range()`
  - `.iteritems()` → `.items()`
  - `StandardError` → `Exception`

### PyQt Changes
- **PyQt4 → PyQt5**
  - `from PyQt4 import ...` → `from PyQt5 import ...`
  - Many classes moved from `QtGui` to `QtWidgets`
  - `QVariant` removed (no longer needed)
  - `pyqtSignature` decorator removed (deprecated)
  - `.toString()` calls removed (automatic conversion)

### Build System Changes
- **pip → uv**
  - Faster dependency resolution
  - Better dependency isolation
  - Reproducible builds
- **setup.py → pyproject.toml**
  - Modern Python packaging standard
  - Better metadata definition
  - Cleaner dependency management

## System Dependencies

### Debian/Ubuntu
```bash
sudo apt-get install python3 python3-venv python3-pip
sudo apt-get install libxcb-xinerama0  # For PyQt5
```

### Fedora/RHEL
```bash
sudo dnf install python3 python3-pip
sudo dnf install qt5-qtbase  # For PyQt5
```

### Arch Linux
```bash
sudo pacman -S python python-pip
sudo pacman -S qt5-base  # For PyQt5
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'PyQt5'"

Make sure you've activated the virtual environment:
```bash
source .venv/bin/activate
uv pip install PyQt5
```

### "ImportError: libQt5Core.so.5: cannot open shared object file"

Install Qt5 system libraries:
```bash
# Debian/Ubuntu
sudo apt-get install libqt5core5a libqt5gui5 libqt5widgets5

# Fedora
sudo dnf install qt5-qtbase
```

### "Permission denied" when running scripts

Make scripts executable:
```bash
chmod +x build/build_with_uv.sh
chmod +x build/build_executable.sh
```

### Application crashes on startup

Check the console output for errors. Common issues:
- Missing system libraries (install Qt5 dependencies)
- Python version too old (requires Python 3.8+)
- Corrupted virtual environment (delete `.venv/` and rebuild)

## Contributing

When contributing to this Python 3 fork:

1. Ensure all code is Python 3.8+ compatible
2. Use PyQt5 (not PyQt4)
3. Test with `uv` build system
4. Run tests before submitting
5. Follow existing code style

## License

DrumBurp is licensed under the GNU General Public License v3.0 or later (GPL-3.0-or-later).

See COPYING.txt for details.

## Support

- Original Project: https://whatang.org/drumburp
- Original Repository: https://github.com/Whatang/DrumBurp
- Python 3 Fork Issues: [Your fork's issue tracker]

## Credits

- Original Author: Michael Thomas (Whatang)
- Python 3 Migration: [Your name/contribution]
