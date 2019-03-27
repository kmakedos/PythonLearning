'''

'''
import sqlite3


class SQLiteDB(object):
    # Singleton pattern is applied here
    # so a single db instance is used
    __instance = None

    def __new__(cls, dbname):
        if SQLiteDB.__instance is None:
            SQLiteDB.__instance = object.__new__(cls)
        SQLiteDB.__instance.dbname = dbname
        return SQLiteDB.__instance

    def __init__(self, dbname):
        self._conn = sqlite3.connect(dbname)
        self._cursor = self._conn.cursor()

    def execute_sql(self, SQL, params=()):
        try:
            self._cursor.execute(SQL, params)
            self._conn.commit()
            rows = self._cursor.fetchall()
            return rows
        except sqlite3.Error as error:
            print("Database Error: %s" % error)


    def close(self):
        self._conn.close()
