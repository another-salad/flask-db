"""Creates a user in the local_users DB"""

import hashlib
from typing import Dict

import mysql.connector

from argparse import ArgumentParser

def db_conn():
    pass

def create_user(username: str, password: str, read_only: bool = True, create_users: bool = False):
    """Creates a user in the Users DB (created on first time start up)

    Args:
        username (str): The username (255 char limit)
        password (str): The password (255 char limit)
        read_only (bool): True only has access to read functions, else use can write to db (defaults True)
        create_users (bool): True for the ability to create users, else False (defaults False)

    """
    pass