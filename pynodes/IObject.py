from typing import Callable
import xml.etree.ElementTree as ET
import os
from .abstract import abstract


class IObject:
    subParsers: dict[str, Callable[[ET.ElementTree], 'IObject']] = {}
    isSetup = False
    
    @abstract
    @staticmethod
    def getName() -> str:
        pass

    @abstract
    @staticmethod
    def parser(xml: ET.ElementTree) -> 'IObject':
        pass

    @abstract
    def getTitle(self) -> str:
        pass

    @classmethod
    def setup(cls):
        if cls.isSetup:
            return
        cls.isSetup = True
        for subclass in cls.__subclasses__():
            cls.subParsers[subclass.getName()] = subclass.parser
    @classmethod
    def parse(cls, path) -> 'IObject':
        cls.setup()
        xml = ET.parse(os.path.join(path, "object.xml"))
        root = xml.getroot()
        obj = cls.subParsers.get(root.tag, cls.parser)(xml)
        return obj