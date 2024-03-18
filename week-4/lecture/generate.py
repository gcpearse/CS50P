import random


def main():
  flip_coin()
  pick_number()
  shuffle_cards(["J", "Q", "K", "A"])


def flip_coin():
  coins = ["heads", "tails"]
  coin = random.choice(coins)
  print(coin.capitalize())


def pick_number():
  n = random.randint(1, 10)
  print(n)


def shuffle_cards(cards):
  random.shuffle(cards)
  print(", ".join(cards))


if __name__ == "__main__":
  main()
