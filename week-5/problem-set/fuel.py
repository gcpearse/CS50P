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
  while True:
    try:
      fraction = get_fraction()
      percentage = convert(fraction)
      if 0 <= percentage <= 100:
        print(gauge(percentage))
        break
      else:
        pass
    except ValueError or ZeroDivisionError:
      pass


def get_fraction():
  return input("Fraction: ").strip()


def convert(fraction: str):
  x, y = fraction.split("/")
  if int(y) == 0:
    raise ZeroDivisionError
  elif int(x) > int(y):
    raise ValueError
  else:
    return round(int(x) / int(y) * 100)


def gauge(percentage: int):
  if percentage >= 99:
    return "F"
  elif percentage <= 1:
    return "E"
  else:
    return f"{percentage}%"


if __name__ == "__main__":
  main()
