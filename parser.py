import pdftotext
import re

# open pdf in read and binary mode
with open("BennieTop.pdf", "rb") as pattern:
    pdfPages = pdftotext.PDF(pattern)
    pdf = "\n\n".join(pdfPages)

sizeRegex = r"([\d]+\s+\([\d]+\)\s+)+([\d]+)"
matches = re.finditer(sizeRegex, pdf)
selectedSize = 3

for match in matches:
    sizes = re.split(r"\(|\)", match.group(0).replace(" ", ""))
    valueForSelectedSize = sizes[selectedSize-1]
    pdf = pdf.replace(match.group(0), valueForSelectedSize)  

print(pdf)
