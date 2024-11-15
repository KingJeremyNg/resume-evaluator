from glob import glob

from nltk import download as nltkDownload

from src.evaluator.indexer import indexer
from src.helpers.saveJSON import saveJSON
from src.parser.loadPDF import loadPDF


def runIndexer():
    # These are required from NLTK
    print("Checking NLTK data...")
    nltkDownload("punkt", quiet=True)
    nltkDownload("stopwords", quiet=True)
    nltkDownload("wordnet", quiet=True)

    # get all resume files
    fileList = glob(".\\resumes\\*")

    # parse resume files. assuming PDF
    resumeObj = {}
    for file in fileList:
        print(f"Processing {file}...")
        resumeObj[file] = loadPDF(file)

    # index all resumes
    print("Indexing Resumes...")
    resumeCollection, dictionary, postingList = indexer(resumeObj)

    # save collection files
    print("Saving collection files...")
    saveJSON("./data/resumeCollection.json", resumeCollection)
    saveJSON("./data/dictionary.json", dict(sorted(dictionary.items(),
             key=lambda item: item[1], reverse=True)))
    saveJSON("./data/postingList.json", dict(sorted(postingList.items())))
    return


if __name__ == "__main__":
    runIndexer()
