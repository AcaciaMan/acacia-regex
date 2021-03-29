from Item import Item
from RegEx import RegEx
import re


class RegExQueue(RegEx):
    def __init__(self):
        regEx=br'>jms://(.+?)/(.+?)/(.+?)</'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine, app):
        print(engine.getProjectName() + ' ' + str(self.x))

        if engine.sFile.endswith('.proxy'):
            item = Item()

            item.id = self.x.group(3).decode("utf-8")
            item.sFile = engine.getProjectName()
            item.dRefItemIds = {}
            item.dRefToItemIds = {}

            app.dItems[item.id] = item
            engine.dRegExPrev['JMSProxy'] = item
        elif engine.sFile.endswith('.bix'):
            queue = self.x.group(3).decode("utf-8")
            item: Item = app.dItems.get(queue)
            if item:
                item.sBix = engine.getProjectName()
            else:
                item = Item()

                item.id = queue
                item.sBix = engine.getProjectName()
                app.dItems[item.id] = item

