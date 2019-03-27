import os
from unittest import TestCase
from models.BookDAO import BookDAO
from controllers.Controller import Controller
from models.Book import Book
from views.Gui import Gui

class TestController(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = '08-database-desktop-app/db/test.db'

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.db_path)

    def setUp(self):
        self.gui = Gui()
        self.bookdao = BookDAO('test.db')
        self.controller = Controller(self.bookdao, self.gui)
        self.book = Book("alpha", "beta", "22-2-2022", "32432")

    def tearDown(self):
        SQL = "DROP TABLE store"
        rows = self.bookDAO.connection.execute_sql(SQL)

