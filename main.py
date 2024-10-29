import tkinter
from tkinter import *
import node
root = Tk()
root.title("Circuit Sim")
root.geometry('1200x600')
board = Canvas(root, bg="gray", height=400, width=400)
board.place(x=0,y=0)
board.create_line(20,20,40,40)
root.mainloop()