import tkinter as tk

from .Type import Type
from .annotators import todo
from .AObject import AObject

@todo
class Node(tk.Frame, AObject):
    class Input:
        def __init__(self, typename: str, typegroup: str, name: str):
            self.name = name
            self.typename = typename
            self.typegroup = typegroup

            self.type: Later[Type] = Later()
            # Somwhere else, later in programm flow
            Later.build(self.type, arg)
            self.type.doStuff() # Das soll quasi von dem later object getunnelt werden


    def __init__(self, master, title: str, color: str, outputs: list, inputs: list):
        super().__init__(master)
        self.base_width = 100
        self.base_height = (20 + len(outputs)*20 + len(inputs)*20)
        self.config(width=self.base_width, height=self.base_height, bg="#404040", highlightbackground="#000000", highlightthickness=3)
        self.current_scale = 1.0
        self.pack_propagate(False)
        self.title_bar = tk.Frame(self, background=color, height=20)
        self.title_bar.pack(side="top", fill="x")
        self.title_bar.pack_propagate(False)
        self.title_label = tk.Label(self.title_bar, text=title, fg="#FFFFFF", bg=color, anchor="w")
        self.base_font_size = 10
        self.base_padx = 5
        self.title_label.pack(fill="both", padx=self.base_padx)
        self.title_label.config(font=("Arial", self.base_font_size))

    def scale(self, factor: float) -> None:
        self.current_scale *= factor
        new_w = int(self.base_width * self.current_scale)
        new_h = int(self.base_height * self.current_scale)
        new_font_size = max(int(self.base_font_size * self.current_scale), 1)
        new_padx = max(int(self.base_padx * self.current_scale), 1)
        title_height = int(20 * self.current_scale)
        self.config(width=new_w, height=new_h)
        self.title_bar.config(height=title_height)
        self.title_label.config(font=("Arial", new_font_size))
        self.title_label.pack_configure(padx=new_padx)
    @staticmethod
    def getType() -> str:
        return "node"