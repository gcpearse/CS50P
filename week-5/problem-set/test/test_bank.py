import pytest

from bank import value


def test_hello_str():
  assert value("hello") == "$0"


def test_h_str():
  assert value("hey") == "$20"
  assert value("hi") == "$20"


def test_other_str():
  assert value("good morning") == "$100"
  assert value("are you well?") == "$100"


def test_empty_str():
  assert value("") == "$100"


def test_number():
  with pytest.raises(AttributeError):
    value(1)
    value(1.2)
