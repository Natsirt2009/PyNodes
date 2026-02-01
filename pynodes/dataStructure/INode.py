from ..Node import Node
from .IObject import IObject
import xml.etree.ElementTree as ET
from ..annotators import todo, abstract

class INode(IObject[Node]):
    class IPort:
        @abstract
        def __init__(self):
            pass
    @todo
    class IInput(IPort):
        def __init__(self, element: ET.Element):
            pass
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
        return Node(master)
