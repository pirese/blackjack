"""
A module to model a deck of playing cards.
"""

import random

from model.card import Card
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
                    cards.append(AceCard(suit, rank))
                elif rank.value <= Rank.TEN.value:
                    cards.append(NumberCard(suit, rank))
                else:
                    cards.append(FaceCard(suit, rank))
        self._cards = cards
        self._draw_counter = 0

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
        deck._cards = [card for card in deck._cards for i in range(multiple)]
        return deck

    @property
    def size(self):
        """
        Gets the number of cards currently in the deck

        Returns
        -------
        int
            The number of cards in the deck.
        """
        return len(self._cards)

    @property
    def draw_counter(self):
        """
        Gets the number of cards drawn from the deck since the last shuffle

        Returns
        -------
        int
            The number of cards drawn from the deck.
        """
        return self._draw_counter

    def shuffle(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self._cards)
        self._draw_counter = 0

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
        self._draw_counter += 1
        return card

    def replace(self, card):
        """
        Place a card back into the deck at the bottom

        Parameters
        ----------
        card : Card
            The card to be placed back into the deck
        """
        if not issubclass(type(card), Card):
            raise TypeError("Parameter 'card' is not of 'Card' type")
        self._cards.append(card)
