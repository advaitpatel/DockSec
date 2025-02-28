import subprocess
import sys
import json
from typing import Tuple, Optional, Dict, List
import os

from config import RESULTS_DIR

class DockerSecurityScanner:
    def __init__(self, dockerfile_path: str, image_name: str, results_dir: str = RESULTS_DIR):
        """
        Initialize the Docker Security Scanner with a Dockerfile path and image name.
        Verifies that required tools are installed and the specified files exist.
        
        Args:
            dockerfile_path: Path to the Dockerfile to scan
            image_name: Name of the Docker image to scan
        
        Raises:
            ValueError: If required tools are missing or specified files don't exist
        """
        self.dockerfile_path = dockerfile_path
        self.image_name = image_name
        self.required_tools = ['docker', 'hadolint', 'trivy']
        self.RESULTS_DIR = results_dir
        
        # Verify required tools
        missing_tools = self._check_tools()
        if missing_tools:
            raise ValueError(f"Missing required tools: {', '.join(missing_tools)}")
        
        # Verify Dockerfile exists
        if not os.path.exists(dockerfile_path):
            raise ValueError(f"Dockerfile not found at {dockerfile_path}")
        
        # Verify Docker image exists
        try:
            subprocess.run(
                ['docker', 'image', 'inspect', image_name],
                capture_output=True,
                check=True
            )
        except subprocess.CalledProcessError:
            raise ValueError(f"Docker image '{image_name}' not found locally")
            
    def _check_tools(self) -> List[str]:
        """Check if all required tools are installed and return list of missing tools."""
        missing_tools = []
        
        for tool in self.required_tools:
            try:
                subprocess.run([tool, '--version'], capture_output=True, check=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                missing_tools.append(tool)
        
        return missing_tools

    def scan_dockerfile(self) -> Tuple[bool, Optional[str]]:
        """
        Scan Dockerfile using Hadolint.
        
        Returns:
            Tuple containing:
                - bool: True if no issues found, False otherwise
                - Optional[str]: Output from the scan or None if successful
        """
        print("\n=== Starting Dockerfile scan with Hadolint ===")
        try:
            result = subprocess.run(
                ['hadolint', self.dockerfile_path],
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                output = result.stdout if result.stdout else result.stderr
                print("Dockerfile linting issues found:")
                print(output)
                return False, output
            else:
                print("No Dockerfile linting issues found.")
                return True, None
                
        except subprocess.CalledProcessError as e:
            print(f"Error running Hadolint: {e}")
            return False, str(e)
    
    def _filter_scan_results(self, scan_results: Dict) -> List[Dict]:
        """
        Filter Trivy scan results to extract specific vulnerability data.
        
        Args:
            scan_results: The raw Trivy scan results
            
        Returns:
            List of filtered vulnerability data with key information
        """
        filtered_vulnerabilities = []
        
        for result in scan_results.get("Results", []):
            target = result.get("Target", "")
            
            for vulnerability in result.get('Vulnerabilities', []):
                description = vulnerability.get("Description", "")
                if description and len(description) > 150:
                    description = description[:150] + "..."
                
                filtered_vulnerability = {
                    "VulnerabilityID": vulnerability.get("VulnerabilityID"),
                    "Target": target,
                    "PkgName": vulnerability.get("PkgName"),
                    "InstalledVersion": vulnerability.get("InstalledVersion"),
                    "Severity": vulnerability.get("Severity"),
                    "Title": vulnerability.get("Title"),
                    "Description": description,
                    "Status": vulnerability.get("Status"),
                    "CVSS": vulnerability.get("CVSS", {}).get("nvd", {}).get("V3Score"),
                    "PrimaryURL": vulnerability.get("PrimaryURL")
                }
                
                filtered_vulnerabilities.append(filtered_vulnerability)
        
        return filtered_vulnerabilities
    
    def scan_image_json(self, severity: str = "CRITICAL,HIGH") -> Tuple[bool, Optional[List[Dict]]]:
        """
        Scan Docker image using Trivy and return the results as structured data.
        
        Args:
            severity: Comma-separated list of severity levels to scan for
            
        Returns:
            Tuple containing:
                - bool: True if scan completed successfully, False otherwise
                - Optional[List[Dict]]: Filtered vulnerability data or None if scan failed
        """
        print("\n=== Starting vulnerability scan with Trivy ===")
        
        try:
            print(f"Scanning image: {self.image_name}")
            result = subprocess.run(
                [
                    'trivy',
                    'image',
                    '-f', 'json',
                    '--severity', severity,
                    '--no-progress',
                    self.image_name
                ],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            if result.stderr:
                print("Errors:", result.stderr)
            
            response = json.loads(result.stdout)
            filtered_results = self._filter_scan_results(response)
            
            # Check if vulnerabilities were found
            if not filtered_results:
                print("No vulnerabilities found.")
            else:
                print(f"Found {len(filtered_results)} vulnerabilities.")
                
            return True, filtered_results
            
        except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
            print(f"Error running Trivy scan: {e}")
            return False, None

    def scan_image(self, severity: str = "CRITICAL,HIGH") -> Tuple[bool, Optional[str]]:
        """
        Scan Docker image using Trivy and return text output.
        
        Args:
            severity: Comma-separated list of severity levels to scan for
            
        Returns:
            Tuple containing:
                - bool: True if no vulnerabilities found, False otherwise
                - Optional[str]: Output from the scan or None if failed
        """
        print("\n=== Starting vulnerability scan with Trivy ===")
        
        try:
            print(f"Scanning image: {self.image_name}")
            result = subprocess.run(
                [
                    'trivy',
                    'image',
                    '--severity', severity,
                    '--no-progress',
                    self.image_name
                ],
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            
            print("Scan completed.")
            if result.stdout:
                print(result.stdout)
            
            if result.stderr:
                print("Errors:", result.stderr)
            
            # Check if vulnerabilities were found based on return code
            # Trivy returns 0 if no vulnerabilities are found with the specified severity
            return result.returncode == 0, result.stdout
            
        except subprocess.CalledProcessError as e:
            print(f"Error running Trivy scan: {e}")
            return False, str(e)

    def run_full_scan(self, severity: str = "CRITICAL,HIGH") -> Dict:
        """
        Run all security scans and return results.
        
        Args:
            severity: Comma-separated list of severity levels to scan for
            
        Returns:
            Dictionary containing scan results
        """
        scan_status = True
        results = {
            'dockerfile_scan': {
                'success': False,
                'output': None
            },
            'image_scan': {
                'success': False,
                'output': None
            },
            'json_data': None
        }

        # Run Dockerfile scan
        dockerfile_success, dockerfile_output = self.scan_dockerfile()
        results['dockerfile_scan']['success'] = dockerfile_success
        results['dockerfile_scan']['output'] = dockerfile_output
        if not dockerfile_success:
            scan_status = False

        # Run image vulnerability scan
        image_success, image_output = self.scan_image(severity)
        results['image_scan']['success'] = image_success
        results['image_scan']['output'] = image_output
        if not image_success:
            scan_status = False

        # Get JSON data
        json_success, json_data = self.scan_image_json(severity)
        if json_success:
            results['json_data'] = json_data

        # Print final summary
        print("\n=== Scan Summary ===")
        if scan_status:
            print("All security scans completed successfully with no issues found.")
        else:
            print("Some security scans failed or found issues. Please review the results above.")

        return results

    def save_results_to_file(self, results: Dict) -> None:
        """
        Save scan results to a JSON file.
        
        Args:
            results: The scan results to save
            output_file: The file to save results to
        """
        output_file = os.path.join(self.RESULTS_DIR, "scan_results.json")
        
        try:
            with open(output_file, "w") as f:
                json.dump(results, f, indent=4)
            print(f"Results saved to {output_file}")
        except Exception as e:
            print(f"Error saving results to file: {e}")


def main():
    """Main function to run the security scanner."""
    if len(sys.argv) < 3:
        print("Usage: python docker_scanner.py <dockerfile_path> <image_name> [severity] [output_file]")
        print("Example: python docker_scanner.py ./Dockerfile myapp:latest CRITICAL,HIGH results.json")
        sys.exit(1)

    dockerfile_path = sys.argv[1]
    image_name = sys.argv[2]
    severity = sys.argv[3] if len(sys.argv) > 3 else "CRITICAL,HIGH"
    # output_file = sys.argv[4] if len(sys.argv) > 4 else "results/scan_results.json"
    
    try:
        # Initialize scanner with verification
        scanner = DockerSecurityScanner(dockerfile_path, image_name)
        
        # Run full scan
        results = scanner.run_full_scan(severity)
        
        # Save results to file
        scanner.save_results_to_file(results)
        
        # Exit with appropriate code
        if results['dockerfile_scan']['success'] and results['image_scan']['success']:
            sys.exit(0)
        else:
            sys.exit(1)
            
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()