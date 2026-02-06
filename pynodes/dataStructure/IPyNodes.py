from typing import TypeVar, Type
from .AObject import AObject
from ..annotators import abstract
from .IPyNodesRenderer import IPyNodesRenderer

R = TypeVar('R', bound=AObject)

class IPyNodes:
    @abstract
    def __init__(self):
        pass
    @abstract
    def create(self, nodetype: Type[R], name: str, group: str, master: IPyNodesRenderer) -> R:
        pass