import json
import requests
import sys


def main():
  base_url = "https://api.carbonintensity.org.uk/regional"
  response = get_data(base_url)
  print_data(response)


def get_data(url):
  if (len(sys.argv)) != 2:
    sys.exit()
  response = requests.get(f"{url}/{sys.argv[1]}")
  print(f"Status code: {response.status_code}")
  return response.json()


def print_data(response):
  try:
    for data in response["data"]:
      for result in data["data"]:
        print(json.dumps(result["intensity"], indent=2))
  except KeyError:
    print("Invalid argument")


main()
