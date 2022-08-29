import pdftotext
import re

# open pdf in read and binary mode
with open("BennieTop.pdf", "rb") as f:
    pdfPages = pdftotext.PDF(f)
    pdf = "\n\n".join(pdfPages)

sizeRegex = "([\d]+\s+\([\d]+\)\s+)+([\d]+)"
matches = re.finditer(sizeRegex, pdf)
selectedSize = 3

for match in matches:
    sizes = re.split("\(|\)", match.group(0).replace(" ", ""))
    valueForSelectedSize = sizes[selectedSize-1]
    pdf = pdf.replace(match.group(0), valueForSelectedSize)  

print(pdf)

# EDGE CASE: look at #1 in first set of instructions. current code fails to account for newlines when replacing old values with new