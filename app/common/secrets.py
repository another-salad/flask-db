from pathlib import Path

# parent DIR to common /app
mod_path = Path(__file__).parent.parent

def read_secrets() -> dict:
    """Reads the secret files to fetch the username and password for the DB

    Returns:
        dict: The DB user's username and password
    """

def read_secrets(secret_file_names: list) -> dict:
    """Reads the file and returns its contents as a string

    Args:
        secret_file_names (list): A list of filenames from the 'secrets' DIR

    Returns:
        dict: {"secret_file_name": "contents"}
    """
    return_dict = {}
    for fi in secret_file_names:
        with open(Path(mod_path, "secrets", fi), "r") as f:
            return_dict.update({fi : f.read()})

    return return_dict
