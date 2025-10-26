from fuel import convert, gauge
import pytest


def test_convert_normal():
    assert convert("3/4") == 75


def test_covert_round():
    assert convert("2/3") == 67


def test_convert_str():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_convert_float():
    with pytest.raises(ValueError):
        convert("3.14/5.96")


def test_convert_divide_zero():
    with pytest.raises(ValueError):
        convert("4/0")


def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/4")


def test_gauge_normal():
    assert gauge(75) == "75%"


def test_gauge_full():
    assert gauge(100) == "F"


def test_gauge_empty():
    assert gauge(1) == "E"