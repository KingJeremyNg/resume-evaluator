import fitz


def loadPDF(filePath):
    reader = fitz.open(filePath)

    pages = []
    if "waterloo" in filePath.lower():
        for page in reader:
            text = page.get_text()
            if ("University of Waterloo\nCo-operative Work Terms" in text):
                pages.append(page.number)
    else:
        pages = [0]

    return {
        "reader": reader,
        "pageIndices": pages,
    }
