from unittest import TestCase
from views.Gui import Gui

class TestGui(TestCase):

    def setUp(self):
        self.gui = Gui()


    def tearDown(self):
        self.gui.start()

    def test_update_listbox(self):
        items = ['Alpha', 'Beta']
        self.gui.update_listbox_items(*items)

    def test_update_author_text(self):
        author = "Jules Vern"
        self.gui.update_author_text(author)

    def test_update_isbn_text(self):
        isbn = "327462"
        self.gui.update_isbn_text(isbn)

    def test_update_title_text(self):
        title = "20000 Leagues under the sea"
        self.gui.update_title_text(title)

    def test_update_year_text(self):
        year = "16-6-2022"
        self.gui.update_year_text(year)