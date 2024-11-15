import os
import glob


def clearOutputDir():
    files = glob.glob("./output/*")
    for file in files:
        if ".gitignore" in file:
            continue
        os.remove(file)
    return
