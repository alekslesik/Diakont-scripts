import configparser


class MyConfigParser(configparser.ConfigParser):
    # redifinition in RawConfigParser
    def optionxform(self, optionstr):
        return optionstr
