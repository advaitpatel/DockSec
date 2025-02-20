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