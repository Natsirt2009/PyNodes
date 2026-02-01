from pynodes import PyNodes, PyNodeFrame, INode
import tkinter as tk
from tkinter import ttk
import os

class Application:
    def buildLayout(self) -> None:
        self.root = tk.Tk()
        self.root.title("PyNode Editor")
        self.root.geometry("800x600")
        self.sidebar = tk.Frame(self.root)
        self.sidebar.pack(side="left", fill="y")
        self.paned = tk.PanedWindow(self.sidebar, orient=tk.VERTICAL, sashwidth=5)
        self.paned.pack(fill="y", expand=True)
        self.treeviewFolders = ttk.Treeview(self.paned)
        self.paned.add(self.treeviewFolders, minsize=100)
        self.treeviewNodes = ttk.Treeview(self.paned)
        self.paned.add(self.treeviewNodes, minsize=100)
    
    def loadImages(self):
        for path, folder, files in os.walk("images"):
            for file in files:
                if file.endswith(".png"):
                    imgpath = (path.removeprefix("images\\").replace("\\", "/") + "/" + file.removesuffix(".png"))
                    img = tk.PhotoImage(file=os.path.join(path, file))
                    self.images[imgpath] = img.subsample(img.width() // 16, img.height() // 16)
                    print(F"[ IMAGE ] {imgpath}")

    def getImageForExtention(self, ext: str) -> tk.PhotoImage:
        if not F'ext/{ext}' in self.images:
            return self.images['ext/unknown_ext']
        return self.images[F'ext/{ext}']

    def getImageForFileFolder(self, f: os.DirEntry):
        if f.is_dir():
            if not F'generic/folder' in self.images:
                return self.images['ext/unknown_ext']
            return self.images['generic/folder']
        elif f.is_file():
            return self.getImageForExtention(str(f.name).split(".")[1])
        else:
            return self.images['ext/unknown_ext']

    def __init__(self):
        self.project_folder = os.path.join(os.path.split(__file__)[0], "project")
        self.nodes = PyNodes("data")
        self.images: dict[str, tk.PhotoImage] = {}
        self.buildLayout()
        self.loadImages()
        for node in self.nodes.getTypeList(INode.getName()):
            if node.getGroup() not in self.treeviewNodes.get_children():
                self.treeviewNodes.insert("", tk.END, text=node.getGroup(), iid=node.getGroup())
            self.treeviewNodes.insert(node.getGroup(), tk.END, text=node.getTitle(), tags=("node", ))
        for f in os.scandir(self.project_folder):
            self.treeviewFolders.insert("", tk.END, text=f.name, image=self.getImageForFileFolder(f))
        self.nodeFrame = PyNodeFrame(self.root, self.nodes)
        self.nodeFrame.pack(fill= "both", side= "right", expand= True)
        self.nodeFrame.createNode("Add", "math")
    def run(self) -> None:
        self.root.mainloop()

def main():
    app = Application()
    app.run()

if __name__ == '__main__':
    main()