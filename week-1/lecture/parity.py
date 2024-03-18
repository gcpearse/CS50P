def main():
  x = int(input("Enter a value for x: "))
  if check_is_odd(x):
    print("Odd")
  else:
    print("Even")


def check_is_odd(n):
  return n % 2


if __name__ == "__main__":
  main()
