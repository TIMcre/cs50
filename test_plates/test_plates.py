from plates import is_valid


def test_start():
    assert is_valid("AA") == True


def test_lenght_over():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False


def test_lenght_in():
    for i in range(5):
        assert is_valid("A" * (i + 2)) == True


def test_numbers_last():
    assert is_valid("AAAAA5") == True
    assert is_valid("AA6AAA") == False


def test_first_letter():
    assert is_valid("A9") == False
    assert is_valid("9A") == False
    assert is_valid("99") == False


def test_alphanumeric_chars():
    assert is_valid("AA.") == False
    assert is_valid("AA;,") == False


def test_zeroplace():
    assert is_valid("AA009") == False
    assert is_valid("AA900") == True
