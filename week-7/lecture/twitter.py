import re


def main():
  url = get_url()
  print(retrieve_username(url))


def get_url():
  return input("Twitter URL: ").strip()


def retrieve_username(url):
  if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    return f"Username: {matches.group(1)}"


if __name__ == "__main__":
  main()
