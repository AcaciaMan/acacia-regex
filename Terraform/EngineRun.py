from App import App
from Engine import Engine
from RegExCidr import RegExCidr
from RegExDefaultRefId import RegExDefaultRefId
from RegExRefId import RegExRefId
from RegExResource import RegExResource


class EngineRun:
    app = App()
    engine = Engine()
    engine.app = app
    engine.dRegEx["Resource"] = RegExResource()
    engine.dRegEx["RefId"] = RegExRefId()
    engine.dRegEx["DefaultRefId"] = RegExDefaultRefId()
    engine.dRegEx["Cidr"] = RegExCidr()

    engine.sFile = 'core.tf'
    engine.run()

    app.calculate()
    app.print()

