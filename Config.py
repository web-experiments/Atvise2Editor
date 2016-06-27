import configparser
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
        return config["Editor"["Arguments"]]
