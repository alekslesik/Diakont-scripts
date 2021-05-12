from Utils import Utils


class FaPassport:
    __passports_path = ''
    __path = ''
    __encoding = ''
    __section = 'Passport'
    __description = 'FA'
    __code_function = 34
    __coord_z = 6960
    __alpha = 0.0
    __dirty = 0
    __defective = 0
    __name = ''
    __coord_x = ''
    __coord_y = ''
    __num = ''

    def __init__(self, main_path):
        self.__passports_path = main_path + 'ReloadedItems\\'
        self.__encoding = Utils.define_ini_encoding(self.__passports_path + Utils.listdir(self.__passports_path)[0])

    @property
    def x(self):
        return self.__coord_x

    @x.setter
    def x(self, coord_x):
        self.__coord_x = coord_x

    @property
    def y(self):
        return self.__coord_y

    @y.setter
    def y(self, coord_y):
        self.__coord_y = coord_y

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, directory):
        self.__path = directory

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, passportname):
        self.__name = passportname

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding):
        self.__encoding = encoding

    @property
    def code_function(self):
        return self.__code_function

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def passports_path(self):
        return self.__passports_path

    def create_passport_file(self):
        pattern = {'X': self.__coord_x,
                   'Y': self.__coord_y,
                   'Z': self.__coord_z,
                   'Alpha': self.__alpha,
                   'Code_Function': self.__code_function,
                   'Num': self.__num,
                   'Description': self.__description,
                   'Dirty': self.__dirty,
                   'Defective': self.__defective}

        Utils.write_ini_file(Utils.create_ini_file(self.__section, pattern), self.__path, self.__encoding)
