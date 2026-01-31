from .IObject import IObject
import xml.etree.ElementTree as ET
from .abstract import abstract
from .todo import todo

class INode(IObject):
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
    def parser(xml: ET.ElementTree) -> 'INode':
        root = xml.getroot()
        title = root.get("title", "UNKNOWN")
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
        return INode(inputs, outputs, action, title)

    def __init__(self, inputs: list['INode.IInput'], outputs: list['INode.IOutput'], action: 'INode.IAction', title: str):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.title = title
        self.action = action

    def getTitle(self) -> str:
        return self.title
