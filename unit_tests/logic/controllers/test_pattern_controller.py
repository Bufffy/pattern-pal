from unittest.mock import patch
from logic.controllers.pattern_controller import PatternController


@patch("logic.pattern_updater.PatternUpdater.update_pattern")
@patch("builtins.input", side_effect=["BennieTop.pdf", 2])
class TestPatternController:
    def test__update_pattern__prompts_user_to_enter_name_of_pdf_file(self, mock_input, mock_pattern_updater):
        PatternController.update_pattern()

        mock_input.assert_any_call("enter pattern file name: ")

    def test__update_pattern__prompts_user_to_enter_their_size(self, mock_input, mock_pattern_updater):
        PatternController.update_pattern()

        mock_input.assert_any_call("enter your size: ")

    def test__update_pattern__updates_pattern_pdf_with_user_size(self, mock_input, mock_pattern_updater):
        PatternController.update_pattern()

        mock_pattern_updater.assert_called_with("BennieTop.pdf", 1)

