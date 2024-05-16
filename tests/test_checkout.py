import pytest
from src.checkout import Checkout

from csv import DictReader

checkout_test = Checkout()


def test_price_empty_cart():
    """
    The function `test_price_empty_cart()` checks if the total price is 0 when the cart is empty.
    """
    checkout_test.scan('')
    total_price = checkout_test.price
    assert total_price == 0


def test_price_case_1():
    """
    The function `test_price_case_1` checks if scanning item 'A' results in a total price of 50.
    """
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 50


def test_price_case_2():
    """
    The function `test_price_case_2` checks if scanning items A and B results in a total price of 80.
    """
    checkout_test.scan('A')
    checkout_test.scan('B')
    total_price = checkout_test.price
    assert total_price == 80


def test_price_case_3():
    """
    The function `test_price_case_3` scans items in a specific order and checks if the total price
    matches the expected value.
    """
    checkout_test.scan('C')
    checkout_test.scan('D')
    checkout_test.scan('B')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 115


def test_price_case_4():
    """
    The function `test_price_case_4` checks if scanning two items of type 'A' results in a total price
    of 100.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 100


def test_price_case_5():
    """
    The function `test_price_case_5` checks if the total price is correctly calculated when three 'A'
    items are scanned.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 130


def test_price_case_6():
    """
    The function `test_price_case_6` scans four items of type 'A' and asserts that the total price is
    180.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 180


def test_price_case_7():
    """
    The function `test_price_case_7` scans five items of type 'A' and asserts that the total price is
    230.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 230


def test_price_case_8():
    """
    The function `test_price_case_8` scans six items of type 'A' and asserts that the total price is
    260.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 260


def test_price_case_9():
    """
    The function `test_price_case_9` scans items 'A', 'A', 'A', 'B' and asserts that the total price is
    160.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('B')
    total_price = checkout_test.price
    assert total_price == 160


def test_price_case_10():
    """
    The function `test_price_case_10` scans items A and B multiple times and asserts that the total
    price is 175.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('B')
    total_price = checkout_test.price
    assert total_price == 175


def test_price_case_11():
    """
    The function `test_price_case_11` scans items A, A, A, B, B, D and asserts that the total price is
    190.
    """
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('B')
    checkout_test.scan('D')
    total_price = checkout_test.price
    assert total_price == 190


def test_price_case_12():
    """
    The function `test_price_case_12` scans items and checks if the total price matches the expected
    value.
    """
    checkout_test.scan('D')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('A')
    checkout_test.scan('B')
    checkout_test.scan('A')
    total_price = checkout_test.price
    assert total_price == 190