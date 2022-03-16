"""
This module models a playing card.
"""

from abc import ABC, abstractmethod
from enum import Enum


class Suit(Enum):
    """
    The allowed suits for a playing card.
    """
    SPADES = 1
    HEARTS = 2
    CLUBS = 3
    DIAMONDS = 4


class Rank(Enum):
    """
    The allowed ranks for a playing card.
    """
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card(ABC):
    """
    An abstract class representing a playing card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        if not isinstance(suit, Suit):
            raise TypeError("Parameter 'suit' is of invalid type")
        self.suit = suit
        if not isinstance(rank, Rank):
            raise TypeError("Parameter 'rank' is of invalid type")


    @property
    def suit_symbol(self):
        """
        Gets the first letter of the suit name e.g D for Diamonds
        """
        return  self.suit.name[0]


    @property
    def suit_name(self):
        """
        Gets the name of the suit
        """
        return  self.suit.name


    @property
    @abstractmethod
    def rank_symbol(self):
        """
        Gets the symbol representing the rank of the card e.g. A, 6, Q.
        """


class NumberCard(Card):
    """
    A class representing a numbered playing card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        super().__init__(suit, rank)
        allowed_ranks = [rank.value for rank in Rank][1:10]
        if not rank.value in allowed_ranks:
            raise ValueError('Rank ' + rank.name + ' is not a valid rank for a number card')
        self.rank = rank


    @property
    def rank_symbol(self):
        """
        Gets the symbol representing the value of the numbered card e.g. 2, 3.
        """
        return str(self.rank.value)


class FaceCard(Card):
    """
    A class representing a faced playing card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        super().__init__(suit, rank)
        allowed_ranks = [rank.value for rank in Rank][10:]
        if not rank.value in allowed_ranks:
            raise ValueError('Rank ' + rank.name + ' is not a valid rank for a face card')
        self.rank = rank


    @property
    def rank_symbol(self):
        """
        Gets the symbol representing the value of the face card e.g. J, Q.
        """
        return self.rank.name[0]


class AceCard(Card):
    """
    A class representing an ace playing card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        super().__init__(suit, rank)
        if rank.value != rank.ACE.value:
            raise ValueError('Rank ' + rank.name + ' is not a valid rank for an ace card')
        self.rank = rank


    @property
    def rank_symbol(self):
        """
        Gets the symbol representing the value of the face card i.e. A.
        """
        return self.rank.name[0]
