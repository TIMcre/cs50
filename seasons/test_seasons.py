import seasons as sea
from datetime import date

cur = date.today()


def test_difrence():
    assert sea.getDateDifMinutes(date(2001, 1, 1), date(2002, 1, 1)) == 525600
    assert sea.getDateDifMinutes(date(2001, 1, 1), date(2003, 1, 1)) == 1051200
