def main():
  x = int(input("Enter a value for x: "))
  print(f"The value of {x} squared is {find_square(x)}.")


def find_square(n: int):
  return n * n


if __name__ == "__main__":
  main()
