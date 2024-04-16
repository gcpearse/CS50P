students = ["Harry", "Ron", "Hermione"]

# Dictionary comprehension
gryffindors = {
  student: "Gryffindor" for student in students
}

# Enumerate
for i, student in enumerate(students):
  print(i + 1, student)
