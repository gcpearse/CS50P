def main():
  x = get_int("Enter a value for x: ")
  print(f"The value of x is {x}.")


def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      pass


main()
