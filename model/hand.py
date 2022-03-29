"""
A module to model a hand in blackjack.
"""

from model.constants import MAX_HAND_VALUE
from model.constants import Rank


class Hand:
    """
    A representation of a hand in blackjack.

    Properties
    ----------
    cards : list of Card
        The cards comprising the hand.
    min_value : int
        The minimum numeric value of the hand
    max_value : int
        The maximum non-bust value of the hand
    is_bust : bool
        Whether the hand is bust
    is_blackjack : bool
        Whether the hand is blackjack

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
        """
        The cards in the hand

        Returns
        -------
        list of Card
            The cards in the hand.
        """
        return self._cards

    @property
    def min_value(self):
        """
        The minimum value of the hand

        Returns
        -------
        int
            The minimum value of the hand.
        """
        value = 0
        for card in self._cards:
            value += card.min_blackjack_value
        return value

    @property
    def max_value(self):
        """
        The maximum non-bust value of the hand

        Returns
        -------
        int
            The maximum value of the hand.
        """
        value = 0
        aces = 0
        for card in self._cards:
            if card.min_blackjack_value == Rank.ACE.value:
                aces += 1
            value += card.max_blackjack_value
        if aces > 1:
            value = value - (aces - 1) * Rank.TEN.value
        if value > MAX_HAND_VALUE:
            return self.min_value
        else:
            return value

    @property
    def is_bust(self):
        """
        Whether the hand is bust

        Returns
        -------
        bool
            Whether the hand is bust.
        """
        return \
            (self.min_value > MAX_HAND_VALUE and
             self.max_value > MAX_HAND_VALUE)

    @property
    def is_blackjack(self):
        """
        Whether the hand is blackjack

        Returns
        -------
        bool
            Whether the hand is blackjack.
        """
        return \
            (len(self._cards) == 2 and
             self.max_value == MAX_HAND_VALUE)

    def add(self, card):
        """
        Add a card to the hand
        """
        self._cards.append(card)
