import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    if float(sys.argv[1]):
        pass
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    return_json = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json"
    ).json()
except requests.RequestException:
    sys.exit("Cant reach server")

bitcoin_rate = return_json["bpi"]["USD"]["rate"].replace(",", "")
print(f"${(float(bitcoin_rate) * float(sys.argv[1])):,.4f}")
