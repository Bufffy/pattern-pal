from logic.pattern_updater import PatternUpdater


class PatternController:
    @staticmethod
    def update_pattern():
        pdf = input("enter pattern file name: ")
        size = input("enter your size: ")
        size_index = int(size) - 1

        PatternUpdater.update_pattern(pdf, size_index)
