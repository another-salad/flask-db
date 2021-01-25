from mysql.connector import connect, errorcode

from secrets import read_secrets

#
# Long term, these probably need a better place to stay
#
# Currently, the db name will need to be edited here, in the .sql files and
# compose file(s). The open port is here and the compose file(s).
#
#

INSTANCE_NAME = "db"  # From docker-compose file
DB_NAME = "local_db"
DB_PORT = "3307"  # From docker-compose file
DB_UN_FILE = ".user_name"
DB_UN_PW_FILE = ".user_pw"


class DBConn:

    _creds = read_secrets(secret_file_names=[DB_UN_FILE, DB_UN_PW_FILE])

    def __init__(self) -> None:
        self.db_config = {
            "user": self._creds[DB_UN_FILE],
            "password": self._creds[DB_UN_PW_FILE],
            "host": "0.0.0.0",  # UPDATE THIS
            "port": DB_PORT,
            "database": DB_NAME
        }

    def __enter__(self):
        """Creates the DB connection and returns the cursor object"""
        self._db_conn = connect(**self.db_config)
        self.cursor = self._db_conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Closes cursor and DB connection"""
        self.cursor.close()
        self._db_conn.close()

class DBActions(DBConn):

    def __init__(self) -> None:
        super().__init__()

    def insert(self, table: str, rows: tuple, values, tuple) -> bool:
        pass

    def delete(self):
        pass

    def select(self):
        pass