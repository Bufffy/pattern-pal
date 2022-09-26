from unittest.mock import patch
from logic.size_info_updater import SizeInfoUpdater


@patch("logic.size_info_updater.SizeInfoUpdater.trim_size_info")
class TestSizeInfoUpdater:
    def test__replace_size_info_with_selected_size_info__updates_text_with_one_set_of_sizing_info(
            self, mock_trim_size_info):
        mock_trim_size_info.return_value = "4"
        expected = "4 balls of yarn"

        output = SizeInfoUpdater.replace_size_info_with_selected_size_info("2 (3) 4 (5) 6 balls of yarn",
                                                                           ["2 (3) 4 (5) 6"],
                                                                           2)

        assert str(output) == expected

    def test__replace_size_info_with_selected_size_info__updates_text_with_multiple_sets_of_sizing_info(
            self, mock_trim_size_info):
        size_info = "2 (3) 4 (5) 6"
        more_size_info = "110 (115) 120 (125) 130"
        mock_trim_size_info.side_effect = ["6", "130"]
        expected = "6 balls of yarn\nk 130 stitches"

        output = SizeInfoUpdater.replace_size_info_with_selected_size_info(f"{size_info} balls of yarn\nk "
                                                                           f"{more_size_info} stitches",
                                                                           [size_info, more_size_info],
                                                                           4)

        assert str(output) == expected

    def test__trim_size_info__removes_symbols_from_size_info(self, mock_trim_size_info):
        symbols = ["(", ")"]
        size_info = "(56)"
        mock_trim_size_info.return_value = "56"
        expected = "56"

        output = SizeInfoUpdater.trim_size_info(symbols, size_info)

        assert str(output) == expected

    def test__replace_size_info_with_selected_size_info__removes_parentheses_from_size_info(self,
                                                                                            mock_trim_size_info):
        parentheses = ["(", ")"]
        mock_trim_size_info.return_value = "5"

        SizeInfoUpdater.replace_size_info_with_selected_size_info("2 (3) 4 (5) 6 balls of yarn", ["2 (3) 4 (5) 6"], 3)

        mock_trim_size_info.assert_called_with(parentheses, "(5)")

    def test__replace_size_info_with_selected_size_info__returns_trimmed_size_info(self, mock_trim_size_info):
        mock_trim_size_info.return_value = "5"
        expected = "5 balls of yarn"

        output = SizeInfoUpdater.replace_size_info_with_selected_size_info("2 (3) 4 (5) 6 balls of yarn",
                                                                           ["2 (3) 4 (5) 6"],
                                                                           3)
        assert str(output) == expected
