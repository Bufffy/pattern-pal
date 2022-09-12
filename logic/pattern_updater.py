from facades.pdf_parser import PdfParser
from logic.pattern_parser import PatternParser
from logic.size_info_updater import SizeInfoUpdater


class PatternUpdater:
    @staticmethod
    def update_pattern(pdf: str, size: int) -> str:
        if not pdf.upper().endswith(".PDF"):
            raise ValueError("File type is not pdf.")

        pattern_text = PdfParser.get_all_text(pdf)
        sizing_info = PatternParser.get_sizing_info(pattern_text)

        return SizeInfoUpdater.replace_size_info_with_selected_size_info(pattern_text, sizing_info, size)
