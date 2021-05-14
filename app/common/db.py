from mysql.connector import connect

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
DB_PORT = "3306"  # From docker-compose file
DB_UN_FILE = ".user_name"
DB_UN_PW_FILE = ".user_pw"


class DBConn:

    _creds = read_secrets(secret_file_names=[DB_UN_FILE, DB_UN_PW_FILE])

    def __init__(self) -> None:
        self.db_config = {
            "user": self._creds[DB_UN_FILE],
            "password": self._creds[DB_UN_PW_FILE],
            "host": INSTANCE_NAME,  # UPDATE THIS
            "port": DB_PORT,
            "database": DB_NAME
        }

    def __enter__(self):
        """Creates the DB connection and returns the cursor object"""
        self._db_conn = connect(**self.db_config)
        self.cursor = self._db_conn.cursor()
        return self

    def commit(self):
        """Commits actions to DB"""
        self._db_conn.commit()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Closes cursor and DB connection"""
        self.cursor.close()
        self._db_conn.close()


class DBActions(DBConn):

    def __init__(self) -> None:
        super().__init__()

    def _call_proc(self, stored_proc: str, values: tuple = None) -> tuple:
        """Calls stored procedures

        Args:
            stored_proc (str): The stored procedure name
            values (tuple): The args to pass to the stored procedure

        Returns:
            tuple: The returned result or an Exception

        """
        if values:
            return_data =  self.cursor.callproc(stored_proc, values)
        else:
            return_data = self.cursor.callproc(stored_proc)

        stored_res = next((i.fetchall() for i in self.cursor.stored_results()), None)
        if stored_res:
            return_data = stored_res

        return return_data

    def set(self, stored_proc: str, values: tuple) -> tuple:
        """The set method exposed to Flask. Allows inserts into DB

        Args:
            stored_proc (str): The stored procedure name
            values (tuple): The args to pass to the stored procedure

        Returns:
            tuple: The returned result or an Exception

        """
        if stored_proc.lower() == CREATE_USER_PROC:
            return False, "denied"

        cmd = self._call_proc(stored_proc, values)
        self.commit()
        return True, cmd

    def get(self, stored_proc: str, values: tuple = None) -> tuple:
        """The get method exposed to Flask. Gets from DB

        Args:
            stored_proc (str): The stored procedure name
            values (tuple): The args to pass to the stored procedure

        Returns:
            tuple: The returned result or an Exception

        """
        return self._call_proc(stored_proc, values)

    def create_user(self, values: tuple) -> tuple:
        """This will not be exposed to flask, local user creation only

        Args:
            values (tuple): The args to pass to the stored procedure

        Returns:
            tuple: The returned result or an Exception

        """
        cmd = self._call_proc(CREATE_USER_PROC, values)
        self.commit()
        return cmd
