# Expect a string as input from the user
# Assume the format will match one of these options:
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# Raise a ValueError in the following cases:
# The input does not match the valid formats
# The time is invalid (e.g. 12:60 AM)

import re


def main():
  hours = get_hours()
  print(convert(hours))


def get_hours():
  return input("Hours: ").strip()


def convert(hours):
  matches = re.search(r"^([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM) to ([1-9]|1[0-2])(:[0-5][0-9])? (AM|PM)$", hours)
  if matches:
    start_hours = matches.group(1)
    start_minutes = ""
    end_hours = matches.group(4)
    end_minutes = ""
    if matches.group(3) == "PM":
      start_hours = str(int(matches.group(1)) + 12)
    if matches.group(6) == "PM":
      end_hours = str(int(matches.group(4)) + 12)
    if matches.group(2):
      start_minutes = matches.group(2)
    else:
      start_minutes = ":00"
    if matches.group(5):
      end_minutes = matches.group(5)
    else:
      end_minutes = ":00"
    return f"{int(start_hours):02}{start_minutes} to {int(end_hours):02}{end_minutes}"
  else:
    raise ValueError


if __name__ == "__main__":
  main()
