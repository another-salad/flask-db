"""Unit tests for the docker secret reader"""

from unittest import mock, TestCase

from secret_reader import read_secrets


# pylint: disable=W0613
class TestCaseReadDockerSecrets(TestCase):
    """Test cases for the 'read_secrets' function in secret_reader.py"""

    open_builtin = "builtins.open"

    @mock.patch(open_builtin, new_callable=mock.mock_open, read_data="\nhello\n\n")
    def test_ignore_newlines(self, mock_file):
        """Tests that newline characters are stripped from the file"""
        test_file_name = "test"
        return_text = read_secrets([test_file_name])
        self.assertEqual(return_text[test_file_name], "hello")

    @mock.patch(open_builtin, new_callable=mock.mock_open, read_data="test")
    def test_mutliple_files(self, mock_file):
        """Tests that all files from the input list are opened and returned"""
        expected_result = {"test1": "test", "test2": "test"}
        return_result = read_secrets(list(expected_result.keys()))
        self.assertEqual(expected_result, return_result)
