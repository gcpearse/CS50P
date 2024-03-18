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


main()
