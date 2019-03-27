from tkinter import *
from models.Book import Book
"""
A class to create the gui needed for db desktop application 
using Tkinter
"""

class Gui(object):
    def __init__(self):
        self._window = Tk()
        self._gui_listeners = []
        self._window.geometry("640x400")
        self._font_large = ('Helvetica', '14')
        self._font_small = ('Helvetica', '12')
        self._window.title("Book Management")
        self._books = None
        self._titleLabel = Label(self._window, text="Title:", font=self._font_large, width=7)
        self._titleLabel.grid(row=0, column=0, sticky=W)
        self._titleText = Text(self._window, height=1, width=20, font=self._font_large)
        self._titleText.grid(row=0, column=1, sticky=W, padx=(0, 0))
        self._authorLabel = Label(self._window, text="Author:", font=self._font_large, width=8)
        self._authorLabel.grid(row=0, column=2, sticky=W)
        self._authorText = Text(self._window, height=1, width=20, font=self._font_large)
        self._authorText.grid(row=0, column=3, sticky=W)
        self._yearLabel = Label(self._window, text="Year:", font=self._font_large, width=7)
        self._yearLabel.grid(row=1, column=0, sticky=W)
        self._yearText = Text(self._window, height=1, width=10, font=self._font_large)
        self._yearText.grid(row=1, column=1, sticky=W)
        self._isbnLabel = Label(self._window, text="ISBN:", font=self._font_large, width=7)
        self._isbnLabel.grid(row=1, column=2, sticky=W)
        self._isbnText = Text(self._window, height=1, width=20, font=self._font_large)
        self._isbnText.grid(row=1, column=3, sticky=W)

        self._listLabel = Label(self._window, text="Entries:", font=self._font_large)
        self._listLabel.grid(row=2, column=0, columnspan=4, sticky=W, pady=(10, 0), padx=(10, 0))

        self._scroll = Scrollbar(self._window, orient=VERTICAL)
        self._scroll.grid(row=3, column=2, rowspan=6, sticky=W, padx=0, pady=0, ipady=90)
        self._listBox = Listbox(self._window, yscrollcommand=self._scroll.set, width=30, font=self._font_small)
        self._listBox.grid(row=3, column=0, columnspan=2, rowspan=6, sticky=W, padx=10, pady=(0, 10))
        self._scroll.config(command=self._listBox.yview)

        self._viewAllButton = Button(text="View All", width=20, height=1, font=self._font_small, command=lambda: self.update_listeners('FETCH_ALL',''))
        self._viewAllButton.grid(row=3, column=3)

        self._searchEntryButton = Button(text="Search Entry", width=20, height=1, font=self._font_small,
                                         command = lambda: self.search())
        self._searchEntryButton.grid(row=4, column=3)

        self._addEntryButton = Button(text="Add Entry", width=20, height=1, font=self._font_small,
                                      command=lambda: self.insert_current())
        self._addEntryButton.grid(row=5, column=3)

        self._updateSelectedButton = Button(text="Update Selected", width=20, height=1, font=self._font_small,
                                            command=lambda: self.update_selected(self._listBox.curselection()[0]))
        self._updateSelectedButton.grid(row=6, column=3)

        self._deleteSelectedButton = Button(text="Delete Selected", width=20, height=1, font=self._font_small,
                                            command=lambda: self.delete_selected(self._listBox.curselection()[0]))
        self._deleteSelectedButton.grid(row=7, column=3)

        self._closeButton = Button(text="Close", width=20, height=1, font=self._font_small, command=self.close)
        self._closeButton.grid(row=8, column=3)

        self._listBox.bind('<<ListboxSelect>>', self._on_select)

    def _on_select(self,event):
        w = event.widget
        if w.curselection():
            index = int(w.curselection()[0])
            self.update_title_text(self._books[index].title)
            self.update_author_text(self._books[index].author)
            self.update_year_text(self._books[index].year)
            self.update_isbn_text(self._books[index].isbn)

    def add_gui_listener(self, gui_listener):
        self._gui_listeners.append(gui_listener)

    def update_listeners(self, event_type, event_data):
        for listener in self._gui_listeners:
            listener.gui_event_performed(event_type, event_data)

    def start(self):
        self._window.mainloop()

    def search(self):
        book = Book(self._titleText.get("1.0", 'end-1c'), self._authorText.get("1.0", 'end-1c'),
                   self._yearText.get("1.0", 'end-1c'), self._isbnText.get("1.0", 'end-1c'))
        self.update_listeners('SEARCH', book)

    def update_listbox_items(self, books):
        self._listBox.delete(0,END)
        self._books = books
        for book in self._books:
            self._listBox.insert(END, [book.title, book.author, book.year, book.isbn])
        self._listBox.update()

    def insert_current(self):
        book = Book(self._titleText.get("1.0", 'end-1c'), self._authorText.get("1.0", 'end-1c'),
                   self._yearText.get("1.0", 'end-1c'), self._isbnText.get("1.0", 'end-1c'))
        self._books.append(book)
        self.update_listbox_items(self._books)
        self.update_listeners('INSERT', book)

    def update_selected(self, index):
        book = Book(self._titleText.get("1.0", 'end-1c'), self._authorText.get("1.0", 'end-1c'),
                    self._yearText.get("1.0", 'end-1c'), self._isbnText.get("1.0", 'end-1c'))
        self._books[index] = book
        self.update_listbox_items(self._books)
        self.update_listeners('UPDATE', book)

    def delete_selected(self, index):
        self.update_listeners('DELETE', self._books[index])
        self._books.remove(self._books[index])
        self.update_listbox_items(self._books)


    def update_author_text(self, author):
        self._authorText.delete("1.0",END)
        self._authorText.insert(END, author)
        self._authorText.update()

    def update_title_text(self, title):
        self._titleText.delete("1.0",END)
        self._titleText.insert(END, title)

        self._titleText.update()

    def update_year_text(self, year):
        self._yearText.delete("1.0",END)
        self._yearText.insert(END, year)
        self._yearText.update()

    def update_isbn_text(self, isbn):
        self._isbnText.delete("1.0",END)
        self._isbnText.insert(END, isbn)
        self._isbnText.config(state=DISABLED)
        self._isbnText.update()

    def close(self):
        self._window.destroy()