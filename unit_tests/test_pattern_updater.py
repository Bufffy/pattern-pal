import pytest
from logic.pattern_updater import PatternUpdater


@pytest.mark.parametrize("any_pdf_file", ("bennietop.pdf", "BENNIETOP.PDF"))
def test__update_pattern__accepts_pdf_file_format(any_pdf_file: str) -> None:
    PatternUpdater.update_pattern(any_pdf_file)


def test__update_pattern__raises_exception_when_file_format_is_not_pdf():
    any_non_pdf_file = "BennieTop.txt"

    with pytest.raises(ValueError) as e_info:
        PatternUpdater.update_pattern(any_non_pdf_file)

    assert str(e_info.value) == "File type is not pdf."


def test__update_pattern__updates_text_with_sizing_info_for_selected_size():
    any_pdf_file = "BennieTop.pdf"
    any_text_with_sizing_options = "1 (1) 2 (3) 3 balls of yarn"
    selected_size = 2

    updated_text = PatternUpdater.update_pattern(any_pdf_file)

    assert updated_text == "2 balls of yarn"
