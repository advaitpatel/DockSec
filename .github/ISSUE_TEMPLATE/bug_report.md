---
name: Bug Report
about: Report a bug to help us improve DockSec
title: '[BUG] '
labels: bug
assignees: ''

---

## 🐛 Bug Description

A clear and concise description of what the bug is.

## 📋 To Reproduce

Steps to reproduce the behavior:

1. Run command: `docksec ...`
2. With Dockerfile containing: '...'
3. See error: '...'

## ✅ Expected Behavior

A clear and concise description of what you expected to happen.

## ❌ Actual Behavior

What actually happened instead.

## 📊 Environment

**DockSec Version:**
```bash
pip show docksec
```

**Operating System:**
- [ ] Windows
- [ ] macOS
- [ ] Linux (which distribution?)

**Python Version:**
```bash
python --version
```

**Docker Version:**
```bash
docker --version
```

**External Tools (if applicable):**
```bash
trivy --version
hadolint --version
```

## 📝 Additional Context

### Error Message/Logs

```
Paste error message or relevant logs here
```

### Configuration

```bash
# Contents of .env file (remove sensitive data)
LLM_MODEL=gpt-4o
TRIVY_SCAN_TIMEOUT=600
# ... etc
```

### Dockerfile (if relevant)

```dockerfile
# Your Dockerfile content here (if it helps reproduce the issue)
```

## 🔍 Possible Solution

If you have ideas on how to fix this, please share them here.

## ✔️ Checklist

- [ ] I have searched existing issues to avoid duplicates
- [ ] I have provided all the required information above
- [ ] I have tested with the latest version of DockSec
- [ ] I have included error messages and logs
- [ ] I have removed any sensitive information (API keys, passwords, etc.)

## 📸 Screenshots

If applicable, add screenshots to help explain your problem.

---

**Thank you for taking the time to report this bug! We'll look into it as soon as possible.**
