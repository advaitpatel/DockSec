from setuptools import setup
import os
import glob
setup(
    name="docksec",
    version="0.0.20",
    description="AI-Powered Docker Security Analyzer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Advait Patel",
    url="https://github.com/advaitpatel/DockSec",
    py_modules=["docksec", "main", "docker_scanner", "utils", "config", "setup_external_tools"],
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
        "pydantic>=2.0.0,<3.0.0",
        "langchain-core>=0.3.0,<2.0.0",
        "langchain>=0.3.0,<2.0.0",
        "langchain-openai>=0.2.0,<1.0.0",
        "python-dotenv>=1.0.0,<2.0.0",
        "pandas>=2.0.0,<3.0.0",
        "tqdm>=4.65.0,<5.0.0",
        "colorama>=0.4.6,<1.0.0",
        "rich>=13.0.0,<14.0.0",
        "fpdf2>=2.7.0,<3.0.0",
        "tenacity>=8.0.0,<9.0.0",
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