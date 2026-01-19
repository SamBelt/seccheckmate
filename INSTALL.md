# Installation Guide

## System Requirements

- **Python 3.7+** (3.10+ recommended)
- **OS**: macOS, Linux, or Windows
- **Disk Space**: ~50 MB
- **Internet**: Not required (fully offline)

## Installation Methods

### Method 1: Standard Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/seccheckmate.git
cd seccheckmate

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Verify installation
python seccheckmate.py
```

### Method 2: Minimal Installation

```bash
git clone https://github.com/yourusername/seccheckmate.git
cd seccheckmate
pip install PyYAML colorama
python seccheckmate.py
```

### Method 3: Development Installation

```bash
git clone https://github.com/yourusername/seccheckmate.git
cd seccheckmate

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install with development tools
pip install -r requirements.txt

# Make executable (macOS/Linux)
chmod +x seccheckmate.py
```

## Troubleshooting Installation

### Python Not Found
```bash
# Check Python installation
python3 --version

# If not installed, download from https://www.python.org/downloads/
# macOS: brew install python3
# Ubuntu/Debian: sudo apt-get install python3
# Windows: Download installer from python.org
```

### Module Not Found Errors

```bash
# Verify PyYAML installation
python -c "import yaml; print(yaml.__version__)"

# Reinstall dependencies
pip uninstall PyYAML colorama -y
pip install -r requirements.txt
```

### Permission Denied (macOS/Linux)

```bash
# Make script executable
chmod +x seccheckmate.py

# Run with explicit Python path
python3 seccheckmate.py
```

### Virtual Environment Issues

```bash
# Remove and recreate venv
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Platform-Specific Notes

### macOS

```bash
# Using Homebrew (recommended)
brew install python3

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install
pip install -r requirements.txt
```

### Linux (Ubuntu/Debian)

```bash
# Install Python
sudo apt update
sudo apt install python3 python3-venv python3-pip

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
# Create virtual environment
python -m venv venv
venv\Scripts\Activate.ps1

# Install
pip install -r requirements.txt

# Run
python seccheckmate.py
```

### Windows (Command Prompt)

```cmd
REM Create virtual environment
python -m venv venv
venv\Scripts\activate.bat

REM Install
pip install -r requirements.txt

REM Run
python seccheckmate.py
```

## Verification

```bash
# Test import
python -c "from seccheckmate import SecCheckmate; print('✅ Installation successful')"

# Check available assessments
python -c "from seccheckmate import SecCheckmate; app = SecCheckmate(); print(app.list_checklists())"

# Run application
python seccheckmate.py
# Press 5 to exit if it loads
```

## Uninstallation

```bash
# Deactivate virtual environment
deactivate

# Remove directory
rm -rf /path/to/seccheckmate
```

## Getting Help

If you encounter issues:

1. Check [Troubleshooting](#troubleshooting-installation) section above
2. Review [README.md](README.md#troubleshooting)
3. Check [FEATURES.md](FEATURES.md)
4. Open an issue: [GitHub Issues](https://github.com/yourusername/seccheckmate/issues)

## Next Steps

1. Read [QUICKSTART.md](QUICKSTART.md) for 5-minute setup
2. Review [FEATURES.md](FEATURES.md) for comprehensive feature overview
3. Check [README.md](README.md) for detailed documentation
4. Start your first assessment!

---

**Happy assessing! 🛡️**
