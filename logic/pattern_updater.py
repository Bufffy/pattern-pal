class PatternUpdater:
    @staticmethod
    def update_pattern(pdf: str):
        if not pdf.upper().endswith(".PDF"):
            raise ValueError("File type is not pdf.")

        # PdfParser.getAllText

        # PatternParser.getAllSizingInfoFromText

        # replace sizing info with sizing info corresponding to selected size
