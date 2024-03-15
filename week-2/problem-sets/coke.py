# Prompt the user to insert a coin
# Valid denominations: 5, 10, 15
# Continue until a total of 50 or more has been paid
# Display change owed


def main():
  handle_payment()


def handle_payment():
  amount_due = 50
  valid_coins = [5, 10, 25]
  while amount_due > 0:
    print(f"Amount due: {amount_due}")
    coin = int(input("Insert coin: "))
    if coin in valid_coins:
      amount_due -= coin
  if amount_due <= 0:
    print(f"Change owed: {0 - amount_due}")


main()
