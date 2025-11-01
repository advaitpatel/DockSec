"""Unit tests for utility functions."""
import unittest
import os
import tempfile
from unittest.mock import patch, Mock

# Import after mocking external dependencies
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestUtils(unittest.TestCase):
    """Test cases for utility functions."""
    
    def test_get_custom_logger(self):
        """Test logger creation."""
        from utils import get_custom_logger
        
        logger = get_custom_logger('TestLogger')
        self.assertEqual(logger.name, 'TestLogger')
        self.assertEqual(logger.level, 20)  # INFO level
    
    def test_load_docker_file(self):
        """Test Dockerfile loading."""
        from utils import load_docker_file
        
        # Create temporary Dockerfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.dockerfile', delete=False) as f:
            f.write("FROM ubuntu:latest\nRUN echo 'test'")
            temp_path = f.name
        
        try:
            content = load_docker_file(temp_path)
            self.assertIn("FROM ubuntu:latest", content)
            self.assertIn("RUN echo 'test'", content)
        finally:
            os.unlink(temp_path)
    
    def test_load_docker_file_not_found(self):
        """Test Dockerfile loading when file doesn't exist."""
        from utils import load_docker_file
        
        result = load_docker_file("/nonexistent/path/Dockerfile")
        self.assertIsNone(result)
    
    @patch('utils.get_openai_api_key')
    @patch('utils.ChatOpenAI')
    def test_get_llm(self, mock_chatopenai, mock_api_key):
        """Test LLM initialization."""
        from utils import get_llm
        
        mock_api_key.return_value = "test-api-key"
        mock_llm_instance = Mock()
        mock_chatopenai.return_value = mock_llm_instance
        
        llm = get_llm()
        
        mock_chatopenai.assert_called_once()
        self.assertIsNotNone(llm)
    
    @patch('utils.get_openai_api_key')
    def test_get_llm_no_api_key(self, mock_api_key):
        """Test LLM initialization without API key."""
        from utils import get_llm
        
        mock_api_key.side_effect = EnvironmentError("API key not found")
        
        with self.assertRaises(EnvironmentError):
            get_llm()


if __name__ == '__main__':
    unittest.main()

