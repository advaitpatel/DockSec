[![GitHub Repo stars](https://img.shields.io/github/stars/glasskube/glasskube?style=flat)](https://github.com/advaitpatel/DockSec)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/advaitpatel/DockSec/blob/main/LICENSE)
[![Docs](https://img.shields.io/badge/docs-glasskube.dev%2Fdocs-blue)](https://github.com/advaitpatel/DockSec/blob/main/README.md)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/advaitpatel/DockSec/blob/main/CONTRIBUTING.md)
[![Downloads](https://img.shields.io/github/downloads/glasskube/glasskube/total)](https://github.com/advaitpatel/DockSec/releases)

<br>
<div align="center">
  <a href="https://github.com/advaitpatel/DockSec">
    <img src="#" alt="DockSec Logo" height="160">
  </a>
  <img referrerpolicy="no-referrer-when-downgrade" src="#" />

<h3 align="center">🧊 The next generation AI-Powered Docker Security Analyzer 📦</h3>

  <p align="center">
    <a href="#"><strong>Getting started »</strong></a>
    <br> <br>
    <a href="https://github.com/advaitpatel/DockSec" target="_blank">GitHub</a>
    .
    <a href="#" target="_blank">Docker Hub</a>
    .
    <a href="https://pypi.org/project/docksec/" target="_blank">PYPI Hub</a>
    .
    <a href="https://www.linkedin.com/in/advaitpatel93/" target="_blank">LinkedIn</a>
    . 
     <a href="https://x.com/AdvaitPatel93" target="_blank">Twitter / X</a>
  </p>
</div>
<hr>


## 🔐 What is DockSec?

DockSec is an **Open Source, AI-powered Docker Security Analyzer** that helps developers and DevSecOps teams detect, prioritize, and remediate security issues in Dockerfiles and container images.

It combines trusted static analysis tools like Trivy, Hadolint, and Docker Bench with a powerful AI engine (LangChain + LLM) to provide actionable security insights, remediation suggestions, and human-readable reports.

Unlike traditional scanners that overwhelm users with raw output, DockSec focuses on developer-first security — delivering context-aware recommendations, risk scoring, and clean reports in HTML, PDF, or JSON formats. It seamlessly integrates into CI/CD pipelines or can be run locally via a simple CLI.


## 🎯 Architecture Diagram

COMING SOON


## ❓Why DockSec?

Most Docker security tools do one thing well — scan. But they often fall short where it matters most: prioritizing what’s important, explaining why it matters, and guiding you toward a fix.

Here’s why DockSec is different:

✅ **Smart + Actionable**: Combines traditional scanners with AI-driven remediation suggestions using LangChain + LLM.

🚀 **Developer-First**: Clear, prioritized output. Designed to work in CI/CD, pre-commit hooks, and developer environments.

📊 **Security Score & Reports**: Assigns a score to your Dockerfile/image and generates human-readable reports (HTML, PDF, JSON).

🔧 **Flexible CLI**: Run full scans, AI-only analysis, or scan-only modes with simple commands.

🧠 **Shift Left, Intelligently**: Helps developers fix security issues early — without friction or false positives.


## 🗄️ Table Of Contents

- [Features](https://github.com/glasskube/#-features)
- [Quick Start](https://github.com/glasskube/#-quick-start)
- [How to install your first package](https://github.com/glasskube/glasskube#-how-to-install-you-first-package)
- [Supported Packages](https://github.com/glasskube/glasskube#-supported-packages)
- [Architecture Diagram](https://github.com/glasskube/glasskube#architecture-diagram)
- [Need help?](https://github.com/glasskube/glasskube#-need-help)
- [Related projects](https://github.com/glasskube/glasskube#-related-projects)
- [How to Contribute](https://github.com/glasskube/glasskube#-how-to-contribute)
- [Supported by](https://github.com/glasskube/glasskube#-thanks-to-all-our-contributors)
- [Activity](https://github.com/glasskube/glasskube#-activity)
- [License](https://github.com/glasskube/glasskube#-license)

## 🚀 How To Install DockSec

You can install DockSec via [PyPI](https://pypi.org/project/docksec/)

```bash
pip install docksec
```

OR You can install DockSec using Python virtual environment

```bash
python -m venv env

# On Windows
env\Scripts\activate

# On macOS/Linux
source env/bin/activate

pip install -e .
```
This will install the docksec using `setup.py` from local files.

To completely use the AI scanning of DockSec, you have to setup the `OPENAI-API-KEY`

  - 🔹 PowerShell (Windows): $env:OPENAI_API_KEY = "your-secret-key"

  - 🔹 Command Prompt (CMD on Windows): set OPENAI_API_KEY=your-secret-key

  - 🔹 Bash/Zsh (Linux/macOS): export OPENAI_API_KEY="your-secret-key"

  - 🔹 Or create a .env file with: OPENAI_API_KEY=your-secret-key

Congratulations, you can now explore and install all our available packages! 🎉


## 🎬 DockSec Demo Video

[![DockSec Demo Video - Coming Soon](#)](#)


## 📦 Required Packages

The following dependencies will be automatically installed:

  - `langchain`
  - `langchain-openai`
  - `python-dotenv`
  - `pandas`
  - `tqdm`
  - `colorama`
  - `rich`
  - `fpdf`
  - `setuptools`


## 📝 How To Use DockSec using CLI

After installation, you can use DockSec with a simple command:

```bash
docksec path\to\Dockerfile
```

### Options:
  - `-i, --image`: Specify Docker image ID for scanning (optional)
  - `-o, --output`: Specify output file for the report (default: security_report.txt)
  - `--ai-only`: Run only AI-based recommendations
  - `--scan-only`: Run only Dockerfile/image scanning

### Examples:

```bash
# Basic analysis
docksec path\to\Dockerfile

# Analyze both Dockerfile and a specific image
docksec path\to\Dockerfile -i myimage:latest

# Only run AI recommendations
docksec path\to\Dockerfile --ai-only

# Only scan for vulnerabilities with custom output file
docksec path\to\Dockerfile --scan-only -o custom_report.txt
```

### Legacy Usage

You can still use the original commands:

```bash
# For AI-based recommendations
python .\main.py "path\to\your\dockerfile"

# For scanning both Dockerfile and images
python docker_scanner.py <dockerfile_path> <image_name> [severity]
# Example: python docker_scanner.py .\Dockerfile myapp:latest CRITICAL,HIGH
```

### External Tools Setup

To check the Dockerfile as well as images for vulnerabilities, you need to setup `Trivy` and `hadolint`:

```bash
python .\setup_external_tools.py
```

For manual installation, refer to [Trivy] (https://trivy.dev/v0.18.3/installation/) and [hadolint] (https://github.com/hadolint/hadolint?tab=readme-ov-file#install) documentation.


## ☝️ Need Help or Want to Provide Feedback?

If you encounter any problems, we will be happy to support you wherever we can.
For bugs, issues or feature requests feel free to [open an issue](https://github.com/advaitpatel/DockSec/issues/new).
We are happy to assist you with anything related to the project.


## 🤝 How to Contribute to DockSec

Your feedback is invaluable to us as we continue to improve DockSec. If you'd like to contribute, consider trying out the beta version, reporting any issues, and sharing your suggestions. See [the contributing guide](CONTRIBUTING.md) for detailed instructions on how you can contribute.


## 👾 Activity

![Glasskube Activity](https://repobeats.axiom.co/api/embed/c5aac6f5d22bd6b83a21ae51353dd7bcb43f9517.svg "Glasskube activity image")

## 📘 License

The DockSec is licensed under the MIT license. For more information check the [LICENSE](https://github.com/advaitpatel/DockSec/blob/main/LICENSE) file for details.
