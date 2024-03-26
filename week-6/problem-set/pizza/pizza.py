# Expect the name of a CSV file as a CL argument
# Use the tabulate package to output a table
# Use the library's grid format
# Exit via sys.exit in the following cases:
# There is not exactly one CL argument
# The specified file name does not end in .csv
# The specified file does not exist

import csv
import sys

from tabulate import tabulate


def main():
  print(handle_cli_input())


def handle_cli_input():
  if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
  else:
    if not sys.argv[1].endswith(".csv"):
      sys.exit("Not a CSV file")
    else:
      return format_table()


def format_table():
  try:
    with open(sys.argv[1]) as file:
      reader = csv.DictReader(file)
      return tabulate(reader, headers="keys", tablefmt="grid")
  except FileNotFoundError:
    sys.exit("File does not exist")


if __name__ == "__main__":
  main()
