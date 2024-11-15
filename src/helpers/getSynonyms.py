from itertools import chain

from nltk.corpus import wordnet

from src.helpers.removePunc import removePunc


def getSynonyms(word):
    synonyms = wordnet.synsets(word)
    lemmas = set(chain.from_iterable(
        [word.lemma_names() for word in synonyms[0:5]]))
    return lemmas


def getSynonymsOfSentence(sentence):
    synonymString = ""
    for word in removePunc(sentence).split(" "):
        synonyms = " ".join(list(getSynonyms(word)))
        synonymString += synonyms + " "
    return synonymString
