from twttr import shorten


def test_shorten_lower():
    assert shorten("hello") == "hll"


def test_shorter_upper():
    assert shorten("FRUIT") == "FRT"


def test_shorter_mix():
    assert shorten("Alloc") == "llc"


def test_shorter_empty():
    assert shorten("") == ""