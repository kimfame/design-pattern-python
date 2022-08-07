from ast import Call
import random

from abc import ABC, abstractmethod
from typing import List, Callable


class Card:
    def __init__(self, number: int):
        self.number = number


class CardOrderingStrategy(ABC):
    @abstractmethod
    def order(self, card_list: List[Card]) -> List[Card]:
        pass


def fifo_ordering_strategy(card_list: List[Card]) -> List[Card]:
        return card_list.copy()

def filo_ordering_strategy(card_list: List[Card]) -> List[Card]:
        copied_list = card_list.copy()
        copied_list.reverse()
        return copied_list

def random_ordering_strategy(card_list: List[Card]) -> List[Card]:
        copied_list = card_list.copy()
        random.shuffle(copied_list)
        return copied_list

OrderingStrategyFunction = Callable[[List[Card]], List[Card]]

class CardGameSupporter:
    def __init__(self, ordering_strategy: OrderingStrategyFunction):
        self.card_list = []
        self.ordering_strategy = ordering_strategy

    def add_card(self, number: int):
        self.card_list.append(Card(number))

    def offer_card_list(self):
        mixed_card_list = self.ordering_strategy(self.card_list)
        
        for card in mixed_card_list:
            print(f'Card number : {card.number}')



def main() -> None:
    card_game_supporter = CardGameSupporter(fifo_ordering_strategy)
    #card_game_supporter = CardGameSupporter(filo_ordering_strategy)
    #card_game_supporter = CardGameSupporter(random_ordering_strategy)

    card_game_supporter.add_card(1)
    card_game_supporter.add_card(2)
    card_game_supporter.add_card(3)
    card_game_supporter.add_card(4)

    card_game_supporter.offer_card_list()


if __name__ == "__main__":
    main()