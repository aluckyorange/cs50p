from bank import value


def test_bank_hello():
    assert value("Hello") == 0


def test_bank_h():
    assert value("help") == 20


def test_bank_nor():
    assert value("get out") == 100