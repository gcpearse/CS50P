# Prompt the user for input of two or more words
# Replace each space with an ellipsis
# Output the result


def main():
  text = input("Enter two or more words: ")
  result = pause_between_words(text)
  print(result)


def pause_between_words(text):
  words = text.split(" ")
  return "...".join(words)


if __name__ == "__main__":
  main()
