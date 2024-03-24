import csv


def main():
  name, home = get_input()
  add_students_to_file(name, home)


def get_input():
  name = input("Name: ").strip()
  home = input("Home: ").strip()
  return name, home


def add_students_to_file(name, home):
  with open("students-2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({
      "name": name,
      "home": home
    })


if __name__ == "__main__":
  main()
