from Utils import Utils


class ServiceArea:
    def __init__(self, main_path):
        self.__main_path = main_path
        self.__path = main_path + 'Ini\ServiceArea.ini'
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
        """
        Update .ini config object
        :param section: [section]
        :param setting: setting=
        :param value: =value
        """
        Utils.update_config_parser_setting(self.__ini_config, section, setting, value)

    def get_setting(self, section, setting):
        """
        Return
        :param section: .ini file [section]
        :param setting: .ini file key=
        :return string value
        """
        return Utils.get_config_parser_setting(self.__ini_config, section, setting)

    def write(self):
        """
        Write config object to .ini file
        """
        Utils.write_ini_file(self.__ini_config, self.__path, self.__encoding)

