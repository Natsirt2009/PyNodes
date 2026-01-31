import tkinter as tk
from .dataStructure.todo import todo

@todo
class Node(tk.Frame):
    def __init__(self, master):
        super().__init__(master)