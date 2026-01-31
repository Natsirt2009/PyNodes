
class HeritanceError(Exception):
    def __init__(self, clsname: str, funcName: str):
        super().__init__(F"The Method: {funcName} in {clsname} is abstract!")


def abstract(func):
    def inner(*args, **kwargs):
        raise HeritanceError(str(func.__qualname__).removesuffix("."+func.__name__), func.__name__)
    return inner