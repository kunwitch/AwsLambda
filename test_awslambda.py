# test_awslambda.py
"""
Tests for AwsLambda module.
"""

import unittest
from awslambda import AwsLambda

class TestAwsLambda(unittest.TestCase):
    """Test cases for AwsLambda class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AwsLambda()
        self.assertIsInstance(instance, AwsLambda)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AwsLambda()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
