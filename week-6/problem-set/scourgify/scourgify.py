# Expect exactly 2 CL arguments
# The first should be a CSV file to read as input
# The second should be a new CSV file to write as output
# The input file will have 2 columns: name, house
# The output file should have 3 columns: first, last, house
# Split each name in the input file into first and last
# Assume that each student will have a first and last name
# The program should exit via sys.exit if:
# The user does not provide exactly 2 CL arguments
# The input file cannot be read

import csv
import sys


def main():
  students = handle_cli_input()
  data = reformat_data(students)
  write_csv(data)


def handle_cli_input():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
  else:
    return read_csv()


def read_csv():
  students = []
  try:
    with open(sys.argv[1]) as file:
      reader = csv.DictReader(file)
      for row in reader:
        students.append(row)
    return students
  except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


def reformat_data(students):
  reformatted_students = []
  for student in students:
    last, first = student["name"].split(", ")
    reformatted_students.append({
      "first": first,
      "last": last,
      "house": student["house"]
    })
  return reformatted_students


def write_csv(students):
  fieldnames = []
  for key in students[0]:
    fieldnames.append(key)
  with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
      writer.writerow(student)


if __name__ == "__main__":
  main()
