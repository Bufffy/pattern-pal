import re

class PatternParser:
    @staticmethod
    def getSizingInfo(text):
        sizeRegex = r"([\d]+\s+\([\d]+\)\s+)+([\d]+)"
        return re.finditer(sizeRegex, text)