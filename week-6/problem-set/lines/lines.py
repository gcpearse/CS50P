# Expect the name of a Python file as a CL argument
# Output the number of lines of code in that file
# Exclude comments, docstrings, and blank lines
# Exit via sys.exit in the following cases:
# There is not exactly one CL argument
# The specified file name does not end in .py
# The specified file does not exist

import sys


def main():
  print(handle_cli_input())


def handle_cli_input():
  if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
  else:
    if not sys.argv[1].endswith(".py"):
      sys.exit("Not a Python file")
    else:
      return count_lines()


def count_lines():
  try:
    with open(sys.argv[1]) as file:
      count = 0
      for line in file:
        if (
          line.isspace() or
          line.lstrip().startswith(("#", "\"", "\'"))
        ):
          continue
        else:
          count += 1
      return count
  except FileNotFoundError:
    sys.exit("File does not exist")


if __name__ == "__main__":
  main()
