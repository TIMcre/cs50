from numb3rs import validate

def test_format():
    assert validate("0.0.0.0") == True

def test_in_range():
    for number in range(255):
        assert validate(f"{number}.{number}.{number}.{number}") == True

def test_out_range():
    assert validate("256.256.256.256") == False
    assert validate("255.256.255.255") == False
    assert validate("256.255.255.255") == False
    assert validate("0.0.512.1000") == False
    assert validate("255.1000.999.400") == False

def test_only_number():
    assert validate("&256.-1.-255.-466") == False
    assert validate("cat") == False
    assert validate("h.h.h.h") == False
