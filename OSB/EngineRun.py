import glob

from App import App
from Engine import Engine
from RegExQueue import RegExQueue


class EngineRun:
    app = App()
    engine = Engine()
    engine.app = app
    engine.dRegEx["Queue"] = RegExQueue()

    # Loop through business services, proxy services, proxy pipelines
    sFolder = 'osb-projects/src'
    app.sFolder = sFolder
    engine.sFolder = sFolder
    files = glob.glob(sFolder+'/**/*.proxy', recursive=True)
    files += glob.glob(sFolder+'/**/*.bix', recursive=True)
    files += glob.glob(sFolder+'/**/*.pipeline', recursive=True)


    for sFile in files:
        engine.sFile = sFile
        engine.run()

    app.print()

