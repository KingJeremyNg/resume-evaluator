import math

from src.helpers.loadFile import loadFile


def calculateWeights(query, relevantDocs, IDFs):
    resumeCollection = loadFile("./data/resumeCollection.json")

    for index in relevantDocs:
        for word in relevantDocs[index]:
            f = resumeCollection[index]["stemmedWords"].count(word)
            tf = 1 + math.log10(f)
            relevantDocs[index][word] = tf * IDFs[word]

    queryWeight = {}
    for word in query:
        if word not in IDFs:
            continue
        f = query.count(word)
        tf = 1 + math.log10(f)
        queryWeight[word] = tf * IDFs[word]

    return relevantDocs, queryWeight
