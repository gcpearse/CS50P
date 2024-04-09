from seasons import validate_dob


def test_valid_input():
  assert validate_dob("1990-11-27") == True
  assert validate_dob("2000-01-02") == True
  assert validate_dob("1985-12-31") == True


def test_invalid_input():
  assert validate_dob("1990-11-32") == False
  assert validate_dob("2010-13-27") == False
  assert validate_dob("1995-00-21") == False
  assert validate_dob("19950-10-11") == False
  assert validate_dob("January 1st, 1990") == False
