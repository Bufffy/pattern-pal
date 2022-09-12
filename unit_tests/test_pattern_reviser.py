import pytest
from unittest.mock import Mock
from logic.pattern_reviser import PatternReviser


def test__replace_size_info_with_selected_size_info__updates_text_with_one_set_of_sizing_info():
    text = "2 (3) 4 (5) 6 balls of yarn"
    set_of_size_info = ["2 (3) 4 (5) 6"]
    size = 2
    expected = "4 balls of yarn"

    output = PatternReviser.replace_size_info_with_selected_size_info(text, set_of_size_info, size)

    assert str(output) == expected


@pytest.mark.parametrize(("size", "expected"), [(4, "6 balls of yarn\nk 130 stitches"), (0, "2 balls of yarn\nk 110 "
                                                                                            "stitches")])
def test__replace_size_info_with_selected_size_info__updates_text_with_multiple_sets_of_sizing_info(size, expected):
    size_info = "2 (3) 4 (5) 6"
    more_size_info = "110 (115) 120 (125) 130"
    text = f"{size_info} balls of yarn\nk {more_size_info} stitches"

    output = PatternReviser.replace_size_info_with_selected_size_info(text,
                                                                      [size_info, more_size_info],
                                                                      size)

    assert str(output) == expected


def test__trim_size_info__removes_symbols_from_size_info():
    symbols = ["(", ")"]
    size_info = "(56)"
    expected = "56"

    output = PatternReviser.trim_size_info(symbols, size_info)

    assert str(output) == expected


def test__replace_size_info_with_selected_size_info__removes_parentheses_from_size_info():
    parentheses = ["(", ")"]
    PatternReviser.trim_size_info = Mock()
    PatternReviser.trim_size_info.return_value = "5"

    PatternReviser.replace_size_info_with_selected_size_info("2 (3) 4 (5) 6 balls of yarn", ["2 (3) 4 (5) 6"], 3)

    PatternReviser.trim_size_info.assert_called_with(parentheses, "(5)")


def test__replace_size_info_with_selected_size_info__returns_trimmed_size_info():
    PatternReviser.trim_size_info = Mock()
    PatternReviser.trim_size_info.return_value = "5"
    expected = "5 balls of yarn"

    output = PatternReviser.replace_size_info_with_selected_size_info("2 (3) 4 (5) 6 balls of yarn", ["2 (3) 4 (5) 6"],
                                                                      3)
    assert str(output) == expected
