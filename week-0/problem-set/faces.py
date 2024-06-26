# Prompt the user for text input including emoticons
# Replace each :) and :( with an emoji
# Output the result


def main():
  text = input("Enter some text with emoticons: ")
  result = convert_emoticons(text)
  print(result)


def convert_emoticons(text: str):
  text = text.replace(":)", "🙂")
  text = text.replace(":(", "🙁")
  return text


if __name__ == "__main__":
  main()
