# DrumBurp - Python 3 & uv Fork

This is a modernized fork of [DrumBurp](https://whatang.org/drumburp) - a drum tablature editor - updated to work with Python 3 and the modern `uv` package manager.

## Quick Start

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Build and run DrumBurp
./build/build_with_uv.sh
source .venv/bin/activate
python src/DrumBurp.py
```

That's it! DrumBurp should now be running.

## What's New in This Fork

### ✨ Modernization
- **Python 3.8+** support (was Python 2)
- **PyQt5** instead of PyQt4
- **uv** package manager for faster, more reliable builds
- **pyproject.toml** modern packaging configuration

### 🔧 Technical Changes
- Automated Python 2 → 3 conversion
- All `print` statements converted to functions
- `unicode()` → `str()`
- Exception syntax updated
- QtGui/QtWidgets split properly handled
- Removed deprecated PyQt constructs

### 📦 Build System
- Fast dependency resolution with `uv`
- Reproducible builds
- Simple build scripts
- No need to manually compile Qt from source

## System Requirements

- **Python 3.8 or later**
- **Linux** (this fork focuses on Linux compatibility)
- **Qt5 libraries** (installed automatically via PyQt5)

### Installing System Dependencies

#### Debian/Ubuntu
```bash
sudo apt-get install python3 python3-venv
sudo apt-get install libxcb-xinerama0  # For PyQt5 display support
```

#### Fedora/RHEL
```bash
sudo dnf install python3
sudo dnf install qt5-qtbase
```

#### Arch Linux
```bash
sudo pacman -S python
sudo pacman -S qt5-base
```

## Building from Source

### Option 1: Automated Build (Recommended)

```bash
./build/build_with_uv.sh
source .venv/bin/activate
python src/DrumBurp.py
```

### Option 2: Manual Build

```bash
# 1. Create virtual environment
uv venv

# 2. Activate it
source .venv/bin/activate

# 3. Install dependencies
uv pip install -e ".[dev]"

# 4. Run DrumBurp
python src/DrumBurp.py
```

### Building a Standalone Executable

To create a distributable executable:

```bash
source .venv/bin/activate
./build/build_executable.sh

# Executable will be in dist/DrumBurp/
./dist/DrumBurp/DrumBurp
```

## Documentation

- **[BUILD_UV.md](BUILD_UV.md)** - Comprehensive build instructions
- **[BUILDING.md](BUILDING.md)** - Original build documentation
- **[README.md](README.md)** - Original project README

## Migration Scripts

The following migration scripts were used to convert the codebase:

- `build/migrate_py3_qt5.py` - Python 2 → 3 and PyQt4 → PyQt5
- `build/fix_qtgui_qtwidgets.py` - Fixes QtGui/QtWidgets class splits

These have already been applied. They're included in case you need to re-run them or apply them to modifications.

## What Changed

### Python Changes
✅ `print` statements → `print()` functions
✅ `unicode()` → `str()`
✅ `except Exception, e:` → `except Exception as e:`
✅ `xrange()` → `range()`
✅ `.iteritems()` → `.items()`
✅ `StandardError` → `Exception`

### PyQt Changes
✅ `PyQt4` → `PyQt5`
✅ `QtGui` classes split into `QtWidgets` and `QtGui`
✅ `QVariant` removed (automatic conversion in PyQt5)
✅ `pyqtSignature` decorator removed (deprecated)
✅ `.toString()` calls removed (automatic in PyQt5)

### Build System
✅ Modern `pyproject.toml` configuration
✅ Fast dependency management with `uv`
✅ Automated build scripts
✅ PyInstaller integration for standalone builds

## Known Issues

None currently! If you find any issues, please report them in the issue tracker.

## Contributing

Contributions are welcome! When contributing:

1. Ensure code is Python 3.8+ compatible
2. Use PyQt5 APIs
3. Test with the `uv` build system
4. Run tests before submitting PRs
5. Follow existing code style

## License

GNU General Public License v3.0 or later (GPL-3.0-or-later)

See [COPYING.txt](COPYING.txt) for details.

## Credits

- **Original Author**: Michael Thomas (Whatang) - https://whatang.org
- **Original Project**: https://github.com/Whatang/DrumBurp
- **Python 3 Migration**: This fork

## Support

- **Original Project**: https://whatang.org/drumburp
- **Original Repository**: https://github.com/Whatang/DrumBurp
- **This Fork**: [Your repository URL here]

## Acknowledgments

Special thanks to Michael Thomas for creating DrumBurp and releasing it under an open-source license, making this modernization possible.

---

**Note**: This is an unofficial fork focused on Python 3 compatibility and modern build tooling. The original project remains at https://github.com/Whatang/DrumBurp.
