from hashlib import sha512

def hasher(string: str, salt: str, encoding: str = 'utf-8') -> str:
    """Hashes a string with a salty salt, default encoding of utf-8 (we live in a modern world)

    Args:
        string (str): The string to hash.
        salt (str): Some additional salt.
        encoding (str, optional): Defaults to 'utf-8'.

    Returns:
        str: The hashed string
    """
    return sha512(str(string).encode(encoding) + str(salt).encode(encoding)).hexdigest()
