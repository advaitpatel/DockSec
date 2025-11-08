"""
Security Score Calculator Module

This module handles the calculation of security scores based on scan results.
It uses LLM-based analysis to provide comprehensive security scoring.
"""

import logging
from typing import Dict
from config import docker_score_prompt
from utils import ScoreResponse, get_llm, get_custom_logger

# Initialize logger
logger = get_custom_logger(__name__)


class SecurityScoreCalculator:
    """
    Calculates security scores for Docker images and Dockerfiles.
    
    Uses LLM-based analysis to evaluate security posture based on:
    - Vulnerability severity and count
    - Dockerfile best practices
    - Security misconfigurations
    - CVE scores
    """
    
    def __init__(self):
        """Initialize the security score calculator with LLM chain."""
        logger.info("Initializing SecurityScoreCalculator")
        llm = get_llm()
        self.score_chain = docker_score_prompt | llm.with_structured_output(
            ScoreResponse, 
            method="json_mode"
        )
    
    def calculate_score(self, results: Dict) -> float:
        """
        Calculate the security score based on scan results.
        
        This method analyzes:
        - Dockerfile scan results (linting issues)
        - Image vulnerability scan results
        - Vulnerability severities and counts
        - Overall security posture
        
        Args:
            results: Dictionary containing scan results with keys:
                - 'dockerfile_scan': Dockerfile linting results
                - 'image_scan': Image vulnerability results
                - 'json_data': Structured vulnerability data
                - 'timestamp': Scan timestamp
                - 'image_name': Docker image name
                - 'dockerfile_path': Path to Dockerfile
        
        Returns:
            float: Security score between 0-100 (higher is better)
            
        Raises:
            Exception: If LLM call fails or score calculation errors occur
        """
        logger.info("Calculating security score from scan results")
        
        try:
            # Invoke LLM with scan results
            score_response = self.score_chain.invoke({"results": results})
            score = score_response.score
            
            logger.info(f"Security score calculated: {score}")
            print(f"Security Score: {score}/100")
            
            # Provide contextual feedback based on score
            if score >= 90:
                print("[EXCELLENT] Excellent security posture!")
            elif score >= 70:
                print("[GOOD] Good security, but some improvements recommended")
            elif score >= 50:
                print("[FAIR] Fair security - multiple issues need attention")
            else:
                print("[POOR] Poor security - immediate action required")
            
            return score
            
        except Exception as e:
            logger.error(f"Error calculating security score: {e}", exc_info=True)
            print(f"\n[ERROR] Error calculating security score: {e}")
            print("\nTroubleshooting:")
            print("  1. Check your OpenAI API key and credits")
            print("  2. Verify network connectivity")
            print("  3. Review scan results format")
            # Return a default score in case of error
            logger.warning("Returning default score of 0 due to calculation error")
            return 0.0
    
    def get_score_breakdown(self, results: Dict) -> Dict[str, float]:
        """
        Get a detailed breakdown of the security score by category.
        
        Args:
            results: Scan results dictionary
            
        Returns:
            Dictionary with score breakdown by category:
                - 'dockerfile': Score for Dockerfile quality (0-100)
                - 'vulnerabilities': Score for vulnerability severity (0-100)
                - 'configuration': Score for security configuration (0-100)
                - 'overall': Overall security score (0-100)
        """
        logger.info("Calculating detailed score breakdown")
        
        breakdown = {
            'dockerfile': 0.0,
            'vulnerabilities': 0.0,
            'configuration': 0.0,
            'overall': 0.0
        }
        
        # Calculate Dockerfile score (based on linting results)
        if results.get('dockerfile_scan', {}).get('success', False):
            breakdown['dockerfile'] = 100.0
        else:
            # Deduct based on number of issues (simplified logic)
            output = results.get('dockerfile_scan', {}).get('output', '')
            issue_count = len(output.split('\n')) if output else 0
            breakdown['dockerfile'] = max(0, 100 - (issue_count * 5))
        
        # Calculate vulnerability score
        vulnerabilities = results.get('json_data', [])
        if not vulnerabilities:
            breakdown['vulnerabilities'] = 100.0
        else:
            # Weighted by severity
            critical_count = sum(1 for v in vulnerabilities if v.get('Severity') == 'CRITICAL')
            high_count = sum(1 for v in vulnerabilities if v.get('Severity') == 'HIGH')
            medium_count = sum(1 for v in vulnerabilities if v.get('Severity') == 'MEDIUM')
            low_count = sum(1 for v in vulnerabilities if v.get('Severity') == 'LOW')
            
            # Simplified scoring: deduct more for higher severity
            deduction = (critical_count * 10) + (high_count * 5) + (medium_count * 2) + (low_count * 1)
            breakdown['vulnerabilities'] = max(0, 100 - deduction)
        
        # Configuration score (placeholder - would need actual config analysis)
        breakdown['configuration'] = 75.0  # Default
        
        # Overall score (weighted average)
        breakdown['overall'] = (
            breakdown['dockerfile'] * 0.3 +
            breakdown['vulnerabilities'] * 0.5 +
            breakdown['configuration'] * 0.2
        )
        
        logger.info(f"Score breakdown: {breakdown}")
        return breakdown

