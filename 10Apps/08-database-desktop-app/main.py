import multiprocessing
from views.Gui import Gui
from models.BookDAO import BookDAO
from models.Book import Book
from controllers.Controller import Controller
if __name__ == "__main__":
    gui = Gui()
    bookDAO = BookDAO('main.db')
    #bookDAO.add_book(Book('title1', 'author1', 'year1', '1'))
    #bookDAO.add_book(Book('title2', 'author2', 'year2', '2'))
    #bookDAO.add_book(Book('title3', 'author3', 'year3', '3'))
    controller = Controller(bookDAO, gui)
    gui.add_gui_listener(controller)
    controller.start()
    #row = ("kostas", "kostas_ait", "17/05/1973", "12312")
    #db.insert_row(*row)
   # db.view_all()
    #process1 = multiprocessing.Process(target=Gui)
    #  process2 = multiprocessing.Process(target = Gui)
    #process1.start()
    # process2.start()
    #process1.join()
    # process2.join()
