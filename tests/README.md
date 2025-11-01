# DockSec Test Suite

This directory contains unit and integration tests for DockSec.

## Test Structure

- `test_docker_scanner.py`: Unit tests for the DockerSecurityScanner class
- `test_utils.py`: Unit tests for utility functions
- `test_config.py`: Unit tests for configuration management
- `test_integration.py`: Integration tests that test multiple components together
- `conftest.py`: Pytest fixtures and configuration

## Running Tests

### Using unittest
```bash
python -m unittest discover tests
```

### Using pytest (if installed)
```bash
pytest tests/
```

### Running specific test file
```bash
python -m unittest tests.test_docker_scanner
```

## Test Coverage

Currently, tests cover:
- Input validation (image names, file paths, severity levels)
- Tool checking and installation instructions
- Dockerfile loading
- Configuration and API key handling
- LLM initialization
- Basic scanner initialization

## Adding New Tests

When adding new functionality, please add corresponding tests:
1. Unit tests for individual functions/methods
2. Integration tests for workflows
3. Update this README if adding new test categories

