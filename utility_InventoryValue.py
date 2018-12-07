import urllib.request, json

from settings import steamid64
from constants import HEROES, RARITIES

URL_INVENTORY_PREFIX = "http://steamcommunity.com/inventory/"
URL_INVENOTRY_SUFFIX = "/583950/2?l=english&count=5000"

class InventoryValue:
    def __init__(self, card_data):
        self.refresh_data(card_data)

    # get non-excess inventory, calculate value
    def refresh_data(self, card_data):
        self.value = self.get_inventory_value(card_data)

    # get non-excess cards currently owned
    def get_cards(self):
        cards = []
        card_counts = {}
        card_names = {}

        with urllib.request.urlopen(URL_INVENTORY_PREFIX + str(steamid64) + URL_INVENOTRY_SUFFIX) as url:
            data = json.loads(url.read().decode())

        # get count of cards via classid
        for entry in data["assets"]:
            str_key = str(entry["classid"])
            if str_key in card_counts:
                card_counts[str_key] += 1
            else:
                card_counts[str_key] = 1

        # get dictionary of classids and card names
        for entry in data["descriptions"]:
            if entry["marketable"] == 1:
                for tag in entry["tags"]:
                    if tag["internal_name"] == "card":
                        str_classid = str(entry["classid"])
                        if str_classid not in card_names:
                            card_names[str_classid] = entry["market_name"]

        # generate list of names of all non-excess cards
        for key in card_names.keys():
            if key in card_counts:
                if card_names[key] in HEROES:
                    if card_counts[key] > 1:
                        card_counts[key] = 1
                else:
                    if card_counts[key] > 3:
                        card_counts[key] = 3
                while card_counts[key] > 0:
                    cards.append(card_names[key])
                    card_counts[key] -= 1
        return cards

    # calculate value
    def get_inventory_value(self, full_card_list):
        inventory_cards = self.get_cards()
        inventory_value = 0.0
        for card in full_card_list:
            if card.name in inventory_cards:
                inventory_value += card.price
        return inventory_value