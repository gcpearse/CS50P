import pytest

from plates import validate_plate


def test_empty_str():
  assert validate_plate("") == False


def test_str_length():
  assert validate_plate("A") == False
  assert validate_plate("ABCD") == True
  assert validate_plate("ABCDEFG") == False


def test_only_alnum_chars():
  assert validate_plate("ABCDEF") == True
  assert validate_plate("CS50") == True
  assert validate_plate("AB*CDE") == False


def test_str_start():
  assert validate_plate("AA") == True
  assert validate_plate("A1") == False


def test_first_num_not_zero():
  assert validate_plate("AABB10") == True
  assert validate_plate("AABB01") == False


def test_only_nums_at_end():
  assert validate_plate("AABB23") == True
  assert validate_plate("AAB23C") == False
  assert validate_plate("AAB2C3") == False


def test_no_args():
  with pytest.raises(TypeError):
    validate_plate()


def test_multiple_args():
  with pytest.raises(TypeError):
    validate_plate("AA", "BB")
