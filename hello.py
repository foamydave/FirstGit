from tkinter import *
from lib import *

root = Tk()
 
w = Label(root, text="Hello, "+ getPerson() +"!")
w.pack()
 
root.mainloop()
