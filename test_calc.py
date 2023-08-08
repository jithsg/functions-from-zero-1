"""
write test cases for calc.py

"""
from mylib.calc import add, sub, mul, div, sqrt


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(4, 2) == 2


def test_mul():
    assert mul(2, 3) == 6


def test_div():
    assert div(6, 3) == 2


def test_sqrt():
    assert sqrt(4) == 2
