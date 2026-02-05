from .annotators import abstract


class AObject:
    @abstract
    def __init__(self):
        self.window_id: int = 0
    @abstract
    def scale(self, factor: float) -> None:
        pass
    @abstract
    @staticmethod
    def getType() -> str:
        pass
    @abstract
    def buildTypes(self):
        pass