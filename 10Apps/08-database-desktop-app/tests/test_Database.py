from unittest import TestCase
from models.Database import SQLiteDB
import os

class TestSQLiteDB(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_path = '08-database-desktop-app/db/test.db'

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.db_path)

    def setUp(self):
        self.db = SQLiteDB(self.db_path)

    def tearDown(self):
        self.db.close()

    def test_createTable(self):
        SQL = "CREATE TABLE IF NOT EXISTS store(title TEXT, author TEXT, year DATE, ISBN TEXT)"
        self.db.execute_sql(SQL)

    def test_insertData(self):
        SQL = "INSERT INTO store VALUES (?,?,?,?)"
        values = ("20 thousand leagues", "Jules Vern", "21-2-1899", "325432435")
        self.db.execute_sql(SQL, values)

    def test_selectData(self):
        SQL = "SELECT * FROM store"
        rows = self.db.execute_sql(SQL)
        for row in rows:
            for item in row:
                print(item)


