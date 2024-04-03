import pytest

from working import convert


def test_valid_short_format():
  assert convert("9 AM to 5 PM") == "09:00 to 17:00"
  assert convert("10 PM to 8 AM") == "22:00 to 08:00"


def test_valid_long_format():
  assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
  assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"
  assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
  assert convert("7:47 PM to 11:59 PM") == "19:47 to 23:59"


def test_valid_mixed_format():
  assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
  assert convert("9:30 AM to 5 PM") == "09:30 to 17:00"


def test_invalid_format():
  invalid_formats = [
    "9 AM - 5 PM",
    "09:00 AM - 17:00 PM"
  ]
  for format in invalid_formats:
    with pytest.raises(ValueError):
      convert(format)


def test_invalid_time():
  invalid_times = [
    "9:60 AM to 5:60 PM",
    "9 PM to 30 PM"
  ]
  for time in invalid_times:
    with pytest.raises(ValueError):
      convert(time)
