"""Creates a user in the local_users DB"""

from argparse import ArgumentParser

from pathlib import Path

from typing import Dict

from bcrypt import gensalt

import os.path
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from common.db import DBActions
from common.hashing import hasher


parser = ArgumentParser(
    description="Creates a new user in the local DB",
    usage="create_db_user.py username password"
)
parser.add_argument("username", type=str, help="The username")
parser.add_argument("password", type=str, help="The password")

def create_user(username: str, password: str):
    """Creates a user in the Users DB (created on first time start up)

    Args:
        username (str): The username (255 char limit)
        password (str): The password (255 char limit)

    """
    salt = gensalt()
    hashed_pw = hasher(string=password, salt=salt)

    # Add user to DB
    with DBActions() as db:
        return db.create_user((username, hashed_pw, salt))

if __name__ == "__main__":
    args = parser.parse_args()
    create_user(args.username, args.password)
