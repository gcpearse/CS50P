# Run python3 miaows_3.py -h to see help message

import argparse

parser = argparse.ArgumentParser(
  description="Miaow like a cat"
)
parser.add_argument(
  "-n", 
  default=1, 
  help="number of times to miaow", 
  type=int
)
args = parser.parse_args()

for _ in range(int(args.n)):
  print("Miaow!")
