import re


class PatternParser:
    @staticmethod
    def get_sizing_info(text):
        size_regex = r"([\d]+\s+\([\d]+\)\s+)+([\d]+)"
        return re.finditer(size_regex, text)
