# DockSec - AI-Powered Docker Security Analyzer

## Overview
DockSec is an open-source AI-powered tool designed to analyze Dockerfiles for security vulnerabilities, misconfigurations, and inefficiencies. It provides automated recommendations to enhance container security, reduce the attack surface, and improve compliance with industry best practices.

## Features
- AI/ML-Powered Analysis: Uses AI models to detect vulnerabilities and suggest security improvements.
- Security Vulnerability Detection: Scans Dockerfiles for known security issues, CVEs, and misconfigurations.
- Best Practice Recommendations: Provides actionable insights to enhance security, minimize image size, and improve efficiency.
- Integration with Development Tools:
-- VS Code extension for inline security suggestions.
-- CI/CD pipeline support (GitHub Actions, GitLab CI, Jenkins).
- Compliance Checks: Aligns with CIS Benchmarks, Docker Security Best Practices, and OWASP guidelines.

## Installation
TBD

## Usage
To Run the application the following steps need to be followed.

its preferred to create a virtual environment for it 

```
python -m venv env # for mac use python3
```

Install all the dependencies with 

```
pip install -r requirements.txt # use pip3 for mac
```

Test the Docker File by passing path 

```
python .\main.py "path to your docker file"
```

To check the Dockerfile as well as images for the vulnerabilities

you need to setup Trivy and hadolint in your system for that you can use `python .\setup_external_tools.py` to setup but its recommended to use the documentation for [Trivy](https://trivy.dev/v0.18.3/installation/) and [hadolint](https://github.com/hadolint/hadolint?tab=readme-ov-file#install)

```
python docker_scanner.py <dockerfile_path> <image_name> [severity] # python docker_scanner.py ./Dockerfile myapp:latest CRITICAL,HIGH
```

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
