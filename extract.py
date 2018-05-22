from PyPDF2 import PdfFileWriter, PdfFileReader
pdf = PdfFileReader(open("sample/W99-0803.pdf", "rb"))
for i in range(1,pdf.getNumPages()):
  page = pdf.getPage(i)
  print page.extractText()
  print '\n'
  
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re

def convert(fname, pages=None):
  if not pages:
    pagenums = set()
  else:
    pagenums = set(pages)

  output = StringIO()
  manager = PDFResourceManager()
  converter = TextConverter(manager, output, laparams=LAParams())
  interpreter = PDFPageInterpreter(manager, converter)

  infile = file(fname, 'rb')
  for page in PDFPage.get_pages(infile, pagenums):
    interpreter.process_page(page)
  infile.close()
  converter.close()
  text = output.getvalue()
  output.close
  return text

file = convert('sample/D15-1001.pdf')

print file
