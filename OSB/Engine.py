import mmap


class Engine:
    dRegEx = {}
    sFolder = ' '
    sFile = ' '
    pos = 0
    x = None
    c = None
    app = None
    dRegExPrev = {}

    def run(self):

        with open(self.sFile, 'r+') as f:
            data = mmap.mmap(f.fileno(), 0)
            self.pos = 0
            self.x = None
            self.c = None
            while self.pos >= 0:
                self.x = None
                for d, c in self.dRegEx.items():
                    if (not c.x) and (self.pos == 0):
                        c.x = c.recomp.search(data, self.pos)
                    elif c.x:
                        if c.x.start() < self.pos:
                            c.x = c.recomp.search(data, self.pos)
                    if c.x:
                        if self.x is None:
                            self.x = c.x
                            self.c = c
                        elif c.x.start() < self.x.start():
                            self.x = c.x
                            self.c = c
                        elif c.x.start() == self.x.start() and c.x.end() > self.x.end():
                            self.x = c.x
                            self.c = c
                if not self.x:
                    self.pos = -1
                else:
                    self.c.hit(self, self.app)
                    self.pos = self.x.end()

    def getProjectName(self):
        # Extract from sFile just remaining part after sFolder

        return self.sFile[len(self.sFolder):]

