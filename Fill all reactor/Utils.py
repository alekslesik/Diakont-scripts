import itertools
import chardet
import os
from MyConfigParser import MyConfigParser


class Utils:
    # Define .ini file encoding
    # return string encoding

    @staticmethod
    def define_ini_encoding(file_directory):
        with open(file_directory, 'rb') as file:
            data = file.read(20000)
            detect = chardet.detect(data)
            return detect['encoding']

    @staticmethod
    def get_config_object():
        """
        Get MyConfigParser object
        :return: MyConfigParser object
        """
        return MyConfigParser()

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
        Utils.write_ini_file(config_object, path)

    @staticmethod
    def get_config_parser_setting(config_object, section, setting):
        """
        Return
        :param config_object: MyConfigParser object
        :param section: .ini file [section]
        :param setting: .ini file key=
        :return: value string
        """
        return config_object.get(section, setting)

    @staticmethod
    def remove_config_parser_section(config_object, section):
        """
        Remove section in configparser object
        :param config_object: configparser object
        :param section: [section]
        :return: configparser object
        """
        return config_object.remove_section(section)

    @staticmethod
    def has_section_config_parser(config_object, section):
        """
        Is section exists in configparser object
        :param config_object: configparser object
        :param section: [section]
        :return: configparser object
        """
        return config_object.has_section(section)

    @staticmethod
    def create_ini_file(section, pattern):
        """
        Fill MyConfigParser object with section
        :param section: .ini [section]
        :param pattern: dictionary with key=value
        :return: MyConfigParser object
        """
        config_file = Utils.get_config_object()
        config_file[section] = pattern
        return config_file

    @staticmethod
    def write_ini_file(ini_config, path, encoding=''):
        """
        Write MyConfigParser object to file
        :param ini_config: MyConfigParser object
        :param path: .ini file path to write
        :param encoding: encoding
        """
        global_section = 'global'

        if encoding == '':
            encoding = Utils.define_ini_encoding(path)
        if Utils.has_section_config_parser(ini_config, global_section):
            Utils.remove_config_parser_section(ini_config, global_section)
        with open(path, "w", encoding=encoding) as ini_file:
            ini_config.write(ini_file)

    @staticmethod
    def listdir(path):
        """
        Return a list containing the names of the entries in the directory given by path
        :param path: files path
        :return: list of file names in path
        """
        return os.listdir(path)

    @staticmethod
    def path_join(main_path, path):
        """
        Join one or more path components intelligently
        :param main_path:
        :param path:
        :return string
        """
        return os.path.join(main_path, path)

    @staticmethod
    def remove_path(path):
        """
        Remove (delete) the file path
        :param path:
        """
        os.remove(path)
