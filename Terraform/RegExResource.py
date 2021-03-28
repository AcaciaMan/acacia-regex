from Item import Item
from RegEx import RegEx
import re


class RegExResource(RegEx):
    def __init__(self):
        regEx=br'resource (.+?) (.+?) {'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine, app):
        print(self.x)

        item = Item()

        item.id = self.x.group(2).decode("utf-8")
        item.type = self.x.group(1).decode("utf-8")
        item.dRefItemIds = {}
        item.dRefToItemIds = {}

        app.dItems[item.type+'.'+item.id] = item
        engine.dRegExPrev['Resource'] = item
