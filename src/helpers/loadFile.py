import json


def loadFile(filePath):
    file = open(filePath)
    return json.load(file)
