import tkinter as tk
from .AObject import AObject

class Node(tk.Frame, AObject):
    def __init__(self, master):
        super().__init__(master)
        self.config(width=100, height=100, bg="#F00")

    @staticmethod
    def getType() -> str:
        return "node"