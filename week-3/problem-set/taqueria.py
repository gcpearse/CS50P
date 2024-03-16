dishes = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}


def main():
  handle_order()


def handle_order():
  total = 0
  while True:
    try:
      item = get_item()
      total += dishes[item]
      print_total(total)
    except KeyError:
      if item == "Control-D":
        break
      else:
        print_total(total)
        pass


def get_item():
  return input("Item: ").title()


def print_total(total):
  print(f"Total: ${total:.2f}")


main()
