# Run pytest test_calculator.py

import pytest

from calculator import find_square


def test_positive():
  assert find_square(2) == 4
  assert find_square(3) == 9


def test_negative():
  assert find_square(-2) == 4
  assert find_square(-3) == 9


def test_zero():
  assert find_square(0) == 0


def test_str():
  with pytest.raises(TypeError):
    find_square("cat")
