import sys

from sayings import say_hello

if len(sys.argv) == 2:
  say_hello(sys.argv[1])
