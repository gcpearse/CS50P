def main():
  rank_students()
  assign_houses()
  parse_dict()


def rank_students():
  students = ["Harry", "Ron", "Hermione", "Draco"]
  for i in range(len(students)):
    print(f"{i + 1} {students[i]}")


def assign_houses():
  students = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin"
  }
  for key in students:
    print(key, students[key], sep=", ")


def parse_dict():
  students = [
    {
      "name": "Harry",
      "house": "Gryffindor",
      "patronus": "Stag"
    },
    {
      "name": "Ron",
      "house": "Gryffindor",
      "patronus": "Jack Russell"
    },
    {
      "name": "Hermione",
      "house": "Gryffindor",
      "patronus": "Otter"
    },
    {
      "name": "Draco",
      "house": "Slytherin",
      "patronus": None
    }
  ]
  for student in students:
    print(
      student["name"], 
      student["house"],
      student["patronus"],
      sep=", "
    )


if __name__ == "__main__":
  main()
