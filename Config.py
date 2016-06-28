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
        listConnection = str(config["Editor"]["LastConnection"]).split(',')
        return listConnection

class ConfigWriter():
    def __init__(self):
        config.read("config.ini")

    def writeLastConnection(self,connection):
        listConnection = str(config["Editor"]["LastConnection"]).split(',')
        if len(listConnection) > 10:
            del listConnection[0]

        listConnection.append(connection)
        config.set("Editor", "LastConnection", str(listConnection).replace("'","").replace("[","").replace("]","").replace(" ",""))
        with open('config.ini', 'w') as f:
            print(config.sections())
            config.write(f)
