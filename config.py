from dotenv import load_dotenv
import os


load_dotenv()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

if not OPENAI_API_KEY:
    error_message = """
❌ No OpenAI API Key provided.

You can fix this by setting the `OPENAI_API_KEY` in one of the following ways:

🔹 PowerShell (Windows):
    $env:OPENAI_API_KEY = "your-secret-key"

🔹 Command Prompt (CMD on Windows):
    set OPENAI_API_KEY=your-secret-key

🔹 Bash/Zsh (Linux/macOS):
    export OPENAI_API_KEY="your-secret-key"

🔹 Or create a `.env` file with:
    OPENAI_API_KEY=your-secret-key


🔒 Reminder: Never hardcode your API key in public code or repositories. it is necessary to use Docksec

"""
    raise EnvironmentError(error_message.strip())
else:
    print("✅ OpenAI API Key found in environment variables.")


os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

RESULTS_DIR = os.path.join(BASE_DIR, "results")

os.makedirs(os.path.dirname(RESULTS_DIR), exist_ok=True)



from langchain.prompts import PromptTemplate

docker_agent_template = """
    you are an AI agent that is tasked with analyzing a Dockerfile for security vulnerabilities.
    The Dockerfile is provided to you as a string.
    You need to analyze the Dockerfile and provide a report on the security vulnerabilities present in the Dockerfile.
    You need to identify the vulnerabilities and provide a detailed report on the security risks associated with each vulnerability.

    Output format should be json as below:

    {{
        "vulnerabilities": ["vulnerability1", "vulnerability2", "vulnerability3"],
        "best_practices": ["best practice1", "best practice2", "best practice3"],
        "SecurityRisks": ["security risk1", "security risk2", "security risk3"],
        "ExposedCredentials": ["credential1", "credential2", "credential3"],
        "remediation": ["remediation1", "remediation2", "remediation3"]
    }}


    Docker File to analyze: \n {filecontent}

"""

docker_agent_prompt = PromptTemplate(
    input_variables=["filecontent"],
    template=docker_agent_template
)

docker_score_template = """
You are a Docker Security Expert with extensive knowledge of container security best practices, vulnerabilities, and compliance standards. You will be provided with the security scan results from tools such as Trivy, Clair, or Docker Bench for Security. Your task is to analyze these results and assign a security score between 1 and 100 based on the severity, number, and impact of detected vulnerabilities or misconfigurations.

    ### Scoring Criteria:
    - Base the score on factors including:
    - **Vulnerability Severity**: Critical (high impact), High, Medium, Low.
    - **Misconfigurations**: Privileged containers, exposed sensitive information, missing security policies.
    - **CVE Scores**: Common Vulnerabilities and Exposures (CVEs) detected in the image.
    - **Compliance Violations**: CIS Docker Benchmark compliance, runtime security policies.
    - **Attack Surface Exposure**: Open ports, excessive privileges, unnecessary packages.
    - **Dependency Risks**: Outdated base images, unpatched libraries.

    ### Output Format:
    Your response must be a JSON object with a single key-value pair:

    {{
        "score": 90
    }}
    
    Results:
    {results}



"""

docker_score_prompt = PromptTemplate(
    input_variables=["results"],
    template=docker_score_template
)