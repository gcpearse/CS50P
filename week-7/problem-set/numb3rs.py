# Expect an IPv4 address as input from the user
# Return True if the input is a valid IPv4 address
# Otherwise, return False

import re


def main():
  ip = get_ip()
  print(validate(ip))


def get_ip():
  return input("IPv4 Address: ").strip()


def validate(ip):
  return True if re.search(r"^(\d{1}|\d{2}|1\d{2}|2[0-5][0-5])\.(\d{1}|\d{2}|1\d{2}|2[0-5][0-5])\.(\d{1}|\d{2}|1\d{2}|2[0-5][0-5])\.(\d{1}|\d{2}|1\d{2}|2[0-5][0-5])$", ip) else False


if __name__ == "__main__":
  main()
