import csv


def main():
  students = add_students_from_file()
  print_student_info(students)


def add_students_from_file():
  students = []
  with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
      students.append({
        "name": row["name"],
        "house": row["house"],
        "home": row["home"]
      })
  return students


def print_student_info(students):
  for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}.")


main()
