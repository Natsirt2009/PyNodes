from .IObject import IObject

class IBlock(IObject):
    pass
    @staticmethod
    def getName() -> str:
        return "block"