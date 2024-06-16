from working import convert as cv
import pytest

def test_normal():
    assert cv("9 AM to 5 PM") == "09:00 to 17:00"

    with pytest.raises(ValueError):
        cv("13 AM to 19 PM")

    with pytest.raises(ValueError):
        cv("12 AM 12 PM")
