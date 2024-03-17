def main():
  names = input("Enter your first name and surname: ")
  formatted_names = format_names(names)
  first_name, surname = separate_names(formatted_names)
  say_hello(first_name, surname)


def format_names(names: str):
  return names.strip().title()


def separate_names(names: str):
  return names.split(" ")


def say_hello(first_name, surname):
  print(f"Hello, {first_name} {surname}!")


main()
