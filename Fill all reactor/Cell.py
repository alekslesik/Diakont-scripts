class Cell:
    name = ''
    shortDescription = ''
    description = ''
    groupParameters = ''
    codeVolume = None
    codeFunction = None
    codeFunctionBase = None
    angle = None
    logicX = None
    logicY = None
    xc = None
    yc = None
    subZone = None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_xc(self):
        return self.xc

    def set_xc(self, xc):
        self.xc = xc

    def get_yc(self):
        return self.yc

    def set_yc(self, yc):
        self.yc = yc
