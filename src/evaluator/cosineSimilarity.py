from src.evaluator.calculateIDF import calculateIDF
from src.evaluator.calculateSimilarity import calculateSimilarity
from src.evaluator.calculateWeights import calculateWeights
from src.evaluator.getRelevantDocs import getRelevantDocs


def cosineSimilarity(query):
    print("Retrieving Relevant Documents...")
    revelantDocs = getRelevantDocs(query)
    print("Calculating IDF...")
    IDFs = calculateIDF(revelantDocs)
    print("Calculating Weights...")
    revelantDocs, queryWeight = calculateWeights(query, revelantDocs, IDFs)
    print("Calculating Scores...")
    results = calculateSimilarity(revelantDocs, queryWeight)
    return results
