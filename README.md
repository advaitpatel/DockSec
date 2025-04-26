# DockSec - AI-Powered Docker Security Analyzer

## Overview
DockSec is an open-source AI-powered tool designed to analyze Dockerfiles for security vulnerabilities, misconfigurations, and inefficiencies. It provides automated recommendations to enhance container security, reduce the attack surface, and improve compliance with industry best practices.

## Features
- AI/ML-Powered Analysis: Uses AI models to detect vulnerabilities and suggest security improvements.
- Security Vulnerability Detection: Scans Dockerfiles for known security issues, CVEs, and misconfigurations.
- Best Practice Recommendations: Provides actionable insights to enhance security, minimize image size, and improve efficiency.
- Integration with Development Tools:
  - VS Code extension for inline security suggestions.
  - CI/CD pipeline support (GitHub Actions, GitLab CI, Jenkins).
- Compliance Checks: Aligns with CIS Benchmarks, Docker Security Best Practices, and OWASP guidelines.


## Installation

Create a virtual environment
```bash
python -m venv env
```
Activate the environment
```bash
env\Scripts\activate # for mac use "source env\bin\activate"
```

Install the tool using pip:

```bash
pip install -e .
```

This will install the `docksec` using setup.py from local files.

To install Docksec using pypi you can simply run 

```bash
pip install docksec # it will load the docksec tool from pypi
```

To completely use the AI scanning of docksec you have to setup the OPENAI-API-KEY 

🔹 PowerShell (Windows):
    `$env:OPENAI_API_KEY = "your-secret-key"`

🔹 Command Prompt (CMD on Windows):
    `set OPENAI_API_KEY=your-secret-key`

🔹 Bash/Zsh (Linux/macOS):
    `export OPENAI_API_KEY="your-secret-key"`

🔹 Or create a `.env` file with:
    `OPENAI_API_KEY=your-secret-key`

## Requirements

The following dependencies will be automatically installed:
- langchain
- langchain-openai
- python-dotenv
- pandas
- tqdm
- colorama
- rich
- fpdf
- setuptools

## Usage

### CLI Tool

After installation, you can use DockSec with a simple command:

```bash
docksec path\to\Dockerfile
```

#### Options:
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

#### External Tools Setup

To check the Dockerfile as well as images for vulnerabilities, you need to setup Trivy and hadolint:

```bash
python .\setup_external_tools.py
```

For manual installation, refer to [Trivy](https://trivy.dev/v0.18.3/installation/) and [hadolint](https://github.com/hadolint/hadolint?tab=readme-ov-file#install) documentation.

## CI/CD Integration
TBD

## Roadmap
TBD

## Contributing
We welcome contributions! To get started:
1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Get Involved
- ⭐ Star this repository to show support!
- 📢 Share your feedback via GitHub Issues.
- 📝 Write about DockSec and contribute to our documentation.

## Contact
For questions or collaborations, reach out via:
- GitHub Discussions: DockSec Community
- Twitter: @yourhandle
- LinkedIn: Your Profile