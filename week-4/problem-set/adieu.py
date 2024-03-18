import inflect

p = inflect.engine()


def main():
  names = get_names()
  say_adieu(names)


def get_names():
  names = []
  while True:
    try:
      name = get_input()
      if len(name):
        names.append(name)
    except EOFError:
      print()
      return names


def get_input():
  return input("Name: ").strip().title()


def say_adieu(names):
  sentence = p.join(names)
  print(f"Adieu, adieu, to {sentence}")


main()
