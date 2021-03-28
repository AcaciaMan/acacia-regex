from Item import Item
from RegEx import RegEx
import re


class RegExRefId(RegEx):
    def __init__(self):
        regEx=br'= (.+?)\.(.+?)\.id'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine, app):
        print(self.x)

        item = engine.dRegExPrev['Resource']

        print('PrevItem ' + item.type + '.' + item.id)

        id_ = self.x.group(2).decode("utf-8")
        type_ = self.x.group(1).decode("utf-8")

        item.dRefItemIds[type_+'.'+id_] = None



