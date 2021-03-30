from Item import Item
from RegEx import RegEx
import re


class RegExDefaultRefId(RegEx):
    def __init__(self):
        regEx = br'manage_default_resource_id = ([^ =\'"]+?)\.([^ =]+?)\.([^ =]+?)[\s,\'".]'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine, app):
        print(self.x)

        previtem = engine.dRegExPrev['Resource']

        id_ = self.x.group(2).decode("utf-8")
        type_ = self.x.group(1).decode("utf-8")
        last_ = self.x.group(3).decode("utf-8")
        itemid_ = type_ + '.' + id_ + '.' + last_

        print('PrevItem ' + previtem.type + '.' + previtem.id)

        item = Item()

        item.id = itemid_
        item.type = previtem.type
        item.dRefItemIds = {}
        item.dRefToItemIds = {}

        app.dItems[itemid_] = item
