# Install the inflect module with pip
# Prompt the user for a name
# Repeat until the user enters CTRL + D
# Bid adieu to the names in the list
# Separate two names with a single "and"
# Separate 3 or more names with the Oxford comma
# Output the result

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
  if len(names):
    joined_names = p.join(names)
    print(f"Adieu, adieu, to {joined_names}!")
  else:
    print("Adieu!")


if __name__ == "__main__":
  main()
