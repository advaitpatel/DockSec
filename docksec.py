#!/usr/bin/env python3

import sys
import os
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Docker Security Analysis Tool')
    parser.add_argument('dockerfile', help='Path to the Dockerfile to analyze')
    parser.add_argument('-i', '--image', help='Docker image ID to scan (optional)')
    parser.add_argument('-o', '--output', help='Output file for the report (default: security_report.txt)')
    parser.add_argument('--ai-only', action='store_true', help='Run only AI-based recommendations')
    parser.add_argument('--scan-only', action='store_true', help='Run only Dockerfile/image scanning')
    
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
    
    # Run the AI-based recommendation tool
    if run_ai:
        print("Running AI-based Dockerfile analysis...")
        # Using list form to avoid shell parsing issues on Windows
        subprocess.run([sys.executable, "main.py", args.dockerfile])
    
    # Run the scanner tool
    if run_scan:
        print("Running Dockerfile and image scanner...")
        output_file = args.output or "security_report.txt"
        image_id = args.image or ""
        
        cmd = [sys.executable, "docker_scanner.py", args.dockerfile]
        if image_id:
            cmd.append(image_id)
        
        subprocess.run(cmd)
    
    print("Analysis complete!")

if __name__ == "__main__":
    main()