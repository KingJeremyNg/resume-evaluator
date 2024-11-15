from src.helpers.loadFile import loadFile


def getRelevantDocs(query):
    postingList = loadFile("./data/postingList.json")
    relevantDocs = {}
    for word in query:
        if word in postingList:
            for index in postingList[word].keys():
                if index not in relevantDocs:
                    relevantDocs[index] = {}
                if word not in relevantDocs[index]:
                    relevantDocs[index][word] = 0
    return relevantDocs
