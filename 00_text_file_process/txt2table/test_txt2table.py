import pytest
import txt2table

def test_split():
    txt = "STFR id 'H015RID_B001' ci 'H015RID_B001' mf 1 mt cp 0 0.015 0 mr cp 0 0.015 0 s1 6 s2 6 sf 1 st cp 0 0.015 0 sr cp 0 0.015 stfr"
    seprators = ('STFR ', 'id ', 'ci ', 'mf ', 'mt ', 'cp ', 'mr ', 's1 ', 's2 ', 'sf ', 'st ', 'sr ', 'stfr')
    result = txt2table.split(txt, seprators)
    assert result == ['', '', "'H015RID_B001'", "'H015RID_B001'", '1', '', '0 0.015 0', '', '0 0.015 0', '6', '6', '1', '', '0 0.015 0', '', '0 0.015', '']