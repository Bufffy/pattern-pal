from logic.pattern_parser import PatternParser


def test__get_sizing_info__gets_sizing_options_from_text():
    any_sizing_info = "2 (2) 3 (3) 3 (3) 3 (4) 4"
    any_other_sizing_info = "3 (3) 4 (4) 4 (4) 4 (5) 5"
    any_text = f"{any_sizing_info} skeins of 50 g/100m\nthen {any_other_sizing_info}"

    output = PatternParser.get_sizing_info(any_text)

    assert next(output).group(0) == any_sizing_info
    assert next(output).group(0) == any_other_sizing_info
