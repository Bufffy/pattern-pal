from logic.patternParser import PatternParser

def test_getSizingInfo_getsSizingOptionsFromText():
        anySizingInfo = "2 (2) 3 (3) 3 (3) 3 (4) 4"
        anyOtherSizingInfo = "3 (3) 4 (4) 4 (4) 4 (5) 5"
        anyText = f"{anySizingInfo} skeins of 50 g/100m\nthen {anyOtherSizingInfo}"
        
        output = PatternParser.getSizingInfo(anyText)
        
        assert next(output).group(0) == anySizingInfo
        assert next(output).group(0) == anyOtherSizingInfo