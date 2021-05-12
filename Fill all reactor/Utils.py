import itertools
from MyConfigParser import MyConfigParser

import chardet


class Utils:
    variable = 1

    # Define .ini file encoding
    # return string encoding
    @staticmethod
    def define_ini_encoding(file_directory):
        with open(file_directory, 'rb') as file:
            data = file.read(20000)
            detect = chardet.detect(data)
            return detect['encoding']

    @staticmethod
    def get_config_parser(path, encoding='UTF-8-SIG'):
        """
        Parse .ini file. Get object configparser
        :param path: .ini file directory
        :param encoding: .ini file encoding
        :return: object configparser
        """
        config_file = MyConfigParser()
        with open(path, 'r', encoding=encoding) as file:
            config_file.read_file(itertools.chain(['[global]'], file), source=path)
        return config_file

    @staticmethod
    def update_config_parser_setting(config_object, path, section, setting, value):
        """
        Update .ini file
        :param config_object: object configparser
        :param path: .ini file directory to write
        :param section: .ini file [section]
        :param setting: .ini file key=
        :param value: .ini file =value
        """

        config_object.set(section, setting, value)
        with open(path, "w") as config_file:
            config_object.write(config_file)

    @staticmethod
    def write_ini_file(ini_config, path, encoding):
        with open(path, "w", encoding=encoding) as ini_file:
            ini_config.write(ini_file)
