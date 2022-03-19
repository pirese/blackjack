"""
A module to model a dealer of cards.
"""

from enum import Enum
from model.deck import Deck


class RoundResult(Enum):
    """
    The possible outcomes of a round
    """
    HOUSE = 1
    PLAYER = 2
    PUSH = 3


class Dealer:
    """
    A representation of a dealer of cards.

    Methods
    ----------
    deal : None
        Deal a card to a hand
    """
    def __init__(
        self,
        deck_multiple = 1,
    ):
        """
        Initialises a new dealer
        """
        if not isinstance(deck_multiple, int)
            raise TypeError("Parameter 'deck_multiple' is not of 'int' type")
        if not deck_multiple:
            raise TypeError("Parameter 'deck_multiple' is not greater than zero")
        self._deck = Deck.build_multi_deck(deck_multiple)
        self._deck_multiple = deck_multiple
        self._deck.shuffle()

    @property
    def player_hand(
        self,
    ):
        """
        The player's hand
        """
        return self._player_hand

    @property
    def player_hand(
        self,
    ):
        """
        The player's hand
        """
        return self._player_hand

    def start_round(
        self,
    ):
        """
        Starts a new round
        """
        self._deck = Deck.build_multi_deck(self._deck_multiple)
        self._deck.shuffle()
        self._player_hand = []
        self._house_hand = []
        self.hit_player()
        self.hit_house()
        self.hit_player()
        self.hit_house()

    def hit_player(
        self,
    ):
        """
        Deals a card to the player
        """
        self._player_hand.append(self._deck.draw())

    def hit_house(
        self,
    ):
        """
        Deals a card to the house
        """
        self._house_hand.append(self._deck.draw())

    @property
    def round_result(
        """
        The current outcome of the round
        """
        result = RoundResult.HOUSE
        if self._house_hand.isblackjack():
            if self._player_hand.isblackjack():
                result = RoundResult.PUSH
        else:
            if not self._player_hand.isbust():
                if self._house_hand.isbust():
                    result = RoundResult.Player
                else:
                    if self._house_hand.max_value() < \
                       self._player_hand.max_value():
                        result = RoundResult.Player
                    else:
                        result = RoundResult.Push
        return result

