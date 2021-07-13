"""Unit tests for the docker secret reader"""

from unittest import main, TestCase


class TestCaseReadDockerSecrets(TestCase):
    """Test cases for the 'read_secrets' function in secret_reader.py"""

    def test_ignore_newlines(self):
        """Tests that newline characters are stripped from the file"""
        pass
