# Prompt the user for a variable name in camel case
# Convert that variable name into snake case
# Print the result


def main():
  var = input("Enter a variable name in camel case: ")
  res = convert_to_snake_case(var)
  print(res)


def convert_to_snake_case(var: str):
  res = ""
  for letter in var:
    if letter.lower() != letter:
      res += f"_{letter.lower()}"
    else:
      res += letter
  return res


main()
