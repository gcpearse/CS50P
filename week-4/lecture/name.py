import sys


def print_names():
  if len(sys.argv) < 2:
    sys.exit("Too few arguments provided.")

  for arg in sys.argv[1:]:
    print(f"Hello, {arg}!")


print_names()
