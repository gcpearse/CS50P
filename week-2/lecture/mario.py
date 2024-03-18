def main():
  n = get_number()
  print_square(n)


def get_number():
  while True:
    n = int(input("Enter a number between 1 and 10: "))
    if 0 < n <= 10:
      return n


def print_square(size):
  for _ in range(size):
    print_row(size)


def print_row(width):
  print("#" * width)


if __name__ == "__main__":
  main()
