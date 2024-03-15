# Prompt the user for input
# Output the result with all vowels removed


def main():
  text = input("Input: ")
  res = remove_vowels(text)
  print(f"Output: {res}")


def remove_vowels(text: str):
  res = ""
  vowels = ["a", "e", "i", "o", "u"]
  for letter in text:
    if letter.lower() in vowels:
      continue
    else:
      res += letter
  return res


main()
