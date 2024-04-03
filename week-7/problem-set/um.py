# Expect a line of text as input from the user
# Ignorning case, return a count of the number of times "um" appears as a word in its own right

import re


def main():
  text = get_input()
  print(count(text))


def get_input():
  return input("Text: ").strip()


def count(text):
  return len(re.findall(r"\bum\b", text, re.IGNORECASE))


if __name__ == "__main__":
  main()
