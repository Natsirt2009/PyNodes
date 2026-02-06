from .dataStructure.AType import AType

class Type(AType):
    def __init__(self, meta: dict[str, str]):
        self.meta = meta
    
    @staticmethod
    def getType() -> str:
        return "type"
    