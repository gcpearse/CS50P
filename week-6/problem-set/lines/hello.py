# Define a main function
def main():
  "This is a docstring example."
  # Strip whitespace and capitalise each word
  name = get_name().strip().title()
  say_hello(name)


# Get input from the user
def get_name():
  return input("Name: ")


# Print a greeting
def say_hello(name):
  print(f"Hello, {name}!")


if __name__ == "__main__":
  main()
