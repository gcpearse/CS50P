import pytest

from twttr import shorten


def test_empty_str():
  assert shorten("") == ""


def test_no_vowels():
  assert shorten("rhythm") == ("rhythm")
  assert shorten("lynx lynx") == ("lynx lynx")


def test_vowels():
  assert shorten("twitter") == ("twttr")
  assert shorten("this is the tweet") == ("ths s th twt")


def test_int():
  with pytest.raises(TypeError):
    shorten(1)


def test_float():
  with pytest.raises(TypeError):
    shorten(1.1)


def test_bool():
  with pytest.raises(TypeError):
    shorten(True)
