import os
import json
import subprocess
import csv
import pandas as pd
from typing import List, Tuple, Dict, Optional
from datetime import datetime
from fpdf import FPDF
import sys
import re
from config import RESULTS_DIR
from config import docker_score_prompt
from utils import ScoreResponse, get_llm, print_section

class DockerSecurityScanner:
    def __init__(self, dockerfile_path: str, image_name: str, results_dir: str = RESULTS_DIR):
        """
        Initialize the Docker Security Scanner with a Dockerfile path and image name.
        Verifies that required tools are installed and the specified files exist.
        
        Args:
            dockerfile_path: Path to the Dockerfile to scan
            image_name: Name of the Docker image to scan
            results_dir: Directory to store scan results
        
        Raises:
            ValueError: If required tools are missing or specified files don't exist
        """
        self.dockerfile_path = dockerfile_path
        self.image_name = image_name
        # self.required_tools = ['docker', 'hadolint', 'trivy']
        self.required_tools = ['docker', 'trivy']
        if dockerfile_path:
            self.required_tools.append('hadolint')
        
        self.RESULTS_DIR = results_dir
        llm = get_llm()
        self.score_chain = docker_score_prompt | llm.with_structured_output(ScoreResponse, method="json_mode")
        
        # Ensure results directory exists
        os.makedirs(self.RESULTS_DIR, exist_ok=True)
        

        # Verify required tools
        missing_tools = self._check_tools()
        if missing_tools:
            raise ValueError(f"Missing required tools: {', '.join(missing_tools)}")
        
        # Verify Dockerfile exists
        if dockerfile_path and not os.path.exists(dockerfile_path):
            raise ValueError(f"Dockerfile not found at {dockerfile_path}")
        
        # Verify Docker image exists
        try:
            subprocess.run(
                ['sudo','docker', 'image', 'inspect', image_name],
                capture_output=True,
                check=True
            )
        except subprocess.CalledProcessError:
            raise ValueError(f"Docker image '{image_name}' not found locally")
    def run_image_only_scan(self, severity: str = "CRITICAL,HIGH") -> Dict:
        """
        Run image-only security scan without Dockerfile analysis.
        
        Args:
            severity: Comma-separated list of severity levels to scan for
            
        Returns:
            Dictionary containing scan results
        """
        print(f"\n=== Starting image-only scan for {self.image_name} ===")
        
        results = {
            'dockerfile_scan': {
                'success': True,  # Skip Dockerfile scan
                'output': "Skipped - Image-only scan mode",
                'skipped': True
            },
            'image_scan': {
                'success': False,
                'output': None
            },
            'json_data': None,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'image_name': self.image_name,
            'dockerfile_path': self.dockerfile_path or "N/A - Image-only scan",
            'scan_mode': 'image_only'
        }

        # Run image vulnerability scan
        image_success, image_output = self.scan_image(severity)
        results['image_scan']['success'] = image_success
        results['image_scan']['output'] = image_output

        # Get JSON data for vulnerabilities
        json_success, json_data = self.scan_image_json(severity)
        if json_success:
            results['json_data'] = json_data

        # Print final summary
        print("\n=== Image-Only Scan Summary ===")
        if image_success and not json_data:
            print("Image scan completed successfully with no vulnerabilities found.")
        elif json_data:
            print(f"Image scan completed. Found {len(json_data)} vulnerabilities.")
        else:
            print("Image scan encountered issues. Please review the results above.")

        return results 
          
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
        print("\n=== Starting vulnerability scan with Trivy for Json Output ===")
        
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

    def advanced_scan(self) -> Dict:

        try:
            # Running Docker Scout quick scan
            result = subprocess.run(
                ["docker", "scout", "quickview", self.image_name], 
                capture_output=True, text=True, check=True
            )
            print(f"Scan results for {self.image_name}:\n")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error running Docker Scout: {e.stderr}")
            return 0
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
            'json_data': None,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'image_name': self.image_name,
            'dockerfile_path': self.dockerfile_path
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

    def save_results_to_json(self, results: Dict) -> str:
        """
        Save scan results to a JSON file.
        
        Args:
            results: The scan results to save
            
        Returns:
            Path to the saved JSON file
        """
        output_file = os.path.join(self.RESULTS_DIR, f"{re.sub(r'[:/.\-]', '_', self.image_name)}_scan_results.json")

        json_results = results.get('json_data', [])
        vulnerabilities = {
            "scan_info": {
                "image": self.image_name,
                "dockerfile": self.dockerfile_path,
                "scan_time": results.get('timestamp', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            },
            "vulnerabilities": json_results
        }
        
        try:
            with open(output_file, "w") as f:
                json.dump(vulnerabilities, f, indent=4)
            print(f"JSON results saved to {output_file}")
            return output_file
        except Exception as e:
            print(f"Error saving results to JSON file: {e}")
            return ""

    def save_results_to_csv(self, results: Dict) -> str:
        """
        Save vulnerability scan results to a CSV file.
        
        Args:
            results: The scan results to save
            
        Returns:
            Path to the saved CSV file
        """
        output_file = os.path.join(self.RESULTS_DIR, f"{re.sub(r'[:/.\-]', '_', self.image_name)}_vulnerabilities.csv")
        
        vulnerabilities = results.get('json_data', [])
        if not vulnerabilities:
            print("No vulnerability data to save to CSV")
            return ""
        
        try:
            # Define CSV columns
            fieldnames = [
                "VulnerabilityID", "Severity", "PkgName", "InstalledVersion", 
                "Title", "Description", "CVSS", "Status", "Target", "PrimaryURL"
            ]
            
            with open(output_file, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                for vuln in vulnerabilities:
                    # Only write the fields we care about
                    filtered_vuln = {k: vuln.get(k, "") for k in fieldnames}
                    writer.writerow(filtered_vuln)
                    
            print(f"CSV results saved to {output_file}")
            return output_file
        except Exception as e:
            print(f"Error saving results to CSV file: {e}")
            return ""
    
    def save_results_to_pdf(self, results: Dict) -> str:
        """
        Save scan results to a PDF file with formatting.
        Handles both full scans and image-only scans.
        
        Args:
            results: The scan results to save
            
        Returns:
            Path to the saved PDF file
        """
        output_file = os.path.join(self.RESULTS_DIR, f"{re.sub(r'[:/.\-]', '_', self.image_name)}_security_report.pdf")
        
        try:
            # Create custom PDF class with text wrapping capability
            class PDF(FPDF):
                def __init__(self):
                    super().__init__()
                    self.set_auto_page_break(True, margin=15)
                
                def multi_cell_with_title(self, title, content, title_w=40):
                    """Create a title-content pair with the content potentially spanning multiple lines"""
                    self.set_font('Arial', 'B', 10)
                    x_start = self.get_x()
                    y_start = self.get_y()
                    self.cell(title_w, 7, title)
                    self.set_font('Arial', '', 10)
                    self.set_xy(x_start + title_w, y_start)
                    self.multi_cell(0, 7, content)
                    self.ln(2)
                
                def add_section_header(self, title):
                    """Add a section header"""
                    self.set_font('Arial', 'B', 12)
                    self.cell(0, 10, title, 0, 1)
                    self.ln(2)
            
            # Create PDF instance
            pdf = PDF()
            pdf.add_page()
            
            # Add title
            pdf.set_font('Arial', 'B', 16)
            scan_mode = results.get('scan_mode', 'full')
            title = f'Docker Security Scan Report ({scan_mode.upper()})'
            pdf.cell(0, 10, title, 0, 1, 'C')
            pdf.ln(5)
            
            # Add scan information section
            pdf.add_section_header('Scan Information')
            pdf.multi_cell_with_title('Image:', self.image_name)
            pdf.multi_cell_with_title('Scan Mode:', scan_mode.replace('_', ' ').title())
            pdf.multi_cell_with_title('Dockerfile:', results.get('dockerfile_path', 'N/A'))
            pdf.multi_cell_with_title('Scan Date:', results.get('timestamp', ''))
            pdf.ln(5)
            
            # Add image information if available (for extended scans)
            if 'image_info' in results:
                pdf.add_section_header('Image Information')
                image_info = results['image_info']
                
                if image_info.get('size'):
                    size_mb = round(image_info['size'] / (1024*1024), 2)
                    pdf.multi_cell_with_title('Size:', f"{size_mb} MB")
                
                if image_info.get('created'):
                    pdf.multi_cell_with_title('Created:', image_info['created'][:19])  # Truncate timestamp
                
                if image_info.get('architecture'):
                    pdf.multi_cell_with_title('Architecture:', image_info['architecture'])
                
                if image_info.get('os'):
                    pdf.multi_cell_with_title('OS:', image_info['os'])
                
                pdf.ln(5)
            
            # Add configuration analysis if available
            if 'config_analysis' in results:
                pdf.add_section_header('Configuration Analysis')
                config_analysis = results['config_analysis']
                
                # Count issues
                high_count = len(config_analysis.get('high_risk', []))
                medium_count = len(config_analysis.get('medium_risk', []))
                low_count = len(config_analysis.get('low_risk', []))
                total_count = high_count + medium_count + low_count
                
                pdf.multi_cell_with_title('Total Issues:', str(total_count))
                if high_count > 0:
                    pdf.multi_cell_with_title('High Risk:', str(high_count))
                if medium_count > 0:
                    pdf.multi_cell_with_title('Medium Risk:', str(medium_count))
                if low_count > 0:
                    pdf.multi_cell_with_title('Low Risk:', str(low_count))
                
                # Add issue details
                if high_count > 0:
                    pdf.ln(3)
                    pdf.set_font('Arial', 'B', 10)
                    pdf.cell(0, 7, 'High-Risk Issues:', 0, 1)
                    pdf.set_font('Arial', '', 9)
                    for issue in config_analysis['high_risk']:
                        pdf.multi_cell(0, 5, f"• {issue}")
                
                if medium_count > 0:
                    pdf.ln(3)
                    pdf.set_font('Arial', 'B', 10)
                    pdf.cell(0, 7, 'Medium-Risk Issues:', 0, 1)
                    pdf.set_font('Arial', '', 9)
                    for issue in config_analysis['medium_risk']:
                        pdf.multi_cell(0, 5, f"• {issue}")
                
                if low_count > 0:
                    pdf.ln(3)
                    pdf.set_font('Arial', 'B', 10)
                    pdf.cell(0, 7, 'Low-Risk Issues:', 0, 1)
                    pdf.set_font('Arial', '', 9)
                    for issue in config_analysis['low_risk']:
                        pdf.multi_cell(0, 5, f"• {issue}")
                
                pdf.ln(5)
            
            # Add Dockerfile scan results (only if not skipped)
            if not results['dockerfile_scan'].get('skipped', False):
                pdf.add_section_header('Dockerfile Scan Results')
                
                if results['dockerfile_scan']['success']:
                    pdf.set_font('Arial', '', 10)
                    pdf.cell(0, 7, 'No Dockerfile linting issues found.', 0, 1)
                else:
                    pdf.set_font('Arial', '', 10)
                    pdf.cell(0, 7, 'Dockerfile linting issues:', 0, 1)
                    pdf.ln(2)
                    pdf.set_font('Courier', '', 8)
                    
                    if results['dockerfile_scan']['output']:
                        for line in results['dockerfile_scan']['output'].split('\n')[:20]:  # Limit lines
                            pdf.multi_cell(0, 5, line)
                
                pdf.ln(5)
            
            # Add vulnerability scan summary (rest remains the same)
            pdf.add_section_header('Vulnerability Scan Summary')
            vulnerabilities = results.get('json_data', [])
            
            if not vulnerabilities:
                pdf.set_font('Arial', '', 10)
                pdf.cell(0, 7, 'No vulnerabilities found.', 0, 1)
            else:
                # Count vulnerabilities by severity
                severity_counts = {}
                for vuln in vulnerabilities:
                    severity = vuln.get('Severity', 'UNKNOWN')
                    severity_counts[severity] = severity_counts.get(severity, 0) + 1
                
                pdf.set_font('Arial', '', 10)
                pdf.cell(0, 7, f'Total vulnerabilities: {len(vulnerabilities)}', 0, 1)
                
                for severity, count in severity_counts.items():
                    pdf.cell(0, 7, f'{severity}: {count}', 0, 1)
                
                pdf.ln(5)
                
                # Add limited vulnerability details table
                if len(vulnerabilities) > 0:
                    pdf.add_section_header('Top Vulnerabilities')
                    
                    # Show top 20 vulnerabilities
                    for i, vuln in enumerate(vulnerabilities[:20]):
                        if pdf.get_y() > pdf.h - 40:  # Check if near bottom
                            pdf.add_page()
                        
                        pdf.set_font('Arial', 'B', 9)
                        pdf.cell(0, 6, f"{i+1}. {vuln.get('VulnerabilityID', 'N/A')} ({vuln.get('Severity', 'N/A')})", 0, 1)
                        
                        pdf.set_font('Arial', '', 8)
                        pdf.multi_cell(0, 4, f"Package: {vuln.get('PkgName', 'N/A')} ({vuln.get('InstalledVersion', 'N/A')})")
                        
                        title = vuln.get('Title', '')
                        if title:
                            pdf.multi_cell(0, 4, f"Title: {title[:100]}{'...' if len(title) > 100 else ''}")
                        
                        pdf.ln(2)
                    
                    if len(vulnerabilities) > 20:
                        pdf.ln(3)
                        pdf.set_font('Arial', 'I', 9)
                        pdf.cell(0, 5, f'Showing 20 of {len(vulnerabilities)} vulnerabilities. See CSV/JSON for complete list.', 0, 1)
            
            # Save the PDF
            pdf.output(output_file)
            print(f"PDF report saved to {output_file}")
            return output_file
            
        except Exception as e:
            print(f"Error saving results to PDF file: {e}")
            return ""
        
    def generate_all_reports(self, results: Dict) -> Dict:
        """
        Generate all report formats (JSON, CSV, PDF) from scan results.
        
        Args:
            results: The scan results to save
            
        Returns:
            Dictionary with paths to the generated reports
        """
        report_paths = {
            'json': '',
            'csv': '',
            'pdf': ''
        }
        
        # Save to JSON
        json_path = self.save_results_to_json(results)
        if json_path:
            report_paths['json'] = json_path
        
        # Save to CSV
        csv_path = self.save_results_to_csv(results)
        if csv_path:
            report_paths['csv'] = csv_path
        
        # Save to PDF
        pdf_path = self.save_results_to_pdf(results)
        if pdf_path:
            report_paths['pdf'] = pdf_path
        
        return report_paths
    
    def get_security_score(self, results: Dict) -> float:
        """
        Calculate the security score based on scan results.
        
        Args:
            results: The scan results to calculate the score from
            
        Returns:
            The calculated security score
        """

        score = self.score_chain.invoke({"results": results})
        print(f"Security Score: {score.score}")
        return score.score

    

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
        
        # Calculate security score
        score = scanner.get_security_score(results)

        print_section("Security Score", [f"Score: {score}"], "yellow")

        # Save results to file
        scanner.generate_all_reports(results)

        print("\n=== Doing Advanced Scan ===")
        
        # Run advanced scan
        scanner.advanced_scan()

        print("\n=== Finished Scanning ===")
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