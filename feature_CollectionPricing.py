from Feature import Feature

from settings import steamid64

class CollectionPricing(Feature):
    def print(self, market_data):
        print("[ COLLECTION ]")
        full_collection_value = self.get_total_cost_from_scratch(market_data.get_card_data())
        label_fitter = 11
        print(f"  {'All cards':>{label_fitter}}  - {full_collection_value:>6.2f}")
        if steamid64:
            # inventory value is only non-excess cards, so printing this would be disingenuous
            #print(f"  {'Inventory':>{label_fitter}}  - {market_data.inventory.value:>6.2f}")
            to_complete_collection_cost = self.get_total_cost_from_scratch(market_data.get_card_data()) - market_data.inventory.value
            if to_complete_collection_cost < 0:
                to_complete_collection_cost = 0
            print(f"  {'To complete':>{label_fitter}}  - {to_complete_collection_cost:.2f}")

    def get_total_cost_from_scratch(self, card_list):
        total = 0.0
        for card in card_list:
            if card.hero:
                total += card.price
            else:
                total += 3 * card.price
        return total