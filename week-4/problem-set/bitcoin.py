# Allow the user to specify a number, n, as a command-line argument
# If n cannot be converted to a float, exit via sys.exit with an error message
# Query the API for the CoinDesk Bitcoin Price Index
# Find the current USD price of Bitcoin
# Output the price to 4 decimal places
# Use a comma as a thousands separator

import requests
import sys


def main():
  base_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
  if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
  n = get_number()
  bpi_usd = get_bitcoin_price(base_url)
  res = get_usd_price(n, bpi_usd)
  print(res)


def get_number():
  if len(sys.argv) == 2:
    try:
      return float(sys.argv[1])
    except ValueError:
      sys.exit("Command-line argument is not a number")


def get_bitcoin_price(url):
  response = requests.get(url).json()
  return response["bpi"]["USD"]["rate_float"]


def get_usd_price(n, bpi_usd):
  price = n * bpi_usd
  return f"${price:,.4f}"
  

if __name__ == "__main__":
  main()
