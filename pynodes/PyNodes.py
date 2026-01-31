from .INode import INode
from .IBlock import IBlock
from .IObject import IObject
import os


class PyNodes:
    def _loadObject(self, module, obj):
        isValidObject = False
        for f in os.scandir(os.path.join(self.path, module, obj)):
            if f.is_file():
                if f.name == "object.xml":
                    isValidObject = True
        if isValidObject:
            obj = IObject.parse(os.path.join(self.path, module, obj))
            if obj.getName() not in self.loadedObjects:
                self.loadedObjects[obj.getName()] = []
            self.loadedObjects[obj.getName()].append(obj)
            print(f"\033[31m[ PYNODES ]\033[0m {obj.getName()} {obj.getTitle()}")
    def _loadModule(self, module):
        for f in os.scandir(os.path.join(self.path, module)):
            if f.is_dir():
                currObject = f.name
                self._loadObject(module, currObject)
    def _loadPath(self):
        for f in os.scandir(self.path):
            if f.is_dir():
                currModule = f.name
                self._loadModule(currModule)
    def __init__(self, path: str):
        self.path = path
        self.loadedObjects: dict[str, list[IObject]] = {}
        self._loadPath()