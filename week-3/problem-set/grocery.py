# Prompt the user for an item
# Treat the input case-insensitively
# Repeat until the user enters CTRL + D
# Sort the list alphabetically
# Output each item in uppercase
# Prefix each line item with the correct quantity
# No need to pluralise each item


def main():
  groceries = get_groceries()
  res = sort_groceries(groceries)
  print_groceries(res)


def get_groceries():
  groceries = {}
  while True:
    try:
      item = input("Item: ").upper()
      if item in groceries:
        groceries[item] += 1
      else:
        groceries[item] = 1
    except EOFError:
      print()
      return groceries


def sort_groceries(groceries):
  return dict(sorted((groceries.items())))


def print_groceries(groceries):
  for item in groceries:
    print(f"{groceries[item]} {item}")


main()
