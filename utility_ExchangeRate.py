from Feature import Feature

from settings import exchange_rate, currency

class ExchangeRate(Feature):
    def __init__(self):
        if currency == "USD":
            self.exchange_rate = 1.0
        else:
            self.exchange_rate = exchange_rate

    def get_rate(self):
        return self.exchange_rate

    def print(self):
        if currency == "USD":
            print("Price is in USD")
        else:
            print(f"Using exchange rate of 1 USD = {self.exchange_rate:.2f} {currency}")
