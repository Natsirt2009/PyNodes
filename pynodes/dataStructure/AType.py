from .AObject import AObject
from ..annotators import abstract

class AType(AObject):
    @abstract
    def __init__(self):
        pass