from glob import glob

import fitz
from nltk import download as nltkDownload

from src.evaluator.cosineSimilarity import cosineSimilarity
from src.helpers.clearOutputDir import clearOutputDir
from src.helpers.getSynonyms import getSynonymsOfSentence
from src.helpers.loadFile import loadFile
from src.helpers.saveResume import saveResume
from src.helpers.stem import stem


def runEval():
    config = loadFile("./config.json")
    clearOutputDir()

    # These are required from NLTK
    print("Checking NLTK data...")
    nltkDownload("punkt", quiet=True)
    nltkDownload("stopwords", quiet=True)
    nltkDownload("wordnet", quiet=True)

    # Get query
    print("Getting query...")
    if (config["useResumeTargets"]):
        fileList = glob(".\\resumeTargets\\*")
        query = ""
        for file in fileList:
            document = fitz.open(file)
            for page in document:
                query += page.get_text() + "\n"
        query += config["criteria"]
        if (config["useSynonyms"]):
            query += "\n" + getSynonymsOfSentence(query)
        query = stem(query)
    else:
        query = config["criteria"]
        if (config["useSynonyms"]):
            query += "\n" + getSynonymsOfSentence(config["criteria"])
        query = stem(query)

    # run cosineSimilarity
    results = cosineSimilarity(query)
    sortedScores = sorted(
        results.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Save top scores to output directory
    topScores = sortedScores[0:config["count"]]
    resumeCollection = loadFile("./data/resumeCollection.json")
    for rank, [index, score] in enumerate(topScores):
        fileName = f"{rank + 1}) {index} - {score}"
        resumePath = resumeCollection[index]["filePath"]
        start = resumeCollection[index]["pageStart"]
        end = resumeCollection[index]["pageEnd"]
        saveResume(fileName, resumePath, start, end)

    # Save the worst score
    if (len(sortedScores) >= config["count"]):
        worstScoreIndex, worstScoreValue = sortedScores[-1]
        fileName = f"Worst Resume - {worstScoreIndex} - {worstScoreValue}"
        resumePath = resumeCollection[worstScoreIndex]["filePath"]
        start = resumeCollection[worstScoreIndex]["pageStart"]
        end = resumeCollection[worstScoreIndex]["pageEnd"]
        saveResume(fileName, resumePath, start, end)

    print(
        f"Top {config['count']} resumes successfully saved to 'output' directory.")
    return


if __name__ == "__main__":
    runEval()
