import pytest
from src.checkout import Checkout

from csv import DictReader

checkout_test = Checkout()


def test_price_empty_cart():
    checkout_test.scan('')
    total_price = checkout_test.price
    assert total_price == 0


def test_price_case_1():
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 50


def test_price_case_2():
    checkout_test.scan('A')
    checkout_test.scan('B')
    total_price = checkout_test.price
    assert total_price == 80


def test_price_case_3():
    checkout_test.scan('C')
    checkout_test.scan('D')
    checkout_test.scan('B')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 115


def test_price_case_4():
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 100


def test_price_case_5():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 130


def test_price_case_6():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 180


def test_price_case_7():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 230


def test_price_case_8():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 260


def test_price_case_9():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('B')
    total_price = checkout_test.price
    assert total_price == 160


def test_price_case_10():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('B')
    total_price = checkout_test.price
    assert total_price == 175


def test_price_case_11():
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('B')
    checkout_test.scan('D')
    total_price = checkout_test.price
    assert total_price == 190


def test_price_case_12():
    checkout_test.scan('D')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 190