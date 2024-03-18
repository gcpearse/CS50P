# Prompt the user for a level
# If the level is not a positive integer, prompt again
# Randomly generate an integer between 1 and the level
# Prompt the user to guess the value of that integer
# If the guess is not a positive integer, prompt again

import random


def main():
  level = set_level()
  run_game(level)


def set_level():
  while True:
    try:
      level = int(input("Level: "))
      if (level > 0):
        return level
    except ValueError:
      continue
    
  
def run_game(level):
  secret_number = random.randint(1, level)
  while True:
    try:
      guess = int(input("Guess: "))
    except ValueError:
      continue
    if guess < 1:
      continue
    elif guess > secret_number:
      print("Too large!")
    elif guess < secret_number:
      print("Too small!")
    else:
      print("Correct!")
      break


main()
