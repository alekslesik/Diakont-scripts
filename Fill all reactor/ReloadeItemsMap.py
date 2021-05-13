from Utils import Utils


class ReloadedItemsMap:
    def __init__(self, main_path):
        self.__main_path = main_path
        self.__path = main_path + 'Ini\ReloadedItemsMap.ini'
        self.__encoding = Utils.define_ini_encoding(self.__path)
        self.__ini_config = Utils.get_config_parser(self.__path, self.__encoding)

    @property
    def ini_config(self):
        return self.__ini_config

    @property
    def path(self):
        return self.__path

    @property
    def encoding(self):
        return self.__encoding

    def update_setting(self, section, setting, value):
        Utils.update_config_parser_setting(self.__ini_config, self.__path, section, setting, value)

    def write(self):
        Utils.write_ini_file(self.__ini_config, self.__path, self.__encoding)
