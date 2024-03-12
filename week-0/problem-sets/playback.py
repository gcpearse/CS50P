# Prompt the user for input of two or more words.
# Replace each space with an ellipsis.
# Output the result.


def main():
  text = input("Enter two or more words: ")
  pause_between_words(text)


def pause_between_words(text):
  words = text.split(" ")
  print("...".join(words))


main()
