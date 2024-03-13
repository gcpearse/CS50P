def main():
  print(sum_ints())
  print(divide_floats())
  n = int(input("Choose a number to square: "))
  print(find_square(n))


def sum_ints():
  a = int(input("Enter a value for a: "))
  b = int(input("Enter a value for b: "))
  c = (a + b)
  return f"{c:,}"


def divide_floats():
  x = float(input("Enter a value for x: "))
  y = float(input("Enter a value for y: "))
  z = round(x / y, 2)
  return z


def find_square(n):
  return pow(n, 2)


main()
