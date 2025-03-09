import unittest
from flask import Flask

import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app  


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True


    def test_post_request_with_valid_data(self):
        """Test if POST request with valid data processes correctly."""
        response = self.app.post('/', data={'high': '100', 'low': '90', 'risk': '50'})
        self.assertEqual(response.status_code, 200)  # Adjust based on expected behavior



if __name__ == '__main__':
    unittest.main()
