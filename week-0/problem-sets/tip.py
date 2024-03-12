# Prompt the user for the cost of a meal.
# Prompt the user for a tip percentage.
# For each input, remove special characters and convert to a float.
# Calculate the tip amount and output the result.


def main():
  total = format_total(input("Enter cost of meal as $##.## : "))
  percentage = format_percentage(input("Enter percentage tip as ##% : "))
  result = total * percentage
  print(f"Tip: ${result:.2f}")


def format_total(total: str):
  return float(total.lstrip("$"))


def format_percentage(percentage: str):
  return float(percentage.rstrip("%")) / 100


main()
