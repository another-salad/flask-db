from bcrypt import hashpw, checkpw, gensalt


def hasher(string: str) -> str:
    """Hashes a string with a salty salt, default encoding of utf-8 (we live in a modern world)

    Args:
        string (str): The string to hash.

    Returns:
        str: The hashed string
    """
    return hashpw(str(string).encode('utf8'), gensalt(rounds=15))


def validate_pw(plain_string: str, hashed_string: str) -> bool:
    """
    Validates password against a hashed_string from the DB

    Args:
        plain_string (str): the provided string
        hashed_string (str): a pre-generated hashed string

    Returns:
        bool: True if strings match else False
    """
    return checkpw(password=str(plain_string).encode('utf8'), hashed_password=hashed_string.encode('utf8'))
