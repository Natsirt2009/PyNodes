from pynodes import PyNodes, PyNodeFrame, INode
import tkinter as tk
from tkinter import ttk
import os

class Application:
    def __init__(self):
        pass

def main():
    project_folder = os.path.join(os.path.split(__file__)[0], "project")
    nodes = PyNodes("data")
    root = tk.Tk()
    root.title("PyNode Editor")
    root.geometry("800x600")
    sidebar = tk.Frame(root)
    sidebar.pack(side="left", fill="y")
    paned = tk.PanedWindow(sidebar, orient=tk.VERTICAL, sashwidth=5)
    paned.pack(fill="y", expand=True)
    treeviewFolders = ttk.Treeview(paned)
    paned.add(treeviewFolders, minsize=100)
    treeviewNodes = ttk.Treeview(paned)
    paned.add(treeviewNodes, minsize=100)
    for node in nodes.getTypeList(INode.getName()):
        if node.getGroup() not in treeviewNodes.get_children():
            treeviewNodes.insert("", tk.END, text=node.getGroup(), iid=node.getGroup())
        treeviewNodes.insert(node.getGroup(), tk.END, text=node.getTitle(), tags=("node", ))
    for f in os.scandir(project_folder):
        treeviewFolders.insert("", tk.END, text=f.name)
    nodeFrame = PyNodeFrame(root, nodes)
    nodeFrame.pack(fill= "both", side= "right", expand= True)
    nodeFrame.createNode("Add", "math")
    root.mainloop()


if __name__ == '__main__':
    main()