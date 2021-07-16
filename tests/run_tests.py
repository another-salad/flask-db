"""Runs pylint and unit tests"""

from unittest import TestLoader, TextTestRunner

from pylint.lint import Run


def discover_and_run(start_dir: str = "/", pattern: str = "test_*.py"):
    """Discovers and runs all unit tests from the specified DIR
    Args:
        start_dir (str, optional): The DIR to scan. Defaults to 'tests/'.
        pattern (str, optional): The naming convention for test files. Defaults to 'test*.py'.
    Returns:
        runner.run: The result of the test cases
    """
    tests = TestLoader().discover(start_dir, pattern=pattern)
    runner = TextTestRunner(verbosity=2)
    return runner.run(tests)


if __name__ == "__main__":
    print("######## UNIT TESTS ########")
    discover_and_run()
    print("######## LINTING ########")
    Run("app/")
