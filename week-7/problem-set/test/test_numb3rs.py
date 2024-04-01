from numb3rs import validate


def test_valid_ip():
  assert validate("1.2.3.4") == True
  assert validate("127.0.0.1") == True
  assert validate("255.255.255.0") == True
  assert validate("255.255.255.255") == True


def test_invalid_ip():
  assert validate("512.512.512.512") == False
  assert validate("275.3.12.68") == False
  assert validate("1.2.3.1000") == False
  assert validate("1.2.3") == False
  assert validate("1.2.3.4.5") == False
  assert validate("-1.2.3.4") == False


def test_str():
  assert validate("cat") == False
