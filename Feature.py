import abc

# if your feature needs information stored on the cards, please add it to base_card_data.py

class Feature(abc.ABC):
    @abc.abstractmethod
    def print(self, card_data):
        pass
    