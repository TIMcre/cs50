from twttr import shorten
import pytest


def test_lower():
    for char in ["a", "e", "i", "o", "u"]:
        assert shorten("test" + char) == "tst"


def test_upper():
    for char in ["A", "E", "I", "O", "U"]:
        assert shorten("test" + char) == "tst"


def test_number():
    with pytest.raises(TypeError) as exc_info:
        shorten(1)
    assert shorten("2") == "2"


def test_punc():
    assert shorten(".,;") == ".,;"
