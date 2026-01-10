[![GitHub Repo stars](https://img.shields.io/github/stars/advaitpatel/DockSec?style=flat)](https://github.com/advaitpatel/DockSec)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/docksec.svg)](https://badge.fury.io/py/docksec)
[![Python Version](https://img.shields.io/pypi/pyversions/docksec.svg)](https://pypi.org/project/docksec/)
[![CI Status](https://github.com/advaitpatel/DockSec/actions/workflows/python-app.yml/badge.svg)](https://github.com/advaitpatel/DockSec/actions)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/advaitpatel/DockSec/blob/main/CONTRIBUTING.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<br>
<div align="center">
  <!-- <a href="https://github.com/advaitpatel/DockSec">
    <img src="https://github.com/advaitpatel/DockSec/blob/main/images/docksec-logo-II.png" alt="DockSec Logo" height="160">
  </a> -->
  <img referrerpolicy="no-referrer-when-downgrade" src="https://github.com/advaitpatel/DockSec/blob/main/images/docksec-logo-II.png" />

<h3 align="center">🧊 The next generation AI-Powered Docker Security Analyzer 📦</h3>

  <p align="center">
    <a href="https://github.com/advaitpatel/DockSec" target="_blank">GitHub</a>
    🔹
    <a href="https://pypi.org/project/docksec/" target="_blank">PyPI</a>
    🔹
    <a href="#quick-start" target="_blank">Quick Start</a>
    🔹
    <a href="https://www.linkedin.com/in/advaitpatel93/" target="_blank">LinkedIn</a>
    🔹
     <a href="https://x.com/AdvaitPatel93" target="_blank">Twitter / X</a>
  </p>
</div>
<hr>


## 🚀 Quick Start

Get started with DockSec in 3 simple steps:

```bash
# 1. Install DockSec
pip install docksec

# 2. Set your OpenAI API key (optional, for AI features)
export OPENAI_API_KEY="your-api-key"

# 3. Scan your Dockerfile
docksec path/to/Dockerfile
```

That's it! DockSec will analyze your Dockerfile and provide actionable security recommendations. 🎉

> **Note**: Scan-only mode works without an API key: `docksec path/to/Dockerfile --scan-only`


## 🔐 What is DockSec?

DockSec is an **Open Source, AI-powered Docker Security Analyzer** that helps developers and DevSecOps teams detect, prioritize, and remediate security issues in Dockerfiles and container images.

It combines trusted static analysis tools like Trivy, Hadolint, and Docker Scout with a powerful AI engine (LangChain + OpenAI GPT-4) to provide actionable security insights, remediation suggestions, and human-readable reports.

Unlike traditional scanners that overwhelm users with raw output, DockSec focuses on developer-first security — delivering context-aware recommendations, automated security scoring, and professional reports in HTML, PDF, JSON, and CSV formats. It seamlessly integrates into CI/CD pipelines or can be run locally via a simple CLI with built-in retry logic and rate limiting for reliability.


## ❓Why DockSec?

Most Docker security tools do one thing well — scan. But they often fall short where it matters most: prioritizing what’s important, explaining why it matters, and guiding you toward a fix.

Here’s why DockSec is different:

✅ **Smart + Actionable**: Combines traditional scanners with AI-driven remediation suggestions using LangChain + OpenAI GPT-4.

🚀 **Developer-First**: Clear, prioritized output with progress indicators. Designed to work in CI/CD, pre-commit hooks, and developer environments.

📊 **Security Score & Reports**: Automatically calculates security scores (0-100) and generates professional reports in multiple formats (HTML, PDF, JSON, CSV).

🔧 **Flexible CLI**: Run full scans, AI-only analysis, scan-only modes, or image-only scanning with simple commands.

🧠 **Shift Left, Intelligently**: Helps developers fix security issues early with actionable error messages and troubleshooting guidance.

🔄 **Production-Ready**: Built-in retry logic with exponential backoff, rate limiting handling, and robust error recovery.

⚡ **Performance**: Real-time progress indicators, optimized scanning, and configurable timeouts for long-running operations.


## 🌟 Key Features

### Security Scanning
- **Multi-Tool Integration**: Leverages Trivy, Hadolint, and Docker Scout for comprehensive vulnerability detection
- **Severity-Based Filtering**: Automatically prioritizes CRITICAL and HIGH vulnerabilities
- **CVE Detection**: Identifies known vulnerabilities with detailed CVE information and CVSS scores
- **Package Analysis**: Tracks vulnerable packages with version information

### AI-Powered Analysis
- **Intelligent Recommendations**: OpenAI GPT-4 powered suggestions for security improvements
- **Automated Security Scoring**: 0-100 security score calculation based on findings
- **Best Practice Guidance**: Context-aware recommendations for Dockerfile optimization
- **Remediation Steps**: Actionable fix suggestions with implementation guidance

### Reporting & Visualization
- **Multi-Format Reports**: Generate reports in JSON, CSV, PDF, and HTML formats
- **Professional Formatting**: Clean, well-structured reports with severity-based organization
- **Interactive HTML**: Web-based reports with styling and easy navigation
- **Machine-Readable Output**: JSON format for integration with other tools

### Developer Experience
- **Progress Indicators**: Real-time progress bars for long-running scans
- **Clear Error Messages**: Actionable error messages with troubleshooting steps
- **Multiple Scan Modes**: AI-only, scan-only, image-only, or full analysis
- **Configurable Timeouts**: Adjust timeouts for different scanning scenarios

### Production-Ready Reliability
- **Retry Logic**: Automatic retry with exponential backoff for transient failures
- **Rate Limiting**: Intelligent handling of OpenAI API rate limits
- **Error Recovery**: Graceful handling of network issues and API failures
- **Robust Logging**: Comprehensive logging for debugging and monitoring

### Flexibility & Integration
- **CLI Interface**: Simple command-line interface for local development
- **CI/CD Ready**: Easy integration into continuous integration pipelines
- **Environment Configuration**: Comprehensive configuration via environment variables
- **No-API-Key Mode**: Scan-only mode works without OpenAI API key


## 🧩 Architecture Diagram

Here’s how DockSec works behind the scenes:

![DockSec Architecture](https://github.com/advaitpatel/DockSec/blob/main/images/docksec-architecture-diagram-II.png)

![DockSec Architecture](https://github.com/advaitpatel/DockSec/blob/main/images/docksec-architecture-diagram-III.png)

- **Input**: Dockerfile + optional Docker image
- **Static Analysis**: Trivy, Hadolint, Docker Scout for comprehensive vulnerability detection
- **AI Layer**: LangChain + OpenAI GPT-4 for intelligent insights and automated security scoring
- **Output**: Multi-format security reports (PDF, HTML, JSON, CSV) with severity-based organization
- **Modes**: Full scan, AI-only, scan-only, or image-only modes
- **Reliability**: Automatic retry with exponential backoff, rate limiting support, configurable timeouts


## 🚀 Installation

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
This will install the DockSec using `setup.py` from local files.

To completely use the AI scanning of DockSec, you have to setup the `OPENAI-API-KEY`

  - 🔹 PowerShell (Windows): $env:OPENAI_API_KEY = "your-secret-key"

  - 🔹 Command Prompt (CMD on Windows): set OPENAI_API_KEY=your-secret-key

  - 🔹 Bash/Zsh (Linux/macOS): export OPENAI_API_KEY="your-secret-key"

  - 🔹 Or create a .env file with: OPENAI_API_KEY=your-secret-key

The following dependencies will be automatically installed:

  - `langchain` - AI orchestration framework
  - `langchain-openai` - OpenAI integration for LangChain
  - `python-dotenv` - Environment variable management
  - `pandas` - Data manipulation for reports
  - `tqdm` - Progress bars for long operations
  - `colorama` - Cross-platform colored terminal output
  - `rich` - Advanced terminal formatting and progress indicators
  - `fpdf2` - PDF report generation
  - `tenacity` - Retry logic with exponential backoff
  - `setuptools` - Package management

Congratulations, you can now explore and use DockSec! 🎉

### Configuration Options

DockSec supports configuration via environment variables. Create a `.env` file in your project root:

```bash
# Required for AI features
OPENAI_API_KEY=your-secret-key

# Optional: Customize LLM settings
LLM_MODEL=gpt-4o  # Default model
LLM_TEMPERATURE=0.0  # Response randomness (0-1)
LLM_REQUEST_TIMEOUT=60  # Request timeout in seconds
LLM_MAX_RETRIES=2  # Number of retries for failed requests

# Optional: Tool timeouts (in seconds)
DOCKER_IMAGE_INSPECT_TIMEOUT=30
HADOLINT_TIMEOUT=300
TRIVY_SCAN_TIMEOUT=600
DOCKER_SCOUT_TIMEOUT=300

# Optional: Retry configuration
RETRY_STOP_ATTEMPT=3  # Maximum retry attempts
RETRY_WAIT_MULTIPLIER=1  # Exponential backoff multiplier
RETRY_WAIT_MIN=2  # Minimum wait time between retries
RETRY_WAIT_MAX=10  # Maximum wait time between retries
```


## 📝 How to Use DockSec (CLI)

After installation, you can use DockSec with a simple command:

```bash
docksec path\to\Dockerfile
```

### Command-Line Options:

| Option | Description |
|--------|-------------|
| `dockerfile` | Path to the Dockerfile to analyze (optional when using `--image-only`) |
| `-i, --image` | Docker image name to scan (e.g., `myimage:latest`) |
| `-o, --output` | Output file for the report (default: `security_report.txt`) |
| `--ai-only` | Run only AI-based recommendations (requires Dockerfile) |
| `--scan-only` | Run only Dockerfile/image scanning (no AI analysis) |
| `--image-only` | Scan only the Docker image without Dockerfile analysis |

### Usage Examples:

```bash
# Basic analysis (Dockerfile + AI recommendations)
docksec path/to/Dockerfile

# Full analysis: Dockerfile + Docker image scanning + AI
docksec path/to/Dockerfile -i myimage:latest

# AI-only mode: Get recommendations without security scanning
docksec path/to/Dockerfile --ai-only

# Scan-only mode: Security scanning without AI (works without OpenAI API key)
docksec path/to/Dockerfile -i myimage:latest --scan-only

# Image-only mode: Scan Docker image without Dockerfile analysis
docksec --image-only -i myimage:latest

# Custom output file
docksec path/to/Dockerfile -o custom_report.txt
```

### What Gets Generated:

DockSec automatically generates comprehensive reports in the `results/` directory:

- **JSON Report** (`<image>_json.json`) - Machine-readable vulnerability data
- **CSV Report** (`<image>_csv.csv`) - Spreadsheet-friendly vulnerability list
- **PDF Report** (`<image>_pdf.pdf`) - Professional formatted security report
- **HTML Report** (`<image>_html.html`) - Interactive web-based report with styling
- **Text Report** (`security_report.txt`) - Human-readable summary with AI insights
- **Security Score** - Automated 0-100 rating based on findings

### Features in Action:

- **Progress Indicators**: Real-time progress bars show scan status
- **Error Recovery**: Automatic retry with exponential backoff for API calls
- **Rate Limiting**: Intelligent handling of OpenAI API rate limits
- **Actionable Messages**: Clear error messages with troubleshooting steps
- **Severity Filtering**: Focus on CRITICAL and HIGH vulnerabilities
- **Best Practices**: AI-powered recommendations for Dockerfile optimization

  - ### Legacy Usage

You can still use the original commands:

```bash
# For AI-based recommendations
python .\main.py "path\to\your\dockerfile"

# For scanning both Dockerfile and images
python docker_scanner.py <dockerfile_path> <image_name> [severity]
# Example: python docker_scanner.py .\Dockerfile myapp:latest CRITICAL,HIGH
```

  - ### External Tools Setup

To check the Dockerfile as well as images for vulnerabilities, you need to setup `Trivy` and `hadolint`:

```bash
python .\setup_external_tools.py
```

For manual installation, refer to [Trivy](https://trivy.dev/v0.18.3/installation/) and [hadolint](https://github.com/hadolint/hadolint?tab=readme-ov-file#install) documentation.


## 🔧 Troubleshooting

### Common Issues

**Problem**: `[ERROR] No OpenAI API Key provided`
- **Solution**: Set your OpenAI API key as an environment variable or in a `.env` file
- **Alternative**: Use `--scan-only` mode which doesn't require an API key

**Problem**: `Hadolint not found in PATH`
- **Solution**: Install Hadolint using the setup script: `python setup_external_tools.py`
- **Manual**: Follow [Hadolint installation guide](https://github.com/hadolint/hadolint#install)

**Problem**: `Trivy scan timed out`
- **Solution**: Increase timeout in `.env`: `TRIVY_SCAN_TIMEOUT=1200`
- **Alternative**: Scan smaller images or check network connectivity

**Problem**: OpenAI API rate limit errors
- **Solution**: DockSec automatically retries with exponential backoff
- **Manual**: Configure retry settings in `.env` file
- **Alternative**: Wait a few minutes and retry, or upgrade your OpenAI plan

**Problem**: Reports not generating
- **Solution**: Check the `results/` directory permissions
- **Manual**: Ensure the directory exists: `mkdir results`

### Debug Mode

For detailed logging, set the log level:

```bash
export LOG_LEVEL=DEBUG
docksec path/to/Dockerfile
```

### Getting Help

If you encounter issues:
1. Check the logs in the console output
2. Review error messages - they include troubleshooting steps
3. [Open an issue](https://github.com/advaitpatel/DockSec/issues/new) with:
   - DockSec version
   - Command used
   - Error message
   - Operating system


## 🎬 Examples & Screenshots

### Example: Scanning a Vulnerable Dockerfile

Check out our example Dockerfiles in the [`examples/`](examples/) directory:

- **Secure Python App** - Best practices example (Score: 90+)
- **Vulnerable Node App** - Common mistakes to avoid (Score: 30-)
- **Multi-stage Golang** - Advanced optimization patterns (Score: 95+)

```bash
# Try scanning our example vulnerable Dockerfile
git clone https://github.com/advaitpatel/DockSec.git
cd DockSec/examples/dockerfiles/vulnerable-node-app
docksec Dockerfile
```

**Sample Output:**
```
🔍 Scanning Dockerfile...
⚠️  Security Score: 32/100

Critical Issues (5):
  • Hardcoded secrets detected
  • Running as root user
  • Using 'latest' tag

High Issues (8):
  • Outdated packages with CVEs
  • Unnecessary packages installed
  ...

💡 AI Recommendations:
  1. Remove hardcoded secrets and use environment variables
  2. Create non-root user: RUN adduser -S appuser && USER appuser
  3. Use specific version tags: FROM node:18-alpine
  ...

📊 Reports generated in: results/
```

For more examples and sample reports, see the [`examples/`](examples/) directory.


## ☝️ Need Help or Want to Provide Feedback?

If you encounter any problems, we will be happy to support you wherever we can.
For bugs, issues or feature requests feel free to [open an issue](https://github.com/advaitpatel/DockSec/issues/new).
We are happy to assist you with anything related to the project.


## 🤝 How to Contribute to DockSec

We welcome contributions from the community! Whether it's:

- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📝 Improving documentation
- 🔧 Submitting pull requests

See our [Contributing Guide](CONTRIBUTING.md) for detailed instructions.


## 📚 Documentation

- **[Quick Start Guide](#quick-start)** - Get started in 3 steps
- **[Installation](#-installation)** - Detailed installation instructions
- **[Usage Examples](#-how-to-use-docksec-cli)** - CLI usage and examples
- **[Configuration](CONTRIBUTING.md#configuration)** - Environment variables and settings
- **[Examples Directory](examples/)** - Sample Dockerfiles and use cases
- **[Troubleshooting](#-troubleshooting)** - Common issues and solutions
- **[Changelog](CHANGELOG.md)** - Version history and updates
- **[Security Policy](SECURITY.md)** - Security guidelines and reporting


## 🗺️ Roadmap

### Coming Soon
- [ ] Docker Compose support
- [ ] Kubernetes manifest scanning
- [ ] GitHub Actions integration
- [ ] Custom rule engine
- [ ] Web dashboard interface

### Under Consideration
- [ ] Support for additional LLM providers (Claude, Gemini)
- [ ] SBOM generation
- [ ] Container runtime monitoring
- [ ] VSCode extension

Vote on features or suggest new ones in [GitHub Discussions](https://github.com/advaitpatel/DockSec/discussions)!


## 👾 Activity

![DockSec Activity](https://repobeats.axiom.co/api/embed/c5aac6f5d22bd6b83a21ae51353dd7bcb43f9517.svg "DockSec activity image")


## 📘 License

The DockSec is licensed under the MIT license. For more information check the [LICENSE](https://github.com/advaitpatel/DockSec/blob/main/LICENSE) file for details.