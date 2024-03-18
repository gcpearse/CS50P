# Prompt the user for a time
# Input could be a 24-hour time in the format ##:##
# Input could be a 12-hour time in the format ##:## a.m.
# Handle both possibilities
# Breakfast is between 7:00 and 8:00
# Lunch is between 12:00 and 13:00
# Dinner is between 18:00 and 19:00
# Print the relevant output
# If it is not time for a meal, output nothing


def main():
  time = input("Enter a time: ")
  result = convert(time)
  if 7 <= result <= 8:
    print("Breakfast time")
  elif 12 <= result <= 13:
    print("Lunch time")
  elif 18 <= result <= 19:
    print("Dinner time")


def convert(time: str):
  hours, minutes = time.split(":")
  hours = float(hours)
  if minutes.endswith("a.m."):
    if hours == 12:
      hours = hours - 12
    minutes = minutes.rstrip("am.")
  elif minutes.endswith("p.m."):
    if hours < 12:
      hours = hours + 12
    minutes = minutes.rstrip("pm.")
  minutes = float(minutes)
  minutes = minutes / 60
  return hours + minutes


if __name__ == "__main__":
  main()
