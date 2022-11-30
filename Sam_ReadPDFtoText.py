# pip install PyPDF2

# importing required modules
import PyPDF2

# creating a pdf file object
pdfFObj = open('C:/Users/SAMPA/Documents/RandomPDFfile.pdf', 'rb')

# creating a pdf reader object
pdfRdr = PyPDF2.PdfFileReader(pdfFObj)

# printing number of pages in pdf file
print(pdfRdr.numPages)

# creating a page object
pageObj = pdfRdr.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFObj.close() 