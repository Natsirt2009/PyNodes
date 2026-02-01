import tkinter as tk
from .Node import Node
from .annotators import todo
from .PyNodes import PyNodes

@todo
class PyNodeFrame(tk.Frame):
    def __init__(self, master, nodes: PyNodes):
        super().__init__(master)
        self.availNodes = nodes
        self.nodes: list[Node] = []
        self.canvas = tk.Canvas(self, bg="gray20")
        self.canvas.pack(fill="both", expand=True)

        # example panning bindings
        self.canvas.bind("<ButtonPress-3>", self._pan_start)
        self.canvas.bind("<B3-Motion>", self._pan_move)

    def _pan_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def _pan_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def createNode(self, name: str, group: str) -> None:
        n = self.availNodes.create(Node, name, group, self)
        self.nodes.append(n)
        n.window_id = self.canvas.create_window(
            0, 0,
            window=n,
            anchor="nw"
        )