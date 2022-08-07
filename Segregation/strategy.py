import random

from abc import ABC, abstractmethod
from typing import List

class Card:
    def __init__(self, number: int):
        self.number = number


class CardOrderingStrategy(ABC):
    @abstractmethod
    def order(self, card_list: List[Card]) -> List[Card]:
        pass


class FIFOOrderingStrategy(CardOrderingStrategy):
    def order(self, card_list: List[Card]) -> List[Card]:
        return card_list.copy()

class FILOOrderingStrategy(CardOrderingStrategy):
    def order(self, card_list: List[Card]) -> List[Card]:
        copied_list = card_list.copy()
        copied_list.reverse()
        return copied_list

class RandomOrderingStrategy(CardOrderingStrategy):
    def order(self, card_list: List[Card]) -> List[Card]:
        copied_list = card_list.copy()
        random.shuffle(copied_list)
        return copied_list


class CardGameSupporter:
    def __init__(self, ordering_strategy: CardOrderingStrategy):
        self.card_list = []
        self.ordering_strategy = ordering_strategy

    def add_card(self, number: int):
        self.card_list.append(Card(number))

    def offer_card_list(self):
        mixed_card_list = self.ordering_strategy.order(self.card_list)
        
        for card in mixed_card_list:
            print(f'Card number : {card.number}')


card_game_supporter = CardGameSupporter(FIFOOrderingStrategy())
#card_game_supporter = CardGameSupporter(FILOOrderingStrategy())
#card_game_supporter = CardGameSupporter(RandomOrderingStrategy())

card_game_supporter.add_card(1)
card_game_supporter.add_card(2)
card_game_supporter.add_card(3)
card_game_supporter.add_card(4)

card_game_supporter.offer_card_list()