from __future__ import annotations
from typing import Generic, TypeVar, Type, Any, Optional

T = TypeVar("T")

class Later(Generic[T]):
    def __init__(self, value: Optional[T] = None) -> None:
        self.value: Optional[T] = value

    @staticmethod
    def build(laterelement: Type[T], *args: Any, **kwargs: Any) -> "Later[T]":
        """
        Baut ein Objekt des Typs `laterelement` mit den übergebenen Argumenten.
        Der Rückgabewert ist ein Later-Objekt, das das erzeugte Objekt enthält.
        """
        value = laterelement(*args, **kwargs)
        return Later[T](value)