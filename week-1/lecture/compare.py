def main():
  x = int(input("Enter a value for x: "))
  y = int(input("Enter a value for y: "))
  check_equality(x, y)


def check_equality(x, y):
  if x == y:
    print("x is equal to y")
  else:
    print("x is not equal to y")


main()
