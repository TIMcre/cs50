from bank import value


def test_0():
    assert value("hello") == 0
    assert value("hello how are you doing") == 0


def test_20():
    assert value("h") == 20
    assert value("hell ya m8 how ya doing") == 20


def test_100():
    assert value("") == 100
    assert value("m8 whats up") == 100


def test_integers():
    assert value("123") == 100


def test_case():
    assert value("HELLO") == 0
    assert value("H") == 20
    assert value("EY") == 100
