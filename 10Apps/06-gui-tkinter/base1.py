from tkinter import *

def km_to_miles():
    miles = float(e1_value.get()) * 1.6
    t1.delete(1.0, END)
    t1.insert(END, miles)

window = Tk()
e1_value = StringVar()
button = Button(window, text="Convert KM to Miles",command = km_to_miles)
button.grid(row=0,column=0)
e1 = Entry(window, textvariable = e1_value)
e1.grid(row=0, column=1)
t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)
window.mainloop()
