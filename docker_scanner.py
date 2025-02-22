import subprocess
import sys
import json
from typing import Tuple, Optional
import os

class DockerSecurityScanner:
    def __init__(self):
        self.required_tools = ['docker', 'hadolint', 'trivy']
        
    def check_required_tools(self) -> bool:
        """Check if all required tools are installed."""
        missing_tools = []
        
        for tool in self.required_tools:
            try:
                subprocess.run([tool, '--version'], capture_output=True, check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                missing_tools.append(tool)
        
        if missing_tools:
            print(f"Error: Missing required tools: {', '.join(missing_tools)}")
            print("Please install the missing tools and try again.")
            return False
        return True

    def scan_dockerfile(self, dockerfile_path: str) -> Tuple[bool, Optional[str]]:
        """
        Scan Dockerfile using Hadolint.
        Returns: (success_status, output)
        """
        if not os.path.exists(dockerfile_path):
            print(f"Error: Dockerfile not found at {dockerfile_path}")
            return False, None

        print("\n=== Starting Dockerfile scan with Hadolint ===")
        try:
            result = subprocess.run(
                ['hadolint', dockerfile_path],
                capture_output=True,
                text=True
            )
            
            if result.stdout or result.stderr:
                print("Dockerfile linting issues found:")
                output = result.stdout if result.stdout else result.stderr
                print(output)
                return False, output
            else:
                print("No Dockerfile linting issues found.")
                return True, None
                
        except subprocess.CalledProcessError as e:
            print(f"Error running Hadolint: {e}")
            return False, str(e)

    def scan_image(self, image_name: str, severity: str = "CRITICAL,HIGH") -> Tuple[bool, Optional[str]]:
        """
        Scan Docker image using Trivy.
        Returns: (success_status, output)
        """
        print("\n=== Starting vulnerability scan with Trivy ===")
        
        # Check if image exists
        try:
            subprocess.run(
                ['docker', 'image', 'inspect', image_name],
                capture_output=True,
                check=True
            )
        except subprocess.CalledProcessError:
            print(f"Error: Docker image '{image_name}' not found locally")
            return False, None

        # Run Trivy scan
        try:
            print(f"Scanning image: {image_name}")
            result = subprocess.run(
                [
                    'trivy',
                    'image',
                    '--severity', severity,
                    '--no-progress',
                    image_name
                ],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            print(f"Scan completed. with Result {result}")
            print(result.stdout)
            if result.stderr:
                print("Errors:", result.stderr)
            
            # Check if vulnerabilities were found
            if "Total: 0 (CRITICAL: 0, HIGH: 0)" in result.stdout:
                return True, result.stdout
            return False, result.stdout
            
        except subprocess.CalledProcessError as e:
            print(f"Error running Trivy scan: {e}")
            return False, str(e)

    def run_security_scan(self, dockerfile_path: str, image_name: str, severity: str = "CRITICAL,HIGH"):
        """Run all security scans and return results."""
        if not self.check_required_tools():
            sys.exit(1)

        scan_status = True
        results = {
            'dockerfile_scan': None,
            'image_scan': None
        }

        # Run Dockerfile scan
        dockerfile_success, dockerfile_output = self.scan_dockerfile(dockerfile_path)
        if not dockerfile_success:
            scan_status = False
        results['dockerfile_scan'] = dockerfile_output

        # Run image vulnerability scan
        image_success, image_output = self.scan_image(image_name, severity)
        if not image_success:
            scan_status = False
        results['image_scan'] = image_output

        # Print final summary
        print("\n=== Scan Summary ===")
        if scan_status:
            print("All security scans completed successfully.")
        else:
            print("Some security scans failed or found issues. Please review the results above.")

        return results

def main():
    """Main function to run the security scanner."""
    if len(sys.argv) < 3:
        print("Usage: python docker_scanner.py <dockerfile_path> <image_name> [severity]")
        print("Example: python docker_scanner.py ./Dockerfile myapp:latest CRITICAL,HIGH")
        sys.exit(1)

    dockerfile_path = sys.argv[1]
    image_name = sys.argv[2]
    severity = sys.argv[3] if len(sys.argv) > 3 else "CRITICAL,HIGH"

    scanner = DockerSecurityScanner()
    scanner.run_security_scan(dockerfile_path, image_name, severity)

if __name__ == "__main__":
    main()