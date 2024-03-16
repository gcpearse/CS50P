# Prompt the user for a fraction
# The format should be X / Y, wherein X and Y are integers
# Round the result to the nearest integer
# If the result is 1% or lower, output "E"
# If the result is 99% or higher, output "F"
# Otherwise, output the percentage
# Catch and handle any exceptions
# If either X or Y is not an integer, prompt the user again
# If X is greater than Y, prompt the user again
# If Y equals 0, prompt the user again


def main():
  percentage = get_fuel_level()
  print_fuel_level(percentage)


def get_fuel_level():
  while True:
    try:
      fraction = input("Fraction: ")
      x, y = fraction.split("/")
      percentage = round(int(x) / int(y) * 100)
      if 0 <= percentage <= 100:
        return percentage
      else:
        print("Invalid percentage")
        continue
    except ValueError:
      print("Invalid fraction")
    except ZeroDivisionError:
      print("Cannot divide by zero")


def print_fuel_level(percentage):
  if percentage >= 99:
    print("Full")
  elif percentage <= 1:
    print("Empty")
  else:
    print(f"{percentage}%")


main()
