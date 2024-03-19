import pytest

from fuel import convert, gauge


def test_proper_fractions():
  assert convert("1/1") == 100
  assert convert("0/1") == 0
  assert convert("1/4") == 25
  assert convert("2/4") == 50
  assert convert("3/4") == 75
  assert convert("1/3") == 33
  assert convert("2/3") == 67
  assert convert("9/10") == 90
  assert convert("99/100") == 99


def test_improper_fractions():
  with pytest.raises(ValueError):
    convert("2/1")
  with pytest.raises(ValueError):
    convert("3/2")


def test_division_by_zero():
  with pytest.raises(ZeroDivisionError):
    convert("1/0")
  with pytest.raises(ZeroDivisionError):
    convert("2/0")


def test_invalid_input():
  with pytest.raises(ValueError):
    convert("a/b")
  with pytest.raises(ValueError):
    convert("string")


def test_empty_tank():
  assert gauge(0) == "E"
  assert gauge(1) == "E"


def test_full_tank():
  assert gauge(99) == "F"
  assert gauge(100) == "F"


def test_other_values():
  assert gauge(2) == "2%"
  assert gauge(25) == "25%"
  assert gauge(50) == "50%"
  assert gauge(75) == "75%"
  assert gauge(98) == "98%"
