import pytest
from unittest.mock import patch
from logic.pattern_updater import PatternUpdater


@patch("logic.size_info_updater.SizeInfoUpdater.replace_size_info_with_selected_size_info")
@patch("logic.pattern_parser.PatternParser.get_sizing_info")
@patch("facades.pdf_parser.PdfParser.get_all_text")
class TestPatternUpdater:
    @pytest.mark.parametrize("pdf_file", ("bennietop.pdf", "BENNIETOP.PDF"))
    def test__update_pattern__accepts_pdf_file_format(self, mock_get_all_text, mock_get_sizing_info, mock_replace_size_info, pdf_file):
        size = 2
        mock_get_all_text.return_value = "2 (3) 4 (5) 6 balls of yarn"
        mock_get_sizing_info.return_value = ["2 (3) 4 (5) 6"]

        PatternUpdater.update_pattern(pdf_file, size)

    def test__update_pattern__raises_exception_when_file_format_is_not_pdf(self, mock_get_all_text, mock_get_sizing_info, mock_replace_size_info):
        size = 4
        non_pdf_file = "BennieTop.txt"

        with pytest.raises(ValueError) as e_info:
            PatternUpdater.update_pattern(non_pdf_file, size)

        assert str(e_info.value) == "File type is not pdf."

    def test__update_pattern__gets_text_from_file(self, mock_get_all_text, mock_get_sizing_info, mock_replace_size_info):
        pdf_file = "BennieTop.pdf"
        size = 2
        mock_get_all_text.return_value = "2 (3) 4 (5) 6 balls of yarn"

        PatternUpdater.update_pattern(pdf_file, size)

        mock_get_all_text.assert_called_with(pdf_file)

    def test__update_pattern__gets_sets_of_size_info_from_pdf_text(self, mock_get_all_text, mock_get_sizing_info, mock_replace_size_info):
        size = 2
        pdf_file_text = "2 (3) 4 (5) 6 balls of yarn"
        mock_get_all_text.return_value = pdf_file_text

        PatternUpdater.update_pattern("BennieTop.pdf", size)

        mock_get_sizing_info.assert_called_with(pdf_file_text)

    def test__update_pattern__replaces_sets_of_size_info_with_selected_size_info(self, mock_get_all_text, mock_get_sizing_info, mock_replace_size_info):
        size = 2
        text = "2 (3) 4 (5) 6 balls of yarn"
        sizing_info = ["2 (3) 4 (5) 6"]
        mock_get_all_text.return_value = text
        mock_get_sizing_info.return_value = sizing_info

        PatternUpdater.update_pattern("BennieTop.pdf", size)

        mock_replace_size_info.assert_called_with(text, sizing_info, size)

    def test__update_pattern__returns_updated_text_with_selected_size_info(self, mock_get_all_text, mock_get_sizing_info, mock_replace_size_info):
        updated_pattern = "6 balls of yarn"
        size = 4
        mock_get_all_text.return_value = "2 (3) 4 (5) 6 balls of yarn"
        mock_get_sizing_info.return_value = ["2 (3) 4 (5) 6"]
        mock_replace_size_info.return_value = updated_pattern

        output = PatternUpdater.update_pattern("BennieTop.pdf", size)

        assert str(output) == updated_pattern
