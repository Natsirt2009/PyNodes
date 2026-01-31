import tkinter as tk
from .dataStructure.todo import todo

@todo
class PyNodeFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="#CCC")