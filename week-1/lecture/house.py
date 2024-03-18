def main():
  name = input("Enter your name: ").title()
  result = choose_house(name)
  print(result)


def choose_house(name):
  match name:
    case "Harry" | "Ron" | "Hermione":
      return "Gryffindor"
    case "Draco":
      return "Slytherin"
    case _:
      return "Who?"


if __name__ == "__main__":
  main()
