import json
import sys

import requests


class PotionCalculator:
    def __init__(self):
        with open('item-data.json') as f:
            self.item_data = json.load(f)
        self.price_data = requests.get('https://storage.googleapis.com/osbuddy-exchange/summary.json').json()

    def get_item(self, item: str) -> dict:
        """Gets the price of an OSRS item from self.item_data dict
        
        Args:
            item (str): The item to get pricing information about
        
        Returns:
            dict: The request item's pricing data
        
        Raises:
            KeyError: If the item isn't in the dict
        """
        if item not in self.item_data:
            raise KeyError(f'Item {item} not found.')

        return self.price_data[str(self.item_data[item]['id'])]

    def get_potion_profit(self, herb_name: str) -> dict:
        """Calculates the net profit of potion - (herb + water)
        
        Args:
            herb_name (str): The name of the herb
        
        Returns:
            dict: Profit for a given herb & potion
        """
        potion_name = f'{herb_name.split()[0]} potion (unf)'
        herb_data = self.get_item(herb_name)
        potion_data = self.get_item(potion_name)
        water_price = self.get_item('vial of water')['buying']

        profit = potion_data['sell_average'] - (herb_data['buy_average'] + water_price)

        return {'herb': herb_name,
                'pot': potion_name,
                'buy': herb_data['buy_average'],
                'sell': potion_data['sell_average'],
                'profit': profit, 
                'herb_qty': (herb_data['buy_quantity'], herb_data['sell_quantity']), 
                'potion_qty': (potion_data['buy_quantity'], potion_data['sell_quantity'])}

    def print_potion_profit(self, data: dict):
        """Nicely prints the potion profit information
        
        Args:
            data (dict): data from :func:`self.get_potion_profit()`
        """
        print(f'{data["herb"].title()}\n'
              f'Buy: {data["buy"]:,}\n'
              f'Sell: {data["sell"]:,}\n'
              f'Profit: {data["profit"]:,}\n'
              f'Buy/Sell Qty: ({data["potion_qty"][0]:,}/{data["potion_qty"][1]:,})\n'
              f'{"".join("-" for x in range(30))}')


if __name__ == '__main__':
    # If a specific herb is entered
    calc = PotionCalculator()

    if len(sys.argv) > 1:
        data = calc.get_potion_profit(' '.join(sys.argv[1:]))
        calc.print_potion_profit(data)
    else:
        # This is tailored to my current stats
        herbs = ['tarromin', 'harralander', 'ranarr weed', 'toadflax', 
                 'irit leaf', 'avantoe', 'kwuarm']

        for herb in herbs:
            data = calc.get_potion_profit(herb)
            calc.print_potion_profit(data)
