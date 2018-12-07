import math

from Feature import Feature

from constants import RARITIES

class MarketPricing(Feature):
    def print(self, market_data):
        longest_rarity = len(max(RARITIES, key=len))
        card_data = market_data.get_card_data_by_rarity()
        print(f"[ {'RARITY':>{longest_rarity}}     MEDIAN     AVERAGE ]")

        for rarity in RARITIES:
            print(f"  {(rarity):>{longest_rarity}}  -"
                + f" {self.get_median_price_in_list(card_data[rarity]):>7.2f}  -"
                + f" {self.get_average_price_in_list(card_data[rarity]):>8.3f}")

    # return average price of card, in given list
    def get_average_price_in_list(self, card_list):
        if len(card_list) > 0:
            return sum(card.price for card in card_list) / len(card_list)
        else:
            return 0

    # return median price of card, in given list
    def get_median_price_in_list(self, card_list):
        if len(card_list) > 0:
            sorted_card_list = sorted(card_list, key=lambda card: card.price)
            return sorted_card_list[math.floor(len(sorted_card_list)/2)].price