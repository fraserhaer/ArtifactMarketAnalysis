from Feature import Feature

from settings import specific_cards

class SpecificCardPricing(Feature):
    def print(self, market_data):
        if specific_cards:
            print("[ SPECIFIC CARDS ]")
            longest_name = len(max(specific_cards, key=len))
            specific_card_list = filter(lambda card: card.name in specific_cards, market_data.get_card_data())
            for card in specific_card_list:
                print(f"{card.name:>{longest_name+2}}  - {card.price:>6.2f}")