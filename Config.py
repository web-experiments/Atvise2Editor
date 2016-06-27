import configparser
import sys
from sys import path
config = configparser.ConfigParser()

class ConfigReader():
    def __init__(self):
        config.read("config.ini")

    def getEditorPath(self):
        return config["Editor"]["Path"]

    def getEditorName(self):
        return config["Editor"]["Name"]

    def getEditorArguments(self):
        return config["Editor"]["Arguments"]

    def getLastConnection(self):
        return config["Editor"]["LastConnection"]

class ConfigWriter():
    def __init__(self):
        config.read("config.ini")

    def writeLastConnection(self,connection):
        cfgfile = open("config.ini","w")
        config.set("Editor","LastConnection",str(connection))
        print(config.sections())
        cfgfile.write(config)
        cfgfile.close()