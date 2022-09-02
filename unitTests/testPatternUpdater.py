import re
import pytest
from logic.patternUpdater import PatternUpdater

@pytest.mark.parametrize("anyPdfFile", ("bennytop.pdf", "BENNYTOP.PDF"))
def test_updatePattern_acceptsPdfFileFormat(anyPdfFile):
    PatternUpdater.updatePattern(anyPdfFile) 

def test_updatePattern_throwsException_whenFileFormatIsNotPdf():
    anyNonPdfFile = 'BennieTop.txt'
    
    with pytest.raises(ValueError) as e_info:
        PatternUpdater.updatePattern(anyNonPdfFile)
        
    assert str(e_info.value) == "File type is not pdf."