students = [
  {
    "name": "Harry",
    "house": "Gryffindor"
  },
  {
    "name": "Ron",
    "house": "Gryffindor"
  },
  {
    "name": "Hermione",
    "house": "Gryffindor"
  },
  {
    "name": "Draco",
    "house": "Slytherin"
  }
]

# List comprehension
gryffindors = [
  student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
  print(gryffindor)

# Filter
gryffindors_2 = filter(lambda student: student["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors_2, key=lambda student: student["name"]):
  print(gryffindor["name"])
