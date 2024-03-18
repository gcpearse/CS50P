import json
import requests
import sys


def main():
  baseUrl = "https://api.carbonintensity.org.uk/regional"
  response = get_data(baseUrl)
  print_data(response)


def get_data(baseUrl):
  if (len(sys.argv)) != 2:
    sys.exit()
  response = requests.get(f"{baseUrl}/{sys.argv[1]}")
  return response.json()


def print_data(response):
  try:
    for data in response["data"]:
      for result in data["data"]:
        print(json.dumps(result["intensity"], indent=2))
  except KeyError:
    print("Invalid argument")


main()
