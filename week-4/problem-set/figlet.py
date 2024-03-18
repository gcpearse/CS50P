# Install the pyfiglet module with pip
# Expect 0 or 2 command-line arguments
# If 0 args, output text in a random font
# If 2 args, output text in a specific font
# The first arg should be -f or --font
# The second arg should be the name of a font
# Handle errors via sys.exit with an error message
# Prompt the user for input
# Output the result in the desired font

from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()


def main():
  if len(sys.argv) == 1:
    set_random_font()
  elif len(sys.argv) == 3:
    set_specific_font(sys.argv)
  else:
    sys.exit("Incorrect number of arguments")
  output_text()


def get_input():
  return input("Input: ").strip()


def set_random_font():
  figlet.setFont(font = random.choice(fonts))


def set_specific_font(args):
  flags = ["-f", "--font"]
  if args[1] in flags:
    if args[2] in fonts:
      figlet.setFont(font = args[2])
    else:
      sys.exit("Font not found")
  else:
    sys.exit("Invalid argument")


def output_text():
  text = get_input()
  print(figlet.renderText(text))


if __name__ == "__main__":
  main()
