import json


def saveJSON(filePath, data):
    with open(filePath, "w") as file:
        json.dump(data, file)
