# Prompt the user for an item
# Treat the input case-insensitively
# If the item matches a fruit, output the number of calories
# Otherwise, output nothing

fruit = {
  "apple": 130,
  "avocado": 50,
  "banana": 110,
  "cantaloupe": 50,
  "cherries": 100,
  "grapefruit": 60,
  "grapes": 90,
  "honeydew": 50,
  "kiwi": 90,
  "lemon": 15,
  "lime": 20,
  "nectarine": 60,
  "orange": 80,
  "peach": 60,
  "pear": 100,
  "pineapple": 50,
  "plums": 70,
  "strawberries": 50,
  "tangerine": 50,
  "watermelon": 80,
}


def main():
  item = input("Item: ").lower().strip()
  res = get_calories(item)
  if res:
    print(f"Calories: {res}")


def get_calories(item):
  for key in fruit:
    if key == item:
      return fruit[key]
    

main()
