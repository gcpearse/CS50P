# Prompt the user for a level, n
# Prompt again if the n is not 1, 2, or 3
# Randomly generate 10 maths problems
# Format each problem as X + Y =
# X and Y should be non-negative integers with n digits
# Prompt the user to solve each problem
# If the answer is incorrect or invalid, output EEE
# Allow the user up to 3 attempts
# After 3 attempts, output the correct answer
# Output the user's score out of 10 at the end of the game

import random


def main():
  level = get_level()
  score = run_game(level)
  print(f"Score: {score} / 10")


def get_level():
  while True:
    try:
      level = int(input("Level: "))
      if (1 <= level <= 3):
        return level
    except ValueError:
      continue


def generate_integer(level: int):
  if level == 1:
    return random.randint(1, 9)
  elif level == 2:
    return random.randint(10, 99)
  elif level == 3:
    return random.randint(100, 999)


def run_game(level):
  score = 0
  for _ in range(10):
    limit = 3
    x = generate_integer(level)
    y = generate_integer(level)
    while limit > 0:
      try:
        answer = int(input(f"{x} + {y} = "))
        if answer == x + y:
          score += 1
          break
        else:
          print("EEE")
          limit -= 1
      except ValueError:
        continue
    if limit == 0:
      print(f"{x} + {y} = {x + y}")
  return score


if __name__ == "__main__":
  main()
