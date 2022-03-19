"""
A module to model a deck of playing cards.
"""

import random
from model.constants import Suit
from model.constants import Rank
from model.card import Card
from model.card import AceCard
from model.card import FaceCard
from model.card import NumberCard


class Deck:
    """
    A representation of a deck of cards.

    Attributes
    ----------
    size : int
        The number of cards currently in the deck

    Methods
    -------
    build_multi_deck : list of Card
        Factory method to build a deck comprised of many standard decks
    shuffle : None 
        Shuffles the deck
    draw : Card
        Draws a card from the deck
    replace : None
        Replaces a card back into the deck at the bottom
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
                    cards.append(AceCard(suit, rank))
                elif rank.value <= Rank.TEN.value:
                    cards.append(NumberCard(suit, rank))
                else:
                    cards.append(FaceCard(suit, rank))
        self._cards = cards

    @property
    def size(self):
        """
        The number of cards currently in the deck

        Returns
        -------
        int
            The number of cards in the deck.
        """
        return len(self._cards)

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
        deck : Deck
            A deck of cards comprised of many standard decks.
        """
        deck = cls()
        deck._cards = [card for card in deck._cards for _ in range(multiple)]
        return deck

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self._cards)

    def draw(self):
        """
        Draws a card from the deck

        Returns
        -------
        Card
            A card from the top of the deck
        """
        if not self._cards:
            raise IndexError("Deck is empty; dealer has not returned the cards!")
        card = self._cards.pop(0)
        return card

    def replace(self, card):
        """
        Place a card back into the deck at the bottom

        Parameters
        ----------
        card
            The card to be placed back into the deck
        """
        if not issubclass(type(card), Card):
            raise TypeError("Parameter 'card' is not of 'Card' type")
        self._cards.append(card)
