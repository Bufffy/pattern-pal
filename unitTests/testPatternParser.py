from logic.patternParser import PatternParser

def test_getSizingInformation_getsSizingOptionsFromText():
        service = PatternParser()
        anyText = "2 (2) 3 (3) 3 (3) 3 (4) 4 skeins of 50 g/100m"
        expected = "2 (2) 3 (3) 3 (3) 3 (4) 4"
        
        sizingInfo = service.getSizingInformation(anyText)
        
        assert next(sizingInfo).group(0) == expected 