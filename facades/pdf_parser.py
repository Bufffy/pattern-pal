import pdftotext


class PdfParser:
    @staticmethod
    def get_all_text(pdf_file):
        read_binary_flag = "rb"
        with open(pdf_file, read_binary_flag) as pattern:
            pdf_pages = pdftotext.PDF(pattern)
            return "\n\n".join(pdf_pages)
