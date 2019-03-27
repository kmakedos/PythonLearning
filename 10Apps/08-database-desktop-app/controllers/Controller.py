''' Observer pattern for changes in db
'''
from models.BookDAO import BookDAO
from views.Gui import Gui
from views.GuiListener import GuiListener

class Controller(GuiListener):

    def __init__(self, bookdao, gui):
        self.bookDAO = bookdao
        self.gui = gui

    def start(self):
        self.gui.start()

    def gui_event_performed(self, event_type, event_data):
        if event_type == 'FETCH_ALL':
            self.gui.update_listbox_items(self.bookDAO.fetch_all())
        if event_type == 'UPDATE':
            self.bookDAO.update_book(event_data)
        if event_type == 'DELETE':
            self.bookDAO.delete_book(event_data)
        if event_type == 'INSERT':
            self.bookDAO.add_book(event_data)
        if event_type == 'SEARCH':
            self.gui.update_listbox_items(self.bookDAO.search(event_data))

