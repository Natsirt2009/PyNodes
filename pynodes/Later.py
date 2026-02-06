from typing import Generic, TypeVar, Type

T = TypeVar("T")

class Later(Generic[T]):
    def __init__(self, cls: Type[T]) -> None:
        self._cls = cls
        self._value: T | None = None

    def build(self) -> None:
        self._value = self._cls()

    def get(self) -> T:
        if self._value is None:
            raise RuntimeError("Object not built yet")
        return self._value
