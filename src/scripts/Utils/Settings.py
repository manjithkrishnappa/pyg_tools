import json
import os
from os import path


class Config:
    __instance = None
    _isInitialized = False

    _fileName = 'AwesomeGame.conf'
    _filePath = path.expanduser('~/AwesomeGame/')
    _fileNameWithPath = path.join(_filePath, _fileName)

    # Cornflower blue
    _bgColor = [100, 149, 237]
    _screenWidth = 800
    _screenHeight = 600
    # Set FPS to 0 if we dont want v-sync
    _FPS = 60

    @property
    def bgColor(self):
        return self._bgColor

    @property
    def screenWidth(self):
        return self._screenWidth

    @property
    def screenHeight(self):
        return self._screenHeight

    @property
    def FPS(self):
        return self._FPS

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        print("Config Constructor")
        """ Virtually private constructor. """
        if Config.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Config.__instance = self

    def initialize(self):
        print("Initilizing Config")
        if(self._checkElseCreateConfFile() is not True):
            return False
        if(self._readConfFile() is not True):
            return False
        self._isInitialized = True
        return True

    def _checkElseCreateConfFile(self):
        # check if the directory exists else create the directory
        if not path.isdir(self._filePath):
            try:
                print('Directory does not Exist! Creating...' + self._filePath)
                os.makedirs(self._filePath)
            except Exception as e:
                print('Could not create directory for config file')
                print(e)
                return False
        if not path.isfile(self._fileNameWithPath):
            print('Conf file does not Exist! Creating...' + self._fileNameWithPath)
            if (self._createDefaultConf() is not True):
                return False
        return True

    def _createDefaultConf(self):
        data = {}
        data['Screen_Width'] = self._screenWidth
        data['Screen_Height'] = self._screenHeight
        data['FPS'] = self._FPS
        try:
            with open(self._fileNameWithPath, 'w') as outfile:
                json.dump(data, outfile)
        except Exception as e:
            print('Could not create default config file')
            print(e)
            return False
        return True

    def _readConfFile(self):
        try:
            print(self._fileNameWithPath)
            with open(self._fileNameWithPath) as json_file:
                data = json.load(json_file)
            self._screenWidth = data['Screen_Width']
            self._screenHeight = data['Screen_Height']
            self._FPS = data['FPS']
            return True
        except Exception as e:
            print('could not open / read the config file: ')
            print(e)
            return False
