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
        "ExposedCredentials": ["credential1", "credential2", "credential3"]
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