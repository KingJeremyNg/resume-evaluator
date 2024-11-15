import fitz


def saveResume(fileName, resumePath, start, end):
    document = fitz.open(resumePath)
    newPDF = fitz.open()
    newPDF.insert_pdf(document, from_page=start, to_page=end)
    newPDF.save(f"./output/{fileName}.pdf")
    return
