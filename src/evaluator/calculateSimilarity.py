import math

from src.helpers.loadFile import loadFile


def calculateSimilarity(releventDocs, queryWeight):
    for index in sorted(releventDocs.keys(), key=int):
        print(f"Calculating score for Index #{index}")
        num = 0
        for word in queryWeight:
            if word in releventDocs[index]:
                num += releventDocs[index][word] * queryWeight[word]
        den = calculateMagnitude(index, queryWeight)
        releventDocs[index] = num / den
    return releventDocs


def calculateMagnitude(index, queryWeight):
    resumeCollection = loadFile("./data/resumeCollection.json")
    dictionary = loadFile("./data/dictionary.json")
    N = len(resumeCollection)

    docMag = 0
    for word in set(resumeCollection[index]["stemmedWords"]):
        f = resumeCollection[index]["stemmedWords"].count(word)
        tf = 1 + math.log10(f)
        docMag += (tf * math.log10(N / dictionary[word])) ** 2

    queryMag = 0
    for word in queryWeight:
        queryMag += queryWeight[word] ** 2

    return (docMag ** 0.5) * (queryMag ** 0.5)
