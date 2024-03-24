def main():
  names = add_names_from_file()
  greet(names)


def add_names_from_file():
  names = []
  with open("names.txt") as file:
    for line in file:
      names.append(line.rstrip())
  return names


def greet(names):
  for name in sorted(names, reverse=True):
    print(f"Hello, {name}!")


if __name__ == "__main__":
  main()
