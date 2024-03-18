# Prompt the user for a date
# Valid short date input: 9/8/1636 (MM/DD/YYYY)
# Valid long date input: September 8, 1636
# Output the date in YYYY-MM-DD format
# If the input is invalid, prompt the user again
# Assume that every month has a maximum of 31 days

months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December"
]


def main():
  print(format_date())


def get_date():
  return input("Date: ").strip().capitalize()


def validate_date(month, day, year):
  return (1 <= int(month) <= 12 and
          1 <= int(day) <= 31 and
          0 <= int(year) <= 9999)


def format_output(month, day, year):
  return f"{int(year):04}-{int(month):02}-{int(day):02}"


def format_date():
  while True:
    try:
      date = get_date()
      if date.count("/") == 2:
        month, day, year = date.split("/")
        if validate_date(month, day, year):
          return format_output(month, day, year)
      elif date.count(" ") == 2:
        month, day, year = date.split(" ")
        month = months.index(month) + 1
        if day.endswith(","):
          day = day[:-1]
        else:
          continue
        if validate_date(month, day, year):
          return format_output(month, day, year)
    except ValueError:
      pass


if __name__ == "__main__":
  main()
