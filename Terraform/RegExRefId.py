from Item import Item
from RegEx import RegEx
import re


class RegExRefId(RegEx):
    def __init__(self):
        regEx=br'([^ =\'"]+?)\.([^ =]+?)\.([^ =]+?)[\s,\'".]'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine, app):
        print(self.x)

        item = engine.dRegExPrev['Resource']

        id_ = self.x.group(2).decode("utf-8")
        type_ = self.x.group(1).decode("utf-8")
        last_ = self.x.group(3).decode("utf-8")

        print('PrevItem ' + item.type + '.' + item.id)

        if last_ == 'id':
            itemid = type_+'.'+id_
        else:
            itemid = type_+'.'+id_ + '.' + last_

        item.dRefItemIds[itemid] = None



