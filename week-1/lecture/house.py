def main():
  name = input("Enter your name: ").title()
  choose_house(name)


def choose_house(name):
  match name:
    case "Harry" | "Ron" | "Hermione":
      print("Gryffindor")
    case "Draco":
      print("Slytherin")
    case _:
      print("Who?")


main()
