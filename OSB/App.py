from Item import Item


class App:
    sFolder = ' '
    dItems = {}

    def print(self):
        print('OSB items:')
        for i in self.dItems:
            item: Item = self.dItems[i]
            print(i + ';' + str(item.sFile) + ';' + str(item.sBix))


