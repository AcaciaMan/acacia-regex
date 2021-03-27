from Engine import Engine
from RegExApostroph import RegExApostroph
from RegExWord import RegExWord


class EngineRun:
    engine = Engine()
    engine.dRegEx["RegExWord"] = RegExWord()
    engine.dRegEx["RegExApostrophe"] = RegExApostroph()
    engine.sFile = 'RegExWord.py'
    engine.run()

