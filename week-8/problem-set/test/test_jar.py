import pytest

from jar import Jar


def test_init():
  jar = Jar()
  assert jar.capacity == 12
  assert jar.size == 0
  with pytest.raises(ValueError):
    Jar(-1)
  with pytest.raises(ValueError):
    Jar(1.5)


def test_str():
  jar = Jar()
  assert str(jar) == ""
  jar.deposit(1)
  assert str(jar) == "🍪"
  jar.withdraw(1)
  assert str(jar) == ""


def test_deposit():
  jar = Jar()
  assert jar.size == 0
  jar.deposit(5)
  assert jar.size == 5
  jar.deposit(7)
  assert jar.size == 12
  with pytest.raises(ValueError):
    jar.deposit(2)


def test_withdraw():
  jar = Jar()
  assert jar.size == 0
  jar.deposit(5)
  assert jar.size == 5
  jar.withdraw(2)
  assert jar.size == 3
  with pytest.raises(ValueError):
    jar.withdraw(4)
