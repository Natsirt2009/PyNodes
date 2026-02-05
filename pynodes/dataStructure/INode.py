import typing

from ..Type import Type
from ..Node import Node
from .IObject import R, IObject
import xml.etree.ElementTree as ET
from ..annotators import todo, abstract

class INode(IObject[Node]):
    class IPort:
        @abstract
        def __init__(self):
            pass
        @abstract
        def create(self):
            pass
    @todo
    class IInput(IPort):
        def __init__(self, element: ET.Element):
            self.type: str = element.get("type", "unknown")
            self.name: str = element.get("name", "unknown")
            self.typegroup: str = element.get("group", "unkown")
        def getName(self) -> str:
            return self.name
        def getGroup(self) -> str:
            return self.typegroup
        def getTypeName(self) -> str:
            return self.type
        def create(self) -> Node.Input:
            return Node.Input(self.type, self.typegroup, self.name)
    @todo
    class IOutput(IPort):
        def __init__(self, element: ET.Element):
            pass
    @todo
    class IAction:
        def __init__(self, element: ET.Element):
            pass

    @staticmethod
    def getName() -> str:
        return "node"
    @staticmethod
    def parser(xml: ET.ElementTree, group: str) -> 'INode':
        root = xml.getroot()
        title = root.get("title", "UNKNOWN")
        color = root.get("color", "#000000")
        inputs: list[INode.IInput] = []
        outputs: list[INode.IOutput] = []
        action: INode.IAction = []
        for sub in root:
            match sub.tag:
                case 'input':
                    inputs.append(INode.IInput(sub))
                case 'output':
                    outputs.append(INode.IOutput(sub))
                case 'action':
                    action = INode.IAction(sub)
        return INode(group, inputs, outputs, action, title, color)

    def __init__(self, group:str, inputs: list['INode.IInput'], outputs: list['INode.IOutput'], action: 'INode.IAction', title: str, color: str):
        self.inputs = inputs
        self.outputs = outputs
        self.title = title
        self.action = action
        self.group = group
        self.color = color

    def getTitle(self) -> str:
        return self.title
    
    def getGroup(self) -> str:
        return self.group
    
    def create(self, master) -> Node:
        createdInputs:  list[Node.Input]  = [input.create() for input in self.inputs]
        createdOutputs: list[Node.Output] = [output.create() for output in self.inputs]
        return Node(master, self.title, self.color, createdInputs, createdOutputs)
