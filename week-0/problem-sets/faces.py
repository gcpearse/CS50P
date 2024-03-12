# Prompt the user for text input including emoticons.
# Replace each :) and :( with an emoji.
# Output the result.


def main():
  text = input("Enter some text with emoticons: ")
  convert_emoticons(text)


def convert_emoticons(text):
  text = text.replace(":)", "🙂")
  text = text.replace(":(", "🙁")
  print(text)


main()
