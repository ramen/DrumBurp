# DrumBurp Python 3 - Quick Reference

## 🚀 Common Commands

### Build & Run
```bash
# First time setup
./build/build_with_uv.sh
source .venv/bin/activate
python src/DrumBurp.py

# Subsequent runs (after activating venv)
python src/DrumBurp.py
python src/DrumBurp.py path/to/score.brp
```

### Build Executable
```bash
source .venv/bin/activate
./build/build_executable.sh
./dist/DrumBurp/DrumBurp
```

### Development
```bash
# Activate environment
source .venv/bin/activate

# Install dev dependencies
uv pip install -e ".[dev]"

# Run tests
python -m pytest src/test/

# Lint code
pylint src/

# Format code
autopep8 --in-place --recursive src/
```

### Clean Build
```bash
# Remove virtual environment
rm -rf .venv/

# Remove build artifacts
rm -rf dist/ build/DrumBurp.spec

# Rebuild everything
./build/build_with_uv.sh
```

## 📂 Important Files

| File | Purpose |
|------|---------|
| `README_PYTHON3.md` | Quick start guide - **READ THIS FIRST** |
| `BUILD_UV.md` | Detailed build documentation |
| `MIGRATION_CHECKLIST.md` | What was changed |
| `SUMMARY.md` | Executive summary |
| `pyproject.toml` | Project configuration |
| `build/build_with_uv.sh` | Main build script |
| `build/build_executable.sh` | Standalone build |

## 🔧 Troubleshooting

### Application won't start
```bash
# Check Python version (need 3.8+)
python --version

# Reinstall dependencies
rm -rf .venv/
./build/build_with_uv.sh
```

### Missing Qt libraries
```bash
# Debian/Ubuntu
sudo apt-get install libqt5widgets5

# Fedora/RHEL
sudo dnf install qt5-qtbase

# Arch Linux
sudo pacman -S qt5-base
```

### Import errors
```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Verify PyQt5 is installed
python -c "import PyQt5; print(PyQt5.__file__)"
```

## 📦 Dependencies

### Runtime
- Python 3.8+
- PyQt5 5.15+
- pygame 2.0+

### Development
- pylint 2.0+
- autopep8 1.5+
- pre-commit 2.0+

### Build
- pyinstaller 5.0+

## 🎯 Key Differences from Python 2 Version

| Python 2 | Python 3 |
|----------|----------|
| `print "text"` | `print("text")` |
| `unicode(x)` | `str(x)` |
| `except E, e:` | `except E as e:` |
| `xrange()` | `range()` |
| `.iteritems()` | `.items()` |
| PyQt4 | PyQt5 |
| pip | uv |

## 📝 Git Workflow

### Creating a Fork
```bash
# Fork on GitHub, then clone
git clone https://github.com/YOUR_USERNAME/DrumBurp.git
cd DrumBurp

# Add upstream remote
git remote add upstream https://github.com/Whatang/DrumBurp.git
```

### Committing Changes
```bash
# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Python 3 migration complete"

# Push to your fork
git push origin python3-migration
```

### Creating a Release
```bash
# Tag the release
git tag -a v1.4.0-py3 -m "Python 3 release"

# Push the tag
git push origin v1.4.0-py3

# GitHub Actions will build automatically
```

## 🧪 Testing Checklist

- [ ] Application launches
- [ ] Can create new score
- [ ] Can open existing .brp file
- [ ] Can edit drums in score
- [ ] Can add/remove measures
- [ ] Can save score
- [ ] Can export to ASCII
- [ ] Can export to Lilypond
- [ ] Can export to PDF
- [ ] MIDI playback works
- [ ] All menus functional
- [ ] All toolbars functional
- [ ] Undo/redo works
- [ ] Copy/paste works

## 📊 Build Statistics

- **Build time (first)**: ~5 minutes
- **Build time (subsequent)**: ~30 seconds
- **Executable size**: ~50-80 MB
- **Dependencies**: 27 packages
- **Python files**: 115
- **Modified files**: 95

## 🔗 Useful Links

- **Original Project**: https://whatang.org/drumburp
- **Original Repo**: https://github.com/Whatang/DrumBurp
- **uv Documentation**: https://github.com/astral-sh/uv
- **PyQt5 Docs**: https://www.riverbankcomputing.com/static/Docs/PyQt5/
- **Python 3 Migration Guide**: https://docs.python.org/3/howto/pyporting.html

## 💡 Tips

1. **Always activate the virtual environment** before running Python commands
2. **Use `uv pip` instead of `pip`** for faster installs
3. **Check BUILD_UV.md** for detailed troubleshooting
4. **Test on a clean system** before releasing
5. **Keep backups** of your .brp files before testing

## 🆘 Getting Help

1. Check BUILD_UV.md troubleshooting section
2. Review error messages in terminal
3. Verify Python version: `python --version`
4. Check uv version: `uv --version`
5. Verify Qt libraries: `python -c "import PyQt5"`

## 📧 Support

For issues with:
- **Original DrumBurp**: https://github.com/Whatang/DrumBurp/issues
- **Python 3 Migration**: [Your fork's issue tracker]
- **Build System**: Check BUILD_UV.md first

---

**Version**: 1.3.2 (Python 3 fork)
**Last Updated**: 2025-11-29
**License**: GNU GPL v3.0+
