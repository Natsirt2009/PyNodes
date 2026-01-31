from .IObject import IObject

class IType(IObject):
    @staticmethod
    def getName() -> str:
        return "type"
    
    @staticmethod
    def parser(xml, group):
        root = xml.getroot()
        title = root.get("title", "UNKNOWN")
        meta: dict[str, str] = {}
        for sub in root:
            match sub.tag:
                case 'meta':
                    meta[sub.get("name", "unknown")] = sub.get("value", "")
        return IType(group, meta, title)
    
    def __init__(self, group: str, meta: dict[str, str], title: str):
        self.meta = meta
        self.title = title
        self.group = group

    def getTitle(self):
        return self.title
    def getGroup(self):
        return self.group