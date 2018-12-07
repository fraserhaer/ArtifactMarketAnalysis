# Artifact Market Analysis

Market analysis for Artifact in python.

## Features:
- Average / Median prices by rarity
- Cost to buy full collection from scratch
- Cost for you to complete your collection
- Can track specific card prices

## How to contribute:
- Fork the repo
- To add a new feature
  - Make a new .py file named feature_YourFeature
  - Make sure your feature inherits the Feature class i.e. YourFeature(Feature)
  - Make sure to write your print() method as per the Feature class spec
  - Add your feature to main.features[] in the order it should print
  - If you need more card data than is currently scraped, add it in MarketData.analysis_per_rarity().new_card
  - I decided to add 'utilities' to MarketData as well. Try and follow the pattern for now, or suggest a new pattern. I'm new to python!
- Make a pull request!

## Contributors

- Built on the work done by Reddit's u/THE_DQ, u/vadash, and u/messyhess.
- Maintained by @FraserHaer