import string
import re


def removePunc(sentence: str):

    target = string.punctuation
    translator = str.maketrans(target, " " * len(target))
    sentence = sentence.translate(translator)
    return re.sub(r"\W+", " ", sentence)
