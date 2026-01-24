[![GitHub Repo stars](https://img.shields.io/github/stars/advaitpatel/DockSec?style=flat)](https://github.com/advaitpatel/DockSec)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/docksec.svg)](https://pypi.org/project/docksec/)
[![Python Version](https://img.shields.io/pypi/pyversions/docksec.svg)](https://pypi.org/project/docksec/)

<div align="center">
  <img src="https://github.com/advaitpatel/DockSec/blob/main/images/docksec-logo-II.png" alt="DockSec" height="120">
  
  <h1>DockSec</h1>
  <p><strong>AI-powered Docker security scanner that explains vulnerabilities in plain English</strong></p>
  
  <p>
    <a href="#quick-start">Quick Start</a> •
    <a href="#features">Features</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a> •
    <a href="docs/CONTRIBUTING.md">Contributing</a>
  </p>
</div>

---

## What is DockSec?

DockSec combines traditional Docker security scanners (Trivy, Hadolint, Docker Scout) with AI to provide **context-aware security analysis**. Instead of dumping 200 CVEs and leaving you to figure it out, DockSec:

- 🎯 Prioritizes what actually matters
- 💡 Explains vulnerabilities in plain English  
- 🔧 Suggests specific fixes for YOUR Dockerfile
- 📊 Generates professional security reports

Think of it as having a security expert review your Dockerfiles.

## How It Works

<div align="center">
  <img src="images/workflow.png" alt="DockSec Workflow" width="800">
  <p><em>DockSec workflow: From scanning to actionable insights</em></p>
</div>

DockSec follows a simple pipeline:
1. **Scan** - Runs Trivy, Hadolint, and Docker Scout on your images/Dockerfiles
2. **Analyze** - AI processes all findings and correlates them with your setup
3. **Recommend** - Get plain English explanations with specific line-by-line fixes
4. **Report** - Export results in JSON, PDF, HTML, or Markdown formats

## Quick Start

```bash
# Install
pip install docksec

# Scan your Dockerfile
docksec Dockerfile

# Scan with image analysis
docksec Dockerfile -i myapp:latest

# Scan without AI (no API key needed)
docksec Dockerfile --scan-only
```

## Features

- **Smart Analysis**: AI explains what vulnerabilities mean for your specific setup
- **Multiple Scanners**: Integrates Trivy, Hadolint, and Docker Scout
- **Security Scoring**: Get a 0-100 score to track improvements
- **Multiple Formats**: Export reports as HTML, PDF, JSON, or CSV
- **No AI Required**: Works offline with `--scan-only` mode
- **CI/CD Ready**: Easy integration into build pipelines

## Installation

**Requirements:** Python 3.12+, Docker (for image scanning)

```bash
pip install docksec
```

**For AI features**, set your OpenAI API key:
```bash
export OPENAI_API_KEY="your-key-here"
```

**External tools** (optional, for full scanning):
```bash
# Install Trivy and Hadolint
python -m docksec.setup_external_tools

# Or install manually:
# - Trivy: https://aquasecurity.github.io/trivy/
# - Hadolint: https://github.com/hadolint/hadolint
```

## Usage

### Basic Scanning

```bash
# Analyze Dockerfile with AI recommendations
docksec Dockerfile

# Scan Dockerfile + Docker image
docksec Dockerfile -i nginx:latest

# Get only scan results (no AI)
docksec Dockerfile --scan-only

# Scan image without Dockerfile
docksec --image-only -i nginx:latest
```

### CLI Options

| Option | Description |
|--------|-------------|
| `dockerfile` | Path to Dockerfile |
| `-i, --image` | Docker image to scan |
| `-o, --output` | Output file path |
| `--ai-only` | AI analysis only (no scanning) |
| `--scan-only` | Scanning only (no AI) |
| `--image-only` | Scan image without Dockerfile |

### Configuration

Create a `.env` file for advanced configuration:

```bash
OPENAI_API_KEY=your-key
LLM_MODEL=gpt-4o
TRIVY_SCAN_TIMEOUT=600
```

See [full configuration options](docs/CONTRIBUTING.md#configuration).

## Example Output

```
🔍 Scanning Dockerfile...
⚠️  Security Score: 45/100

Critical Issues (3):
  • Running as root user (line 12)
  • Hardcoded API key detected (line 23)
  • Using vulnerable base image

💡 AI Recommendations:
  1. Add non-root user: RUN useradd -m appuser && USER appuser
  2. Move secrets to environment variables or build secrets
  3. Update FROM ubuntu:20.04 to ubuntu:22.04 (fixes 12 CVEs)

📊 Full report: results/nginx_latest_report.html
```

## Examples

Check out example Dockerfiles in [`examples/`](examples/):

- **Secure Python app** - Best practices (Score: 95/100)
- **Vulnerable Node app** - Common mistakes (Score: 32/100)  
- **Multi-stage Go build** - Advanced patterns (Score: 98/100)

## Architecture

```
Dockerfile → [Trivy + Hadolint + Scout] → AI Analysis → Reports
```

DockSec runs security scanners locally, then uses GPT-4 to:
1. Combine and deduplicate findings
2. Assess real-world impact for your context
3. Generate actionable remediation steps
4. Calculate security score

All scanning happens on your machine. Only scan results (not your code) are sent to OpenAI when using AI features.

## Roadmap

- [ ] Docker Compose support
- [ ] Kubernetes manifest scanning  
- [ ] Additional LLM providers (Claude, local models)
- [ ] GitHub Actions integration
- [ ] Custom security policies

See [open issues](https://github.com/advaitpatel/DockSec/issues) or suggest features in [discussions](https://github.com/advaitpatel/DockSec/discussions).

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

Quick links:
- [Report a bug](https://github.com/advaitpatel/DockSec/issues/new?template=bug_report.md)
- [Request a feature](https://github.com/advaitpatel/DockSec/issues/new?template=feature_request.md)
- [View roadmap](https://github.com/advaitpatel/DockSec/issues)

## Documentation

- [Installation Guide](docs/CONTRIBUTING.md#development-setup)
- [Configuration Options](docs/CONTRIBUTING.md#configuration)
- [Examples](examples/)
- [Changelog](docs/CHANGELOG.md)
- [Security Policy](docs/SECURITY.md)

## Troubleshooting

**"No OpenAI API Key provided"**  
→ Set `OPENAI_API_KEY` or use `--scan-only` mode

**"Hadolint not found"**  
→ Run `python -m docksec.setup_external_tools`

**"Python version not supported"**  
→ DockSec requires Python 3.12+. Use `pyenv install 3.12` to upgrade.

**"Where are my scan results?"**  
→ Results are saved to `results/` directory in your DockSec installation  
→ Customize location: `export DOCKSEC_RESULTS_DIR=/custom/path`

For more issues, see [Troubleshooting Guide](docs/CONTRIBUTING.md#troubleshooting).

## License

MIT License - see [LICENSE](LICENSE) for details.

## Links

- **PyPI**: https://pypi.org/project/docksec/
- **Issues**: https://github.com/advaitpatel/DockSec/issues
- **Discussions**: https://github.com/advaitpatel/DockSec/discussions

---

<div align="center">
  
  **If DockSec helps you, give it a ⭐ to help others discover it!**
  
  Built with ❤️ by [Advait Patel](https://github.com/advaitpatel)
  
</div>
