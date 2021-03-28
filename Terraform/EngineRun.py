from App import App
from Engine import Engine
from RegExRefId import RegExRefId
from RegExResource import RegExResource


class EngineRun:
    app = App()
    engine = Engine()
    engine.app = app
    engine.dRegEx["Resource"] = RegExResource()
    engine.dRegEx["RefId"] = RegExRefId()
    engine.sFile = 'core.tf'
    engine.run()

    app.print()

