
import urllib.request, json, datetime, math

from Card import Card

from utility_ExchangeRate import ExchangeRate
from utility_InventoryValue import InventoryValue

from constants import RARITIES, HEROES

# holds data 'self.card_data_by_rarity'
# access by get_card_data_by_rarity() or get_card_data()
class MarketData:
    def __init__(self):
        self.refresh_data()

    # get data from steam, scrape useful info and save to self.card_data_by_rarity
    def refresh_data(self):
        # set exchange rate
        self.exchange_rate = ExchangeRate()

        # get data from steam, analyze, etc
        data_by_rarity = {}
        for rarity in RARITIES:
            data = self.get_raw_data_per_rarity(rarity)
            data_by_rarity[rarity] = self.analysis_per_rarity(rarity, data)
        self.card_data_by_rarity = data_by_rarity

        # get inventory data if possible
        self.inventory = InventoryValue(self.get_card_data())

    # returns card data split into rarities in object: { rarity: card_list }
    def get_card_data_by_rarity(self):
        return self.card_data_by_rarity

    # returns list of all card data
    def get_card_data(self):
        # combine lists
        full_card_list = []
        for rarity in RARITIES:
            full_card_list += self.card_data_by_rarity[rarity]
        return full_card_list

    ## PRIVATE FUNCTIONS ##

    def get_raw_data_per_rarity(self, rarity):
        with urllib.request.urlopen(f"https://steamcommunity.com/market/search/render/?search_descriptions=0&category_583950_Rarity%5B%5D=tag_Rarity_{rarity}&sort_dir=desc&appid=583950&norender=1&count=500&currency=1") as url:
            data = json.loads(url.read().decode())
        return data['results']

    def analysis_per_rarity(self, rarity, data):
        card_list = []
        exchange_rate = ExchangeRate().get_rate()
        for entry in data:
            name = entry['asset_description']['market_name']
            
            # Generate named card
            new_card = Card(name)
            
            # Add required data
            new_card.hero = name in HEROES # used to ensure only 1 of each hero required in deck
            new_card.rarity = rarity
            new_card.price = entry['sell_price'] / 100 * exchange_rate # price with exchange rate applied

            # Add named card to list
            card_list.append(new_card)
        return card_list