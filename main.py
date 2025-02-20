import argparse
from utils import (
    get_custom_logger,
    load_docker_file,
    get_llm,
    analyze_security,
)
from prompts import docker_agent_prompt
import os
from langchain_core.output_parsers import StrOutputParser
from pathlib import Path
logger = get_custom_logger(name=__name__)

llm = get_llm()
analyser_chain = docker_agent_prompt | llm 



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze Dockerfile security risks")
    parser.add_argument("docker_file_path", nargs="?", default=r"testfiles\1\Dockerfile", help="Path to the Dockerfile")
    args = parser.parse_args()
    filecontent = load_docker_file(docker_file_path=Path(args.docker_file_path))

    if not filecontent:
        logger.error("No Dockerfile content found. Exiting...")
        exit(1)

    response = analyser_chain.invoke({"filecontent": filecontent})
    analyze_security(response)
    



