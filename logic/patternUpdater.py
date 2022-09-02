class PatternUpdater:
    @staticmethod
    def updatePattern(pdf : str): 
        if not pdf.upper().endswith(".PDF"):
            raise ValueError("File type is not pdf.")