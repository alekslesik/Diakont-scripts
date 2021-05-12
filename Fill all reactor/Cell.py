class Cell:
    __name = ''
    __shortDescription = ''
    __description = ''
    __groupParameters = ''
    __codeVolume = None
    __codeFunction = None
    __codeFunctionBase = None
    __angle = None
    __logicX = None
    __logicY = None
    __xc = None
    __yc = None
    __subZone = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def xc(self):
        return self.__xc

    @xc.setter
    def xc(self, xc):
        self.__xc = xc

    @property
    def yc(self):
        return self.__yc

    @yc.setter
    def yc(self, yc):
        self.__yc = yc
