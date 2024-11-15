from typing import TypedDict

import fitz

from src.helpers.stem import stem


class resumeType(TypedDict):
    reader: fitz.Document
    pageIndices: list[int]


def indexer(resumeObj: dict[str, resumeType]):

    resumeCollection = {}
    dictionary = {}
    postingList = {}
    resumeKey = 0
    # Iterate over each resume group
    for file in resumeObj.keys():
        pdfReader = resumeObj[file]["reader"]
        bookmarks = resumeObj[file]["pageIndices"]
        resumeCount = len(bookmarks)

        # Iterate over each resume inside of resume group
        for resumeIndex in range(resumeCount):
            # Get start and end of resume instance
            start = bookmarks[resumeIndex]
            end = bookmarks[resumeIndex + 1] if resumeIndex + \
                1 != resumeCount else pdfReader.page_count

            # Print status
            print(
                f"Indexing #{resumeKey} - {file} - Pages: {start + 1} to {end}...")

            # Convert each resume instance into a stemmed word list
            stringDoc = ""
            for pageNumber in range(start, end):
                stringDoc += pdfReader[pageNumber].get_text() + "\n"
            stemmedWords = stem(stringDoc)

            # Add information to data collections
            resumeCollection[resumeKey] = {
                "filePath": file,
                "pageStart": start,
                "pageEnd": end,
                "stemmedWords": stemmedWords,
            }
            for position, term in enumerate(stemmedWords):
                # Construct frequency dictionary
                if term not in dictionary:
                    dictionary[term] = 0
                dictionary[term] += 1
                # Construct posting list
                if term not in postingList:
                    postingList[term] = {}
                if resumeKey not in postingList[term]:
                    postingList[term][resumeKey] = []
                postingList[term][resumeKey].append(position)
            # Increment resumeKey index
            resumeKey += 1
    return (resumeCollection, dictionary, postingList)
