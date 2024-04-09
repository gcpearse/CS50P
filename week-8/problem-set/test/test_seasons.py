from seasons import validate_dob, convert_to_words


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


def test_convert_to_words():
  assert convert_to_words(1) == "One minute"
  assert convert_to_words(2) == "Two minutes"
  assert convert_to_words(21) == "Twenty-one minutes"
  assert convert_to_words(100) == "One hundred minutes"
  assert convert_to_words(1000) == "One thousand minutes"
  assert convert_to_words(1101) == "One thousand, one hundred one minutes"
  assert convert_to_words(123456789) == "One hundred twenty-three million, four hundred fifty-six thousand, seven hundred eighty-nine minutes"
