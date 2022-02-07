import requests
import json


def converter():
    currency_to_exchange = input("Please enter the currency you want to exchange: ").lower()
    currency_response_str = requests.get(f"http://www.floatrates.com/daily/{currency_to_exchange}.json").text
    currencies = json.loads(currency_response_str)
    cache = {}
    if currency_to_exchange == "usd":
        cache["eur"] = currencies["eur"]
    elif currency_to_exchange == "eur":
        cache["usd"] = currencies["usd"]
    else:
        cache["usd"] = currencies["usd"]
        cache["eur"] = currencies["eur"]

    while True:
        currency_to_receive = input("Please enter the currency you want to receive (empty string to leave): ").lower()
        if not currency_to_receive:
            break
        amount = float(input("Please enter the amount you want to exchange (empty string to leave): "))
        if not amount:
            break
        print("Checking the cache...")
        if currency_to_receive in cache.keys():
            print("Oh! It is in the cache!")
            result = round(cache[currency_to_receive]["rate"] * amount, 2)
            print(f"You received {result} {currency_to_receive.upper()}.")
        else:
            print("Sorry, but it is not in the cache!")
            currency_response_str = requests.get(f"http://www.floatrates.com/daily/{currency_to_exchange}.json").text
            currencies = json.loads(currency_response_str)
            cache[currency_to_receive] = currencies[currency_to_receive]
            result = round(currencies[currency_to_receive]["rate"] * amount, 2)
            print(f"You received {result} {currency_to_receive.upper()}.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    converter()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
