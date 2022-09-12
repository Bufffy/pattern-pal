import pytest
from unittest.mock import Mock
# dependencies
from logic.size_info_updater import SizeInfoUpdater
from logic.pattern_updater import PatternUpdater
from logic.pattern_parser import PatternParser
from facades.pdf_parser import PdfParser


@pytest.mark.parametrize("pdf_file", ("bennietop.pdf", "BENNIETOP.PDF"))
def test__update_pattern__accepts_pdf_file_format(pdf_file: str):
    size = 2
    PdfParser.get_all_text = Mock()
    PdfParser.get_all_text.return_value = "2 (3) 4 (5) 6 balls of yarn"
    PatternParser.get_sizing_info = Mock()
    PatternParser.get_sizing_info.return_value = ["2 (3) 4 (5) 6"]

    PatternUpdater.update_pattern(pdf_file, size)


def test__update_pattern__raises_exception_when_file_format_is_not_pdf():
    size = 4
    non_pdf_file = "BennieTop.txt"

    with pytest.raises(ValueError) as e_info:
        PatternUpdater.update_pattern(non_pdf_file, size)

    assert str(e_info.value) == "File type is not pdf."


def test__update_pattern__gets_text_from_file():
    pdf_file = "BennieTop.pdf"
    size = 2
    PdfParser.get_all_text = Mock()
    PdfParser.get_all_text.return_value = "2 (3) 4 (5) 6 balls of yarn"

    PatternUpdater.update_pattern(pdf_file, size)

    PdfParser.get_all_text.assert_called_with(pdf_file)


def test__update_pattern__gets_sets_of_size_info_from_pdf_text():
    size = 2
    pdf_file_text = "2 (3) 4 (5) 6 balls of yarn"
    PdfParser.get_all_text = Mock()
    PdfParser.get_all_text.return_value = pdf_file_text
    PatternParser.get_sizing_info = Mock()
    SizeInfoUpdater.replace_size_info_with_selected_size_info = Mock()

    PatternUpdater.update_pattern("BennieTop.pdf", size)

    PatternParser.get_sizing_info.assert_called_with(pdf_file_text)


def test__update_pattern__replaces_sets_of_size_info_with_selected_size_info():
    size = 2
    text = "2 (3) 4 (5) 6 balls of yarn"
    sizing_info = ["2 (3) 4 (5) 6"]
    PdfParser.get_all_text = Mock()
    PdfParser.get_all_text.return_value = text
    PatternParser.get_sizing_info = Mock()
    PatternParser.get_sizing_info.return_value = sizing_info
    SizeInfoUpdater.replace_size_info_with_selected_size_info = Mock()

    PatternUpdater.update_pattern("BennieTop.pdf", size)

    SizeInfoUpdater.replace_size_info_with_selected_size_info.assert_called_with(text, sizing_info, size)


def test__update_pattern__returns_updated_text_with_selected_size_info():
    updated_pattern = "6 balls of yarn"
    size = 4
    PdfParser.get_all_text = Mock()
    PdfParser.get_all_text.return_value = "2 (3) 4 (5) 6 balls of yarn"
    PatternParser.get_sizing_info = Mock()
    PatternParser.get_sizing_info.return_value = ["2 (3) 4 (5) 6"]
    SizeInfoUpdater.replace_size_info_with_selected_size_info = Mock()
    SizeInfoUpdater.replace_size_info_with_selected_size_info.return_value = updated_pattern

    output = PatternUpdater.update_pattern("BennieTop.pdf", size)

    assert str(output) == updated_pattern
