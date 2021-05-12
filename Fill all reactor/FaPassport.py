import configparser
from MyConfigParser import MyConfigParser


class FaPassport:
    encoding = ''
    header = 'Passport'
    description = 'FA'
    codeFunction = 34
    coordZ = 6960
    alpha = 0.0
    dirty = 0
    defective = 0
    directory = ''
    name = ''
    coordX = ''
    coordY = ''
    num = ''

    def set_x(self, coord_y):
        self.coordX = coord_y

    def get_x(self):
        return self.coordX

    def set_y(self, coord_y):
        self.coordY = coord_y

    def get_y(self):
        return self.coordY

    def set_directory(self, directory):
        self.directory = directory

    def get_directory(self):
        return self.directory

    def set_name(self, passportname):
        self.name = passportname

    def get_name(self):
        return self.name

    def set_encoding(self, encoding):
        self.encoding = encoding

    def get_encoding(self):
        return self.encoding

    def get_code_function(self):
        return self.codeFunction

    def set_num(self, num):
        self.num = num

    def get_num(self):
        return self.num

    def create_passport_file(self):
        config_passport = MyConfigParser()
        config_passport[self.header] = {'X': self.coordX,
                                        'Y': self.coordY,
                                        'Z': self.coordZ,
                                        'Alpha': self.alpha,
                                        'Code_Function': self.codeFunction,
                                        'Num': self.num,
                                        'Description': self.description,
                                        'Dirty': self.dirty,
                                        'Defective': self.defective}

        with open(self.directory, 'w', encoding=self.encoding) as passportFA:
            config_passport.write(passportFA)
