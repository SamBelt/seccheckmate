# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install
```bash
git clone https://github.com/yourusername/seccheckmate.git
cd seccheckmate
pip install -r requirements.txt
```

### Step 2: Run
```bash
python seccheckmate.py
```

### Step 3: Select a Checklist
Choose from:
- Web Application Security
- AWS Cloud Security
- WiFi Security
- Firmware Security
- LLM/AI Security

### Step 4: Answer Questions
For each test:
- Read the description
- Enter PASS, FAIL, or NA
- Add evidence/notes

### Step 5: View Report
Your report is in `reports/report_*.md`

## Available Checklists

| Name | Tests | Focus |
|------|-------|-------|
| Web | 35 | OWASP, APIs, Auth |
| AWS | 40 | Cloud, IAM, Services |
| WiFi | 38 | Networks, Encryption |
| Firmware | 44 | Embedded, Boot, Debug |
| LLM | 44 | AI, Prompts, Data |

## Example Report

```markdown
# Security Assessment Report

**Category:** Web Application Security
**Pass Rate:** 87.5%

## Summary
- ✅ Passed: 35 tests
- ❌ Failed: 3 tests
- ⏭️ N/A: 2 tests

## Critical Issues
- [WEB-07] Privilege Escalation vulnerability found
```

## Configuration

Edit `config/settings.yaml`:
```yaml
organization:
  name: "Your Organization"
```

## Troubleshooting

**ModuleNotFoundError: No module named 'yaml'**
```bash
pip install PyYAML
```

**Checklist not found**
- Check `checklists/` directory
- Verify `.yaml` file extension

## Need Help?

📚 [Full Documentation](README.md)  
🐛 [Report Issues](https://github.com/yourusername/seccheckmate/issues)  
🤝 [Contributing](CONTRIBUTING.md)

---

Happy assessing! 🛡️
