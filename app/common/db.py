from mysql.connector import connect, errorcode

from common import CREATE_USER_PROC
from .secret_reader import read_secrets

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

    def _call_proc(self, stored_proc: str, values: tuple) -> str:
        """Calls stored procedures

        Args:
            stored_proc (str): The stored procedure name
            values (tuple): The args to pass to the stored procedure

        Returns:
            str: The returned result or an Error message

        """
        try:

            call = self.cursor.callproc(stored_proc, values,)
            self._db_conn.commit()

        except Exception as ex:
            return str(ex)

        return call

    def put(self, stored_proc: str, values: tuple) -> str:
        """The put method exposed to Flask. Allows inserts into DB

        Args:
            stored_proc (str): The stored procedure name
            values (tuple): The args to pass to the stored procedure

        Returns:
            str: The returned result or an Error message

        """
        if stored_proc.lower() == CREATE_USER_PROC:
            return "DENIED"

        return self._call_proc(stored_proc, values)

    def create_user(self, values: tuple) -> str:
        """This will not be exposed to flask, local user creation only

        Args:
            values (tuple): The args to pass to the stored procedure

        Returns:
            str: The returned result or an Error message

        """
        return self._call_proc(CREATE_USER_PROC, values)
