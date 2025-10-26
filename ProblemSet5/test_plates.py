from plates import is_valid


def test_is_valid_normal():
    assert is_valid("CS50")


def test_is_valid_all_alpha():
    assert is_valid("ABCD")


def test_is_valid_first_zero():
    assert not is_valid("CS05")


def test_is_valid_short():
    assert not is_valid("H")


def test_is_valid_long():
    assert not is_valid("OUTATIME")


def test_is_valid_sep():
    assert not is_valid("CS50P")


def test_is_valid_punc():
    assert not is_valid("PI3.14")


def test_is_valid_head():
    assert not is_valid("50CS")