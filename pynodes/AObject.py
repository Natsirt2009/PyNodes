from .annotators import abstract


class AObject:
    @abstract
    def __init__(self):
        self.window_id: int = 0
    @abstract
    @staticmethod
    def getType() -> str:
        pass