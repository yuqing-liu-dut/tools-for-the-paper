# Python code for combining the response letter and the manuscript

import os
from PyPDF2 import PdfFileMerger

# Input PDF list
pdf_list = ["Response Letter.pdf", "Revised Manuscript.pdf"]
# Output PDF name
output_pdf = "Response.pdf"

file_merger = PdfFileMerger()
for pdf in pdf_list:
    file_merger.append(pdf)

file_merger.write(output_pdf)
