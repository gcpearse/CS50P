# Prompt the user for capitalised text input.
# Output the result in lowercase.


def main():
  text = input("Enter some capitalised text: ")
  result = convert_to_lowercase(text)
  print(result)


def convert_to_lowercase(text):
  return text.lower()


if __name__ == "__main__":
  main()
