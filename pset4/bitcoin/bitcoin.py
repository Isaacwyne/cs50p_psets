import sys
import json
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')

    try:
        bitcoin = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number')

    price = current_price()
    result = bitcoin * price
    print(f"${result:,.4f}")


def current_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    obj = response.json()
    price = obj['bpi']['USD']['rate_float']
    return price


if __name__ == '__main__':
    main()
