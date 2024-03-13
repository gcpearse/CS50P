def main():
  x = int(input("Enter a value for x: "))
  y = int(input("Enter a value for y: "))
  if check_equality(x, y):
    print("x is equal to y")
  else:
    print("x is not equal to y")


def check_equality(x, y):
  return x == y


main()
