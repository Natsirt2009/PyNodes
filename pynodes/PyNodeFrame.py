import tkinter as tk

from .dataStructure import IPyNodesRenderer
from .Node import Node
from .annotators import todo
from .PyNodes import PyNodes

@todo
class PyNodeFrame(tk.Frame, IPyNodesRenderer):
    def __init__(self, master, nodes: PyNodes):
        super().__init__(master)
        self.availNodes = nodes
        self.nodes: list[Node] = []
        self.scale = 1.0  # current zoom level
        self.canvas = tk.Canvas(self, bg="gray20")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<ButtonPress-3>", self._pan_start)
        self.canvas.bind("<B3-Motion>", self._pan_move)
        self.canvas.bind("<MouseWheel>", self._zoom)

    def _zoom(self, event) -> None:
        if event.num == 4 or event.delta > 0:
            factor = 1.1
        elif event.num == 5 or event.delta < 0:
            factor = 0.9
        else:
            return
        self.scale *= factor
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        x_mouse = self.canvas.canvasx(event.x)
        y_mouse = self.canvas.canvasy(event.y)
        for node in self.nodes:
            x, y = self.canvas.coords(node.window_id)
            new_x = x_mouse + (x - x_mouse) * factor
            new_y = y_mouse + (y - y_mouse) * factor
            self.canvas.coords(node.window_id, new_x, new_y)
            node.scale(factor)
        self.canvas.scale("all", x, y, factor, factor)
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

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