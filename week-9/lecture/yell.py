def main():
  yell("This", "is", "CS50!")
  yell_2("This", "is", "CS50!")


# Map
def yell(*words):
  uppercased = map(str.upper, words)
  print(*uppercased)


# List comprehension
def yell_2(*words):
  uppercased = [word.upper() for word in words]
  print(*uppercased)


if __name__ == "__main__":
  main()
