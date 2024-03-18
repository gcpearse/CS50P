def main():
  say_hello("world")
  say_goodbye("world")


def say_hello(name):
  print(f"Hello, {name}!")


def say_goodbye(name):
  print(f"Goodbye, {name}!")


# Prevent main() from being called from another file
if __name__ == "__main__":
  main()
