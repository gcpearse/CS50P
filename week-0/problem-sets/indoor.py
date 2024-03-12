# Prompt the user for capitalised text input.
# Output the result in lowercase.


def main():
  text = input("Enter some capitalised text: ")
  convert_to_lowercase(text)


def convert_to_lowercase(text):
  print(text.lower())


main()
