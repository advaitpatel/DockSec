from setuptools import setup

setup(
    name="docksec",
    version="0.1.0",
    description="Docker security analysis tool",
    author="Advait Patel",
    py_modules=["docksec"],
    entry_points={
        "console_scripts": [
            "docksec=docksec:main",
        ],
    },
    install_requires=[
        "langchain",
        "langchain-openai",
        "python-dotenv",
        "pandas",
        "tqdm",
        "colorama",
        "rich",
        "fpdf",
        "setuptools",
    ],
)