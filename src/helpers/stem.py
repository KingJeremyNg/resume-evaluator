from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

from src.helpers.removePunc import removePunc


def stem(string):
    stemmer = PorterStemmer()
    stopWords = set(stopwords.words("english"))
    string = removePunc(string)

    words = word_tokenize(string)
    filteredWords = [word for word in words if not word.lower() in stopWords]

    stemmedWords = []
    for word in filteredWords:
        stemmedWords.append(stemmer.stem(word))

    return stemmedWords
