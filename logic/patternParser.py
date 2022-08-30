import re

class PatternParser:
    @staticmethod
    def getSizingInformation(text):
        sizeRegex = "([\d]+\s+\([\d]+\)\s+)+([\d]+)"
        return re.finditer(sizeRegex, text)