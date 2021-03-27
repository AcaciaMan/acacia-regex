from RegEx import RegEx
import re


class RegExWord(RegEx):
    def __init__(self):
        regEx=br'Something'
        recomp = re.compile(regEx)
        super().__init__(regEx, recomp)

    def hit(self, engine):
        print(self.x)
