import logging
import sys
import os
from langchain_openai import ChatOpenAI
from config import (
    BASE_DIR,
    OPENAI_API_KEY
)
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List
import time
from tqdm import tqdm
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table

def get_custom_logger(name: str = 'Docksec'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(name)s - Line %(lineno)d: %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


logger = get_custom_logger(name=__name__)

# Load docker file from the provided directory path if not provided get it from the BASE_DIR

def load_docker_file(docker_file_path: str = None):
    if not docker_file_path:
        docker_file_path = BASE_DIR + "/Dockerfile"
    try:
        with open(docker_file_path, "r") as file:
            docker_file = file.read()
    except FileNotFoundError:
        logger.error(f"File not found at path: {docker_file_path}")
        return None
    return docker_file

class AnalsesResponse(BaseModel ):
    vulnerabilities: List[str] = Field(description="List of vulnerabilities found in the Dockerfile")
    best_practices: List[str] = Field(description="Best practices to follow to mitigate these vulnerabilities")
    SecurityRisks: List[str] = Field(description= "security risks associated with Dockerfile")
    ExposedCredentials: List[str] = Field(description="List of exposed credentials in the Dockerfile")
    remediation: List[str] = Field(description="List of remediation steps to fix the vulnerabilities")

class ScoreResponse(BaseModel):
    score: float = Field(description="Security score for the Dockerfile")

def get_llm():
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    # structure_llm = llm.with_structured_output(AnalsesResponse, method = "json_mode")
    return llm




# Initialize colorama for Windows compatibility
init(autoreset=True)

# Initialize Rich Console
console = Console()

def print_section(title, items, color):
    console.print(f"\n[bold {color}]{'=' * (len(title) + 4)}[/]")
    console.print(f"[bold {color}]| {title} |[/]")
    console.print(f"[bold {color}]{'=' * (len(title) + 4)}[/]")
    if items:
        for i, item in enumerate(items, start=1):
            console.print(f"[{color}]{i}. {item}[/]")
    else:
        console.print("[green]No issues found![/] ✅")

def analyze_security(response):

    vulnerabilities = response.vulnerabilities
    best_practices = response.best_practices
    security_risks = response.SecurityRisks
    exposed_credentials = response.ExposedCredentials
    remediation = response.remediation

    # Simulating scanning with tqdm
    with tqdm(total=100, bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} {elapsed}s[/]") as pbar:
        console.print("\n[cyan]🔍 Scanning Dockerfile...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]🛠️  Analyzing vulnerabilities...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]🔐 Checking security risks...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]📌 Reviewing best practices...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]🔑 Checking for exposed credentials...[/]")
        time.sleep(1)
        pbar.update(20)

    # Print Sections
    print_section("Vulnerabilities", vulnerabilities, "red")
    print_section("Best Practices", best_practices, "blue")
    print_section("Security Risks", security_risks, "yellow")
    print_section("Exposed Credentials", exposed_credentials, "magenta")
    print_section("Remediation Steps", remediation, "green")
    



