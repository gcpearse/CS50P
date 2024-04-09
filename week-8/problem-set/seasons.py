# Prompt the user for their DOB in YYYY-MM-DD format
# Exit via sys.exit if the input format is incorrect
# Print their age in minutes, rounded to the nearest integer
# Use English words instead of numerals without 'and' between words
# Assume that the user was born at midnight
# Assume that the current time is also midnight

import inflect
import re
import sys

from datetime import date

p = inflect.engine()


def main():
  dob = get_dob()
  if not validate_dob(dob):
    sys.exit("Invalid date")
  else:
    age_in_mins = get_age_in_mins(dob)
    if age_in_mins < 0:
      sys.exit("Invalid date")
    else:
      print(convert_to_words(age_in_mins))


def get_dob():
  return input("Date of birth: ").strip()


def validate_dob(dob: str):
  return True if re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|1\d|2\d|3[0-1])$", dob) else False


def get_age_in_mins(dob: str):
  year, month, day = dob.split("-")
  return round((date.today() - date(int(year), int(month), int(day))).total_seconds() / 60)


def convert_to_words(age_in_mins: int):
  word_age = p.number_to_words(age_in_mins, andword="")
  word = "minute"
  return f"{word_age.capitalize()} {p.plural_noun(word, age_in_mins)}"


if __name__ == "__main__":
  main()
