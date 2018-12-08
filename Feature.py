import abc

# if your feature needs information stored on the cards, please add it to MarketData.py

class Feature(abc.ABC):
    @abc.abstractmethod
    def print(self, card_data):
        pass
    
