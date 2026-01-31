from pynodes import PyNodes, PyNodeFrame
import tkinter as tk
from tkinter import ttk
def main():
    nodes = PyNodes("data")
    root = tk.Tk()
    root.title("PyNode Editor")
    root.geometry("800x600")
    treeview = ttk.Treeview()
    treeview.pack(side="left", fill= "y")

    nodeFrame = PyNodeFrame(root)
    nodeFrame.pack(fill= "both", side= "right", expand= True)

    root.mainloop()


if __name__ == '__main__':
    main()