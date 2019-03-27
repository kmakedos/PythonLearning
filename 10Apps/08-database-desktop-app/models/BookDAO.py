from models.Book import Book
from models.Database import SQLiteDB

class BookDAO(object):

    def __init__(self, dbname):
        self.connection = SQLiteDB(dbname)
        self.initialize()

    def initialize(self):
        SQL = "CREATE TABLE IF NOT EXISTS store(title TEXT, author TEXT, year DATE, ISBN TEXT, UNIQUE(isbn) ON CONFLICT IGNORE)"
        self.connection.execute_sql(SQL)

    def add_book(self, book):
        SQL = "INSERT INTO store VALUES (?,?,?,?)"
        values = (book.title, book.author, book.year, book.isbn)
        self.connection.execute_sql(SQL, values)

    def update_book(self, book):
        SQL = "UPDATE store SET title=?, author=?, year=?, ISBN=? " \
              "WHERE ISBN=?"
        values =  (book.title, book.author, book.year, book.isbn, book.isbn)
        self.connection.execute_sql(SQL, values)

    def delete_book(self, book):
        SQL = "DELETE FROM store WHERE ISBN=?"
        values = (book.isbn)
        self.connection.execute_sql(SQL, values)

    def search(self, book):
        books = []
        SQL = "SELECT * FROM store WHERE "
        values = [ value for value in book.__dict__.values() if value ]
        for property in book.__dict__.keys():
            if (book.__dict__[property]):
                SQL += property + " LIKE '%" + book.__dict__[property] + "%' AND "
        if len(values) > 0: SQL += ' 1=1;'
        rows = self.connection.execute_sql(SQL)
        for row in rows:
            books.append(Book(row[0], row[1], row[2], row[3]))
        return books


    def fetch_all(self):
        books = []
        SQL = "SELECT * FROM store"
        rows = self.connection.execute_sql(SQL)
        for row in rows:
            books.append(Book(row[0], row[1], row[2], row[3]))
        return books

