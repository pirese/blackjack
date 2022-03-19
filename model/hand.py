"""
A module to model a hand in blackjack.
"""

from model.card import Rank
from model.card import AceCard


MAX_VALUE = 21


class Hand:
    """
    A representation of a hand in blackjack.
    """
    def __init__(
        self,
        cards,
    ):
        """
        Initialises a new hand
        """
        self._cards = cards
    
    @property
    def cards(self):
        return self._cards

    @property
    def min_value(self):
        value = 0
        for card in self._cards:
            value += card.min_blackjack_value
        return value

    @property
    def max_value(self):
        """
        The maximum non-bust value of the hand
        """
        value = 0
        aces = 0
        for card in self._cards:
            if isinstance(card, AceCard):
                aces += 1
            value += card.max_blackjack_value
        if aces > 1:
            value = value - (aces - 1) * Rank.TEN.value
        return value

    @property
    def isbust(self):
        return \
            self.min_value > MAX_VALUE and \
            self.max_value > MAX_VALUE

    @property
    def isblackjack(self):
        return \
            len(self._cards == 2 and \
            self.max_value == MAX_VALUE

    def add(self, card):
        self._cards.append(card)

