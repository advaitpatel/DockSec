from setuptools import setup
import os
import glob
setup(
    name="docksec",
    version="2026.4.2",
    description="AI-Powered Docker Security Analyzer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Advait Patel",
    url="https://github.com/advaitpatel/DockSec",
    py_modules=["docksec", "main", "docker_scanner", "utils", "config", "config_manager", "report_generator", "score_calculator", "setup_external_tools"],
    entry_points={
        "console_scripts": [
            "docksec=docksec:main",
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/advaitpatel/DockSec/issues",
        "Documentation": "https://github.com/advaitpatel/DockSec/blob/main/README.md",
        "Source Code": "https://github.com/advaitpatel/DockSec",
    },
    python_requires=">=3.12",
    install_requires=[
        "pydantic==2.10.3",
        "langchain-core==0.3.26",
        "langchain==0.3.13",
        "langchain-openai==0.2.10",
        "langchain-anthropic==0.3.0",
        "langchain-google-genai==2.0.5",
        "langchain-ollama==0.2.0",
        "python-dotenv==1.0.1",
        "pandas==2.2.3",
        "tqdm==4.67.1",
        "colorama==0.4.6",
        "rich==13.9.4",
        "fpdf2==2.8.1",
        "tenacity==9.0.0",
        "setuptools>=65.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    # Ensure all Python files and templates are included in the distribution
    package_data={
        '': ['*.py', 'templates/*.html', 'templates/**/*.html'],
    },
)