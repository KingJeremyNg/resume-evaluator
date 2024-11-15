import math

from src.helpers.loadFile import loadFile


def calculateIDF(relevantDocs):
    resumeCollection = loadFile("./data/resumeCollection.json")
    dictionary = loadFile("./data/dictionary.json")
    N = len(resumeCollection)
    IDF = {}
    for index in relevantDocs:
        for word in relevantDocs[index]:
            if word in IDF:
                continue
            DF = dictionary[word]
            IDF[word] = math.log10(N / DF)
    return IDF
