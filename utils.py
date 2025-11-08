import logging
import sys
import os
from langchain_openai import ChatOpenAI
from config import (
    BASE_DIR,
    OPENAI_API_KEY
)
try:
    from langchain_core.pydantic_v1 import BaseModel, Field
except ImportError:
    # Fallback to standard pydantic if langchain_core.pydantic_v1 is not available
    try:
        from pydantic import BaseModel, Field
    except ImportError:
        raise ImportError(
            "Either 'pydantic' or 'langchain-core' must be installed. "
            "Install with: pip install pydantic langchain-core"
        )
from typing import List, Optional, Any
import time
from tqdm import tqdm
from colorama import Fore, Style, init
from rich.console import Console
from rich.table import Table
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
    after_log
)
from openai import (
    APIError,
    RateLimitError,
    APIConnectionError,
    APITimeoutError
)

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

def load_docker_file(docker_file_path: Optional[str] = None) -> Optional[str]:
    """
    Load Dockerfile content from the specified path.
    
    Args:
        docker_file_path: Path to the Dockerfile. If None, defaults to BASE_DIR/Dockerfile
        
    Returns:
        str: Content of the Dockerfile, or None if file not found
    """
    if not docker_file_path:
        docker_file_path = BASE_DIR + "/Dockerfile"
    try:
        with open(docker_file_path, "r") as file:
            docker_file: str = file.read()
    except FileNotFoundError:
        logger.error(f"File not found at path: {docker_file_path}")
        return None
    return docker_file

class AnalyzesResponse(BaseModel):
    vulnerabilities: List[str] = Field(description="List of vulnerabilities found in the Dockerfile")
    best_practices: List[str] = Field(description="Best practices to follow to mitigate these vulnerabilities")
    SecurityRisks: List[str] = Field(description= "security risks associated with Dockerfile")
    ExposedCredentials: List[str] = Field(description="List of exposed credentials in the Dockerfile")
    remediation: List[str] = Field(description="List of remediation steps to fix the vulnerabilities")

class ScoreResponse(BaseModel):
    score: float = Field(description="Security score for the Dockerfile")

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((APIError, APIConnectionError, APITimeoutError, RateLimitError)),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    after=after_log(logger, logging.INFO)
)
def _call_llm_with_retry(llm, *args, **kwargs):
    """
    Internal function to call LLM with retry logic.
    Retries on transient errors with exponential backoff.
    """
    return llm.invoke(*args, **kwargs)


def get_llm():
    """
    Get LLM instance with retry logic and rate limiting support.
    
    This function checks for API key availability and returns a configured
    ChatOpenAI instance. All calls through this LLM will have automatic retry
    logic with exponential backoff for transient failures and rate limiting.
    
    Returns:
        ChatOpenAI: Configured LLM instance
        
    Raises:
        EnvironmentError: If OPENAI_API_KEY is not set
        
    Note:
        - Retries up to 3 times on transient errors
        - Uses exponential backoff: 2s, 4s, 8s
        - Handles rate limiting automatically
    """
    from config import get_openai_api_key
    # Check API key only when LLM is actually needed
    try:
        api_key = get_openai_api_key()
        if not os.getenv("OPENAI_API_KEY"):
            os.environ["OPENAI_API_KEY"] = api_key
        
        # Configure LLM with timeout and error handling
        llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0,
            request_timeout=60,  # 60 second timeout
            max_retries=2  # LangChain's own retry on top of our retry logic
        )
        logger.info("LLM initialized successfully with retry logic enabled")
        return llm
        
    except Exception as e:
        logger.error(f"Failed to initialize LLM: {str(e)}")
        console.print(f"\n[red]Error initializing AI features:[/red] {str(e)}")
        console.print("\n[yellow]Troubleshooting steps:[/yellow]")
        console.print("1. Verify your OpenAI API key is correct")
        console.print("2. Check your internet connection")
        console.print("3. Verify your OpenAI account has available credits")
        console.print("4. Try using --scan-only mode if you don't need AI features")
        raise




# Initialize colorama for Windows compatibility
init(autoreset=True)

# Initialize Rich Console
console = Console()

def print_section(title: str, items: List[str], color: str) -> None:
    """
    Print a formatted section with title and items using rich console.
    
    Args:
        title: Section title
        items: List of items to display
        color: Color for the section (e.g., 'red', 'green', 'yellow')
    """
    console.print(f"\n[bold {color}]{'=' * (len(title) + 4)}[/]")
    console.print(f"[bold {color}]| {title} |[/]")
    console.print(f"[bold {color}]{'=' * (len(title) + 4)}[/]")
    if items:
        for i, item in enumerate(items, start=1):
            console.print(f"[{color}]{i}. {item}[/]")
    else:
        console.print("[green]No issues found![/]")

def analyze_security(response: AnalyzesResponse) -> None:
    """
    Analyze and display security findings from Dockerfile analysis.
    
    Args:
        response: AnalyzesResponse object containing vulnerability findings
    """

    vulnerabilities = response.vulnerabilities
    best_practices = response.best_practices
    security_risks = response.SecurityRisks
    exposed_credentials = response.ExposedCredentials
    remediation = response.remediation

    # Simulating scanning with tqdm
    with tqdm(total=100, bar_format="{l_bar}{bar} {n_fmt}/{total_fmt} {elapsed}s[/]") as pbar:
        console.print("\n[cyan]Scanning Dockerfile...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]Analyzing vulnerabilities...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]Checking security risks...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]Reviewing best practices...[/]")
        time.sleep(1)
        pbar.update(20)

        console.print("[cyan]Checking for exposed credentials...[/]")
        time.sleep(1)
        pbar.update(20)

    # Print Sections
    print_section("Vulnerabilities", vulnerabilities, "red")
    print_section("Best Practices", best_practices, "blue")
    print_section("Security Risks", security_risks, "yellow")
    print_section("Exposed Credentials", exposed_credentials, "magenta")
    print_section("Remediation Steps", remediation, "green")
    



