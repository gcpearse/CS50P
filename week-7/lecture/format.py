import re


def main():
  name = get_name()
  print(clean_up_input(name))


def get_name():
  return input("Enter name: ").strip()


def clean_up_input(name):
  # The walrus operator allows us to assign a value and ask a boolean question on the same line.
  if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"
  return f"Hello, {name}!"


if __name__ == "__main__":
  main()
