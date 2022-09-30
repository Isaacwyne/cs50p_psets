import requests
import json


def main():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    obj = response.json()
    # print(json.dumps(obj['bpi']['USD'], indent=2))
    price = obj['bpi']['USD']['rate_float']
    print(price)


if __name__ == '__main__':
    main()
