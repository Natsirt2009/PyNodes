from pynodes import PyNodes, PyNodeFrame, INode
import tkinter as tk
from tkinter import ttk
def main():
    nodes = PyNodes("data")
    root = tk.Tk()
    root.title("PyNode Editor")
    root.geometry("800x600")
    treeview = ttk.Treeview()
    treeview.pack(side="left", fill= "y")
    for node in nodes.getTypeList(INode.getName()):
        if node.getGroup() not in treeview.get_children():
            treeview.insert("", tk.END, text=node.getGroup(), iid=node.getGroup())
        treeview.insert(node.getGroup(), tk.END, text=node.getTitle())
    nodeFrame = PyNodeFrame(root)
    nodeFrame.pack(fill= "both", side= "right", expand= True)

    root.mainloop()


if __name__ == '__main__':
    main()