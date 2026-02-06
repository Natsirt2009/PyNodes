import typing

from .IPyNodes import IPyNodes
from .IPyNodesRenderer import IPyNodesRenderer
from ..Node import Node
from .IObject import IObject
import xml.etree.ElementTree as ET
from ..annotators import todo, abstract

TP = typing.TypeVar("TP")

class INode(IObject[Node]):
    class IPort(typing.Generic[TP]):
        @abstract
        def __init__(self):
            pass
        @abstract
        def create(self) -> TP:
            pass
    @todo
    class IInput(IPort[Node.Input]):
        def __init__(self, element: ET.Element):
            self.type: str = element.get("type", "unknown")
            self.name: str = element.get("name", "unknown")
            self.typegroup: str = element.get("group", "unkown")
        def create(self) -> Node.Input:
            return Node.Input(self.type, self.typegroup, self.name)
    @todo
    class IOutput(IPort[Node.Output]):
        def __init__(self, element: ET.Element):
            self.type: str = element.get("type", "unknown")
            self.name: str = element.get("name", "unknown")
            self.typegroup: str = element.get("group", "unkown")
        def create(self) -> Node.Output:
            return Node.Output(self.type, self.typegroup, self.name)
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
    
    def create(self, master: IPyNodesRenderer, objectList: IPyNodes) -> Node:
        createdInputs:  list[Node.Input]  = [input.create() for input in self.inputs]
        createdOutputs: list[Node.Output] = [output.create() for output in self.inputs]
        return Node(master, self.title, self.color, createdInputs, createdOutputs, objectList)

