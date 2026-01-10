# Contributing to DockSec

First off, thank you for considering contributing to DockSec! 🎉

It's people like you that make DockSec such a great tool. We welcome contributions from everyone, whether you're fixing a typo, reporting a bug, or implementing a major new feature.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Community](#community)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our commitment to fostering an open and welcoming environment. By participating, you are expected to uphold this code:

- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Focus on what is best** for the community
- **Show empathy** towards other community members

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

1. **Use a clear and descriptive title**
2. **Describe the exact steps to reproduce the problem**
3. **Provide specific examples** (commands, Dockerfiles, etc.)
4. **Describe the behavior** you observed and what you expected
5. **Include screenshots or error messages** if applicable
6. **Specify your environment** (OS, Python version, DockSec version)

Use our [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.md) when creating issues.

### Suggesting Features

Feature suggestions are welcome! Before creating a feature request:

1. **Check if the feature already exists** in the latest version
2. **Search existing issues** to see if someone else suggested it
3. **Provide a clear use case** for the feature
4. **Explain why this feature would be useful** to most users

Use our [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.md).

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:

- `good first issue` - Good for newcomers
- `help wanted` - Issues where we need community help
- `documentation` - Documentation improvements

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following our code style guidelines
3. **Add or update tests** as needed
4. **Update documentation** if you changed functionality
5. **Ensure all tests pass** before submitting
6. **Write a clear commit message** describing your changes
7. **Submit a pull request** using our PR template

## 🛠️ Development Setup

### Prerequisites

- Python 3.12 or higher
- Git
- Docker (for testing image scanning)
- Trivy and Hadolint (for full functionality)

### Setup Steps

1. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/DockSec.git
   cd DockSec
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   pip install -r requirements.txt
   ```

4. **Install development dependencies**:
   ```bash
   pip install pytest pytest-cov black isort flake8 mypy
   ```

5. **Install external tools** (optional, for full testing):
   ```bash
   python setup_external_tools.py
   ```

6. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key if testing AI features
   ```

### Verify Installation

```bash
# Run DockSec
docksec -h

# Run tests
pytest tests/

# Check code style
black --check .
isort --check-only .
flake8 .
mypy .
```

## 🎨 Code Style Guidelines

We follow Python best practices and use automated tools to maintain code quality.

### Style Tools

- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

### Running Style Checks

```bash
# Format code
black .
isort .

# Check linting
flake8 .

# Type checking
mypy .
```

### Code Standards

1. **Follow PEP 8** style guide
2. **Use type hints** for all functions
3. **Write docstrings** for all public functions and classes
4. **Keep functions small** and focused
5. **Add comments** for complex logic
6. **Use meaningful variable names**

### Example

```python
from typing import List, Optional

def analyze_dockerfile(
    dockerfile_path: str,
    severity_levels: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Analyze a Dockerfile for security vulnerabilities.
    
    Args:
        dockerfile_path: Path to the Dockerfile to analyze
        severity_levels: Optional list of severity levels to filter
        
    Returns:
        Dictionary containing analysis results
        
    Raises:
        FileNotFoundError: If Dockerfile doesn't exist
        ValueError: If Dockerfile path is invalid
    """
    # Implementation here
    pass
```

## 🧪 Testing

We maintain high test coverage to ensure code quality.

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_docker_scanner.py

# Run specific test function
pytest tests/test_docker_scanner.py::test_scan_dockerfile
```

### Writing Tests

1. **Create test files** in the `tests/` directory
2. **Name test functions** starting with `test_`
3. **Use descriptive test names** that explain what's being tested
4. **Test edge cases** and error conditions
5. **Use fixtures** for common setup
6. **Mock external dependencies** (API calls, file I/O)

### Example Test

```python
import pytest
from docksec import analyze_dockerfile

def test_analyze_dockerfile_success():
    """Test successful Dockerfile analysis."""
    result = analyze_dockerfile("tests/fixtures/good_dockerfile")
    assert result["score"] > 80
    assert "vulnerabilities" in result

def test_analyze_dockerfile_missing_file():
    """Test error handling for missing Dockerfile."""
    with pytest.raises(FileNotFoundError):
        analyze_dockerfile("nonexistent/Dockerfile")
```

## 📚 Documentation

Good documentation is crucial! When contributing:

### Code Documentation

- Add **docstrings** to all public functions and classes
- Use **Google-style docstrings**
- Include **type hints** in function signatures
- Add **inline comments** for complex logic

### User Documentation

- Update **README.md** if you add features
- Add **examples** in the `examples/` directory
- Update **CLI help text** if you change commands
- Add entries to **CHANGELOG.md**

### Documentation Style

- Use **clear, simple language**
- Provide **code examples**
- Include **expected output**
- Add **troubleshooting tips** if needed

## 🏗️ Project Structure

```
DockSec/
├── .github/              # GitHub templates and workflows
├── examples/             # Example Dockerfiles and usage
├── templates/            # Report templates
├── tests/                # Test files
├── docksec.py           # Main CLI entry point
├── main.py              # AI analysis module
├── docker_scanner.py    # Scanning engine
├── utils.py             # Utility functions
├── config.py            # Configuration management
├── report_generator.py  # Report generation
├── score_calculator.py  # Security scoring
├── requirements.txt     # Dependencies
├── setup.py             # Package configuration
├── README.md            # Main documentation
├── CONTRIBUTING.md      # This file
├── CHANGELOG.md         # Version history
└── SECURITY.md          # Security policy
```

## 🔄 Development Workflow

1. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes** and commit them:
   ```bash
   git add .
   git commit -m "feat: add new feature"
   ```

3. **Keep your branch up to date**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a pull request** on GitHub

### Commit Message Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(scanner): add Docker Compose support
fix(cli): handle missing Dockerfile gracefully
docs(readme): add installation instructions for Windows
test(scanner): add unit tests for Trivy integration
```

## 🚀 Release Process

Maintainers follow this process for releases:

1. Update version in `setup.py`
2. Update `CHANGELOG.md` with release notes
3. Create a git tag: `git tag v0.0.X`
4. Push tag: `git push origin v0.0.X`
5. Build and publish to PyPI: `python -m build && twine upload dist/*`
6. Create GitHub release with changelog

## 💬 Community

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and community discussion
- **Pull Requests**: Code contributions

### Getting Help

- Read the [README](README.md) and [examples](examples/)
- Check [existing issues](https://github.com/advaitpatel/DockSec/issues)
- Ask questions in [Discussions](https://github.com/advaitpatel/DockSec/discussions)

## 📄 License

By contributing to DockSec, you agree that your contributions will be licensed under the MIT License.

## 🙏 Recognition

Contributors are recognized in:
- GitHub contributors page
- Release notes for significant contributions
- README acknowledgments (for major features)

## ❓ Questions?

Don't hesitate to ask! You can:

1. Open an issue with the `question` label
2. Start a discussion on GitHub Discussions
3. Reach out to the maintainers

---

**Thank you for contributing to DockSec! Your efforts help make Docker security more accessible to everyone.** 🎉
