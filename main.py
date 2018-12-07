# Refactored and extended by aburntc00kie
# A big shoutout to the original authors of this script!
# Original by THE_DQ, edited by vadash

import datetime

from MarketData import MarketData

from feature_CollectionPricing import CollectionPricing
from feature_MarketPricing import MarketPricing
from feature_SpecificCardPricing import SpecificCardPricing
from utility_ExchangeRate import ExchangeRate

# get and store market data
market_data = MarketData()

# declare analysis features in print order
features = [
    MarketPricing(),
    CollectionPricing(),
    SpecificCardPricing()
]

# print this once, as a header
print("Artifact market and inventory analysis")
print("======================================")
print()

market_data.exchange_rate.print()
print("Check settings.py for advanced features!")
print("Press Enter to refresh prices")
print()

# print analysis whenever 'enter' is pressed
# while True:
if True:
    print("--------------------------------------")
    print()

    # Mark date and time in UTC
    print(f"[ {datetime.datetime.utcnow().strftime('%m-%d %H:%M')} UTC ]")
    print()

    for feature in features:
        feature.print(market_data)
        print()

    print("--------------------------------------")

    #input()
    #market_data.refresh_data()

