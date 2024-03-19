def main():
  name = input("Enter your name: ")
  print(say_hello(name))


def say_hello(name="world"):
 return f"Hello, {name}!"


if __name__ == "__main__":
  main()
