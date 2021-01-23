from pathlib import Path

# parent DIR to common /app
mod_path = Path(__file__).parent.parent

def read_secrets() -> dict:
    """Reads the secret files to fetch the username and password for the DB

    Returns:
        dict: The username and password
    """
    pass