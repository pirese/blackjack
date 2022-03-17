"""
A module to model a deck of playing cards.
"""

from model.card import AceCard
from model.card import FaceCard
from model.card import NumberCard
from model.card import Suit
from model.card import Rank


class Deck:
    """
    A representation of a deck of cards.

    Methods
    ----------
    build_multi_deck : list of Card
        Build a deck comprised of many standard decks
    """
    def __init__(
        self,
    ):
        """
        Initialises a new deck of cards
        """
        cards = []
        for suit in Suit:
            for rank in Rank:
                if rank.value == Rank.ACE.value:
                    cards.extend(AceCard(suit, rank))
                elif rank.value <= Rank.TEN.value:
                    cards.extend(NumberCard(suit, rank))
                else:
                    cards.extend(FaceCard(suit, rank))
        self._cards = cards

    @classmethod
    def build_multi_deck(cls, multiple):
        """
        Factory method to generate a deck of cards comprised of many standard decks.

        Parameters
        ----------
        multiple : int
            The number of times to multiply a standard deck.

        Returns
        -------
        Deck
            A deck of cards comprised of many standard decks.
        """
        deck = cls()
        deck._cards = [card for card in deck._cards for i in range(multiple)]
        return deck
