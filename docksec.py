#!/usr/bin/env python3

import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Docker Security Analysis Tool')
    parser.add_argument('dockerfile', help='Path to the Dockerfile to analyze')
    parser.add_argument('-i', '--image', help='Docker image name to scan (required for --scan-only)')
    parser.add_argument('-o', '--output', help='Output file for the report (default: security_report.txt)')
    parser.add_argument('--ai-only', action='store_true', help='Run only AI-based recommendations')
    parser.add_argument('--scan-only', action='store_true', help='Run only Dockerfile/image scanning (requires --image)')
    
    args = parser.parse_args()
    
    # Validate that the Dockerfile exists
    if not os.path.isfile(args.dockerfile):
        print(f"Error: Dockerfile not found at {args.dockerfile}")
        sys.exit(1)
    
    # Determine which tools to run
    run_ai = not args.scan_only
    run_scan = not args.ai_only
    
    if not run_ai and not run_scan:
        run_ai = run_scan = True  # Run both by default
    
    # Validate image requirement for scanning
    if run_scan and not args.image:
        print("Error: Image name is required for scanning. Use -i/--image to specify the Docker image.")
        print("Example: docksec -i myapp:latest Dockerfile")
        sys.exit(1)
    
    # Run the AI-based recommendation tool
    if run_ai:
        print("Running AI-based Dockerfile analysis...")
        try:
            # Import required modules from main.py
            from utils import (
                get_custom_logger,
                load_docker_file,
                get_llm,
                analyze_security,
                AnalsesResponse,
                ScoreResponse
            )
            from config import docker_agent_prompt, docker_score_prompt
            from pathlib import Path
            
            # Set up the same components as main.py
            logger = get_custom_logger(name='docksec_ai')
            llm = get_llm()
            Report_llm = llm.with_structured_output(AnalsesResponse, method="json_mode")
            analyser_chain = docker_agent_prompt | Report_llm
            
            # Load and analyze the Dockerfile
            filecontent = load_docker_file(docker_file_path=Path(args.dockerfile))
            
            if not filecontent:
                print("Error: No Dockerfile content found.")
                return
            
            response = analyser_chain.invoke({"filecontent": filecontent})
            analyze_security(response)
            
        except ImportError as e:
            print(f"Error: Required modules not found - {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error running AI analysis: {e}")
    
    # Run the scanner tool
    if run_scan:
        print("Running Dockerfile and image scanner...")
        try:
            from docker_scanner import DockerSecurityScanner
            
            # Initialize and run the scanner
            scanner = DockerSecurityScanner(args.dockerfile, args.image)
            results = scanner.run_full_scan("CRITICAL,HIGH")
            
            # Calculate security score
            score = scanner.get_security_score(results)
            
            # Generate all reports
            scanner.generate_all_reports(results)
            
            # Run advanced scan
            print("\n=== Doing Advanced Scan ===")
            scanner.advanced_scan()
            
            print("\n=== Finished Scanning ===")
            
        except ValueError as e:
            print(f"Scanner error: {e}")
        except ImportError as e:
            print(f"Error: Scanner modules not found - {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error running scanner: {e}")
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()