def main():
  n = get_number()
  miaow(n)


def get_number():
  while True:
    n = int(input("Enter a value for n: "))
    if n > 0:
      return n


def miaow(n):
  for _ in range(n):
    print("Miaow!")


if __name__ == "__main__":
  main()
