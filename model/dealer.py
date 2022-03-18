"""
A module to model a dealer of cards.
"""

from model.deck import Deck


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
        self._deck.shuffle()
        self._draw_counter = 0

