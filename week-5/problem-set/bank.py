# Prompt the user for a greeting
# If the greeting starts with "hello", output $0
# If the greeting starts with "h", output $20
# Otherwise, output $100
# Ignore leading whitespace
# Treat the input case-insensitively


def main():
  greeting = get_input()
  print(value(greeting))


def get_input():
  return input("Enter a greeting: ").lstrip().lower()


def value(greeting: str):
  if greeting.startswith("hello"):
    return "$0"
  elif greeting.startswith("h"):
    return "$20"
  else:
    return "$100"


if __name__ == "__main__":
  main()
