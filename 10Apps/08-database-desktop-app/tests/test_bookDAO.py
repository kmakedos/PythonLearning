import os
from unittest import TestCase
from models.BookDAO import BookDAO
from models.Book import Book


class TestBookDAO(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_path = '08-database-desktop-app/db/test.db'

    @classmethod
    def tearDownClass(cls):
        os.unlink(cls.db_path)

    def setUp(self):
        self.bookDAO = BookDAO(self.db_path)

    def tearDown(self):
        SQL = "DROP TABLE store"
        rows = self.bookDAO.connection.execute_sql(SQL)

    def test_initialize(self):
        SQL = "SELECT * FROM store"
        rows = self.bookDAO.connection.execute_sql(SQL)
        assert(rows != None)

    def test_add_book(self):
        book = Book("From earth to moon", "Jules Vern", "20-9-2020", "SDFD")
        self.bookDAO.add_book(book)
        SQL = "SELECT * FROM store"
        rows = self.bookDAO.connection.execute_sql(SQL)
        assert(rows != None)
        assert(len(rows) == 1)

    def test_fetch_all(self):
        book = Book("From earth to moon", "Jules Vern", "20-9-2020", "SDFD")
        self.bookDAO.add_book(book)
        book = Book("20 thousand leagues", "Jules Vern", "20-9-2021", "SDsFD")
        self.bookDAO.add_book(book)
        books = self.bookDAO.fetch_all()
        assert(books != None)
        assert(len(books) == 2)
        for book in books:
            print(("Title: {0}, Author: {1}, Date: {2}, ISBN: {3}".format(book.title, book.author, book.year, book.isbn)))

