# Expect a string of HTML as input from the user
# Extract any YouTube URL that is the value of a src attribute of an iframe element therein
# Return the shorter youtu.be equivalent as a string
# Expect the URL to take one of the following formats:
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0
# The output prefix should be https in all cases

import re


def main():
  html = get_input()
  print(parse(html))


def get_input():
  return input("HTML: ").strip()


def parse(html: str):
  matches = re.search(r"^<iframe.+src=\"((https?):\/\/(?:www\.)?youtube\.com\/embed\/.+?)\".+<\/iframe>$", html)
  if matches:
    if matches.group(2) == "http":
      url = matches.group(1).replace("http", "https")
    else:
      url = matches.group(1)
    return re.sub(r"(?:www\.)?youtube\.com\/embed", "youtu.be", url)


if __name__ == "__main__":
  main()
