import re


def main():
  email = get_email()
  if validate_email(email):
    print("Valid")
  else:
    print("Invalid")


def get_email():
  return input("E-mail address: ").strip()


def validate_email(email):
  return True if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE) else False


if __name__ == "__main__":
  main()
