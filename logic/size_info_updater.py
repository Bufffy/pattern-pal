class SizeInfoUpdater:

    @staticmethod
    def replace_size_info_with_selected_size_info(text: str, sets_of_size_info: [str], size: int) -> str:
        for size_info in sets_of_size_info:
            updated_size_info = size_info.split(" ")[size]
            trimmed_and_updated_size_info = SizeInfoUpdater.trim_size_info(["(", ")"], updated_size_info)
            text = text.replace(size_info, trimmed_and_updated_size_info)
        return text

    @staticmethod
    def trim_size_info(symbols: [str], size_info: str) -> str:
        for symbol in symbols:
            size_info = size_info.replace(symbol, "")
        return size_info
