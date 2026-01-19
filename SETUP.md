# Setup and Installation Guide

## System Requirements

- **OS**: macOS, Linux, or Windows
- **Python**: 3.7 or higher
- **Disk Space**: ~50 MB

## Installation Steps

### 1. Clone the Repository

```bash
# SSH (if you have SSH key configured)
git clone git@github.com:yourusername/seccheckmate.git

# HTTPS
git clone https://github.com/yourusername/seccheckmate.git

cd seccheckmate
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
python seccheckmate.py
```

You should see the main menu. If successful, press `3` to exit.

## Configuration

### Basic Configuration

Edit `config/settings.yaml` to customize:

```yaml
organization:
  name: "Your Organization Name"
  project: "Your Project Name"
```

### Running Your First Assessment

```bash
# Start the application
python seccheckmate.py

# Select option 1 (Run a security checklist)
# Choose a checklist (e.g., web)
# Answer questions (PASS/FAIL/NA) and add notes
# Report will be generated in reports/ directory
```

## Troubleshooting

### Issue: Python not found
```bash
# Check Python version
python3 --version

# If not installed, download from https://www.python.org/downloads/
```

### Issue: pip: command not found
```bash
# Try using python -m pip
python -m pip install -r requirements.txt
```

### Issue: Permission denied on macOS/Linux
```bash
# Make script executable
chmod +x seccheckmate.py

# Run with explicit Python
python3 seccheckmate.py
```

### Issue: Module 'yaml' not found
```bash
# Reinstall dependencies
pip uninstall PyYAML
pip install -r requirements.txt
```

## Using SecCheckmate

### Interactive Mode (Default)

```bash
python seccheckmate.py
```

Follow the on-screen prompts to:
1. Select a checklist
2. Answer assessment questions
3. Provide evidence/notes
4. Generate reports

### Viewing Reports

Reports are generated in the `reports/` directory with timestamp:

```bash
# View reports (macOS/Linux)
ls reports/

# View specific report
cat reports/report_20260119_120530.md

# Open in default editor (macOS)
open reports/report_20260119_120530.md
```

## File Structure Reference

```
seccheckmate/
├── seccheckmate.py          # Main application
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── CONTRIBUTING.md          # Contribution guidelines
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT License
├── SETUP.md                 # This file
├── config/
│   └── settings.yaml        # Configuration file
├── checklists/              # Assessment templates
│   ├── web.yaml
│   ├── cloud_aws.yaml
│   ├── wifi.yaml
│   ├── firmware.yaml
│   └── llm.yaml
├── reports/                 # Generated assessment reports
├── templates/
│   └── report_template.md
└── screenshots/             # Documentation images
```

## Adding Custom Checklists

1. Create a new file: `checklists/mycheck.yaml`
2. Follow the format:

```yaml
category: My Security Category
description: Description of assessment
version: 1.0

tests:
  - id: MYCHECK-01
    title: Test Title
    description: What this test checks
    severity: High  # Critical, High, Medium, Low, Info
    category: Test Category
```

3. Run the application and select your checklist

## Tips for Success

### Best Practices:
- ✅ Customize checklists for your specific context
- ✅ Store reports in version control for history
- ✅ Share standardized checklists with your team
- ✅ Use consistent evidence notes for better tracking
- ✅ Review failed items and create remediation plans

### Security:
- ✅ Keep reports in a secure location
- ✅ Don't commit sensitive reports to public repos
- ✅ Consider encrypting reports containing sensitive data
- ✅ Limit access to assessment tool and results

## Getting Help

1. Check [README.md](README.md) for features and examples
2. Review [CONTRIBUTING.md](CONTRIBUTING.md) for development setup
3. Create an [issue](https://github.com/yourusername/seccheckmate/issues) on GitHub
4. Check existing issues for similar problems

## Next Steps

1. Read the [README](README.md) for detailed feature overview
2. Try each checklist to understand the assessment types
3. Customize checklists for your organization
4. Share with your security team
5. Contribute improvements back to the project!

---

**Happy assessing! 🛡️**
