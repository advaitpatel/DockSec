"""Pytest configuration and fixtures."""
import pytest
import os
import tempfile
import shutil


@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    test_dir = tempfile.mkdtemp()
    yield test_dir
    shutil.rmtree(test_dir)


@pytest.fixture
def sample_dockerfile(temp_dir):
    """Create a sample Dockerfile for testing."""
    dockerfile_path = os.path.join(temp_dir, "Dockerfile")
    with open(dockerfile_path, 'w') as f:
        f.write("FROM ubuntu:latest\nRUN echo 'test'\n")
    return dockerfile_path

