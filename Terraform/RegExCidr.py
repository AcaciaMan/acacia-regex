from Item import Item
from RegEx import RegEx
import re


class RegExCidr(RegEx):
    def __init__(self):
        regEx=br'([0-9]+?)\.([0-9]+?)\.([0-9]+?)\.([0-9]+?)\/([0-9]+?)'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine, app):
        print(self.x)

        item: Item = engine.dRegExPrev['Resource']

        cidr = self.x.group().decode("utf-8")

        if not item.cidr:
            item.cidr = cidr



