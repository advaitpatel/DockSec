---
name: Bug Report
about: Report a bug to help us improve DockSec
title: '[BUG] '
labels: bug
assignees: ''

---

## Bug Description

A clear and concise description of what the bug is.

## To Reproduce

Steps to reproduce the behavior:

1. Run command: `docksec ...`
2. With Dockerfile containing: `...`
3. See error: `...`

## Expected Behavior

What you expected to happen.

## Actual Behavior

What actually happened instead.

## Environment

**DockSec Version:**
```bash
pip show docksec
```

**Operating System:**
- [ ] Windows
- [ ] macOS
- [ ] Linux (distribution: )

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

## Error Message / Logs

```
Paste error message or relevant logs here
```

## Configuration

```bash
# Contents of .env file (remove sensitive data)
LLM_MODEL=gpt-4o
TRIVY_SCAN_TIMEOUT=600
```

## Dockerfile (if relevant)

```dockerfile
# Your Dockerfile content here
```

## Possible Solution

If you have ideas on how to fix this, share them here.

## Checklist

- [ ] Searched existing issues to avoid duplicates
- [ ] Tested with the latest version of DockSec
- [ ] Included error messages and logs
- [ ] Removed any sensitive information (API keys, passwords, etc.)
