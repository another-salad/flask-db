from mysql.connector import connect, errorcode

from secrets import read_secrets

INSTANCE_NAME = "db"  # From docker-compose file
DB_NAME = "local_db"
DB_PORT = "3306"
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
        self.db_conn = connect(**self.db_config)
        self.cursor = self.db_conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Closes cursor and DB connection"""
        self.cursor.close()
        self.db_conn.close()


class DBHandler(DBConn):

    def __init__(self) -> None:
        super().__init__()

    def read_table(self):  # Just testing it actually works...
        data = self.cursor
        data.execute("SELECT * FROM default_server_active_user_log")
        result = data.fetchall()
        print(result)

if __name__ == "__main__":
    with DBHandler() as db:
        print(db.read_table())
