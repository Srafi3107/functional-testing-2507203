import pytest
import math
from target import (
    is_adult, celsius_to_fahrenheit, count_vowels, invert, greet,
    find_max, get_price, swap, common_items, is_leap_year,
    to_int, divide, power, square_root, factorial, average
)

# 1. is_adult
@pytest.mark.parametrize("age,expected", [
    (18, True),
    (19, True),
    (17, False),
    (0, False),
])
def test_is_adult_valid(age, expected):
    assert is_adult(age) == expected

def test_is_adult_negative():
    with pytest.raises(ValueError, match="age cannot be negative"):
        is_adult(-1)

# 2. celsius_to_fahrenheit
@pytest.mark.parametrize("celsius,expected", [
    (0, 32.0),
    (100, 212.0),
    (-40, -40.0),
    (36.6, 97.88),
])
def test_celsius_to_fahrenheit(celsius, expected):
    assert pytest.approx(celsius_to_fahrenheit(celsius)) == expected

# 3. count_vowels
@pytest.mark.parametrize("text,expected", [
    ("Hello World", 3),
    ("AEIOUaeiou", 10),
    ("rhythm", 0),
])
def test_count_vowels_valid(text, expected):
    assert count_vowels(text) == expected

@pytest.mark.parametrize("invalid_text", [123, None, ["a"], {"a": 1}])
def test_count_vowels_type_error(invalid_text):
    with pytest.raises(TypeError, match="text must be a string"):
        count_vowels(invalid_text)

# 4. invert
@pytest.mark.parametrize("flag,expected", [
    (True, False),
    (False, True),
])
def test_invert_valid(flag, expected):
    assert invert(flag) == expected

@pytest.mark.parametrize("invalid_flag", [1, 0, "True", None])
def test_invert_type_error(invalid_flag):
    with pytest.raises(TypeError, match="flag must be True or False"):
        invert(invalid_flag)

# 5. greet
@pytest.mark.parametrize("name,expected", [
    (None, "Hello, Guest!"),
    ("", "Hello, Guest!"),
    ("   ", "Hello, Guest!"),
    ("Alice", "Hello, Alice!"),
    ("  Bob  ", "Hello, Bob!"),
])
def test_greet(name, expected):
    assert greet(name) == expected

# 6. find_max
@pytest.mark.parametrize("numbers,expected", [
    ([1, 5, 3], 5),
    ([-1, -5, -3], -1),
    ([42], 42),
])
def test_find_max_valid(numbers, expected):
    assert find_max(numbers) == expected

def test_find_max_empty():
    with pytest.raises(ValueError, match="list is empty"):
        find_max([])

# 7. get_price
def test_get_price_valid():
    prices = {"apple": 1.5, "banana": 0.75}
    assert get_price(prices, "apple") == 1.5

def test_get_price_missing():
    prices = {"apple": 1.5}
    with pytest.raises(KeyError, match="orange not found"):
        get_price(prices, "orange")

# 8. swap
@pytest.mark.parametrize("pair,expected", [
    ((1, 2), (2, 1)),
    (("a", "b"), ("b", "a")),
])
def test_swap_valid(pair, expected):
    assert swap(pair) == expected

@pytest.mark.parametrize("invalid_pair", [
    (1,),
    (1, 2, 3),
    [],
])
def test_swap_value_error(invalid_pair):
    with pytest.raises(ValueError, match="pair must have exactly 2 values"):
        swap(invalid_pair)

# 9. common_items
def test_common_items():
    s1 = {1, 2, 3}
    s2 = {2, 3, 4}
    assert common_items(s1, s2) == {2, 3}
    assert common_items(s1, {5, 6}) == set()

# 10. is_leap_year
@pytest.mark.parametrize("year,expected", [
    (2000, True),
    (1900, False),
    (2024, True),
    (2023, False),
    (1, False),
])
def test_is_leap_year_valid(year, expected):
    assert is_leap_year(year) == expected

def test_is_leap_year_invalid():
    with pytest.raises(ValueError, match="year must be 1 or more"):
        is_leap_year(0)

# 11. to_int
@pytest.mark.parametrize("value,expected", [
    ("10", 10),
    (3.14, 3),
    (5, 5),
])
def test_to_int_valid(value, expected):
    assert to_int(value) == expected

@pytest.mark.parametrize("invalid_val", [True, False])
def test_to_int_type_error(invalid_val):
    with pytest.raises(TypeError, match="bool is not allowed"):
        to_int(invalid_val)

# 12. divide
@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 4.0),
    (5, 2, 2.5),
])
def test_divide_valid(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="cannot divide by zero"):
        divide(5, 0)

# 13. power
@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 8),
    (9, 0.5, 3.0),
])
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected

# 14. square_root
@pytest.mark.parametrize("x,expected", [
    (9.0, 3.0),
    (0, 0.0),
])
def test_square_root_valid(x, expected):
    assert square_root(x) == expected

def test_square_root_negative():
    with pytest.raises(ValueError, match="cannot take the square root of a negative number"):
        square_root(-4)

# 15. factorial
@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (5, 120),
])
def test_factorial_valid(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError, match="factorial is not defined for negative numbers"):
        factorial(-1)

# 16. average
@pytest.mark.parametrize("numbers,expected", [
    ([2, 4, 6], 4.0),
    ([10], 10.0),
])
def test_average_valid(numbers, expected):
    assert average(numbers) == expected

def test_average_empty():
    with pytest.raises(ValueError, match="list is empty"):
        average([])
