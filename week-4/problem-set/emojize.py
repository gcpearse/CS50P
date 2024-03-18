# Install the emoji module with pip
# Prompt the user for input
# Convert any codes to emoji
# Output the result

import emoji


def main():
  text = get_input()
  res = convert_to_emoji(text)
  print(f"Output: {res}")


def get_input():
  return input("Input: ").strip()


def convert_to_emoji(text):
  return emoji.emojize(text)


if __name__ == "__main__":
  main()
