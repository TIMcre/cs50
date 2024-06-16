from fuel import convert, gauge
import pytest


def test_errors():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("1/100") == 1


def test_rounding():
    assert convert("1/3") == 33


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_percentage():
    assert gauge(35) == "35%"
