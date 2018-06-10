#!/bin/python3
import json
import sys

import requests


# This rarely changes so I'll set it here instead of requesting it
WATER_PRICE = 5

# Load the items along with their corresponding IDs
with open("item-data.json") as f:
    ITEM_DATA = json.load(f)


def get_item(item: str) -> dict:
    """Gets the buying or selling price of a specific Runescape item
    
    Args:
        item (str): The item's ID
    
    Returns:
        dict: A json respresentation of the item's current value
              Return values appear in this format (Cannonballs for example):
                {'overall': 200, 'buying': 203, 'buyingQuantity': 599379, '
                selling': 197, 'sellingQuantity': 571297}
    
    Raises:
        ConnectionError
    """
    if item not in ITEM_DATA:
        return print(f"Couldn't find {item} in item-data.json")

    url = 'https://api.rsbuddy.com/grandExchange'
    params = {'a': 'guidePrice', 'i': ITEM_DATA[item]['id']}
    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise ConnectionError(f'RSBuddy API went RIP, try again later. Code {response.status_code}')

    return response.json()


def get_potion_profit(herb_name: str) -> dict:
    """Calculates the net profit of potion - (herb + water)
    
    Args:
        herb_name (str): The name of the herb
    """
    potion_name = f'{herb_name.split()[0]} potion (unf)'
    herb_data = get_item(herb_name)
    potion_data = get_item(potion_name)

    profit = potion_data['selling'] - (herb_data['buying'] + WATER_PRICE)

    return {'herb': herb_name,
            'pot': potion_name,
            'buy': herb_data['buying'],
            'sell': potion_data['selling'],
            'profit': profit, 
            'herb_qty': (herb_data['buyingQuantity'], herb_data['sellingQuantity']), 
            'potion_qty': (potion_data['buyingQuantity'], potion_data['sellingQuantity'])}


def print_potion_profit(data: dict):
    """Nicely prints the potion profit information
    
    Args:
        data (dict): data from :func:`get_potion_profit()`
    """
    print(f'{data["herb"].title()}\n'
          f'Buy: {data["buy"]:,}\n'
          f'Sell: {data["sell"]:,}\n'
          f'Profit: {data["profit"]:,}\n'
          f'Buy/Sell Qty: ({data["potion_qty"][0]:,}/{data["potion_qty"][1]:,})\n'
          f'{"".join("-" for x in range(30))}')


def main():
    """This is mostly for my purposes, but should fit most people's stats anyway"""
    herbs = ['tarromin', 'harralander', 'ranarr weed', 'toadflax', 
             'irit leaf', 'avantoe', 'kwuarm']

    for herb in herbs:
        data = get_potion_profit(herb)
        print_potion_profit(data)


if __name__ == '__main__':
    # If a specific herb is entered
    if len(sys.argv) > 1:
        data = get_potion_profit(' '.join(sys.argv[1:]))
        print_potion_profit(data)
    else:
        main()
