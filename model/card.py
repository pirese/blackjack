"""
A module to model a playing card.
"""

import abc
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


class Card(abc.ABC):
    """
    An abstract representation of a playing card.

    Methods
    ----------
    suit_symbol : str
        The symbol representing the suit name e.g D for Diamonds.
    suit_name : str
        The name of the suit
    rank_symbol : str
        The symbol representing the rank of the card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        """
        Initialises a new card

        Parameters
        ----------
        suit : Suit
            The suit of the card
        rank : Rank
            The rank of the card
        """
        if not isinstance(suit, Suit):
            raise TypeError("Parameter 'suit' is not of 'Suit' type")
        self._suit = suit
        if not isinstance(rank, Rank):
            raise TypeError("Parameter 'rank' is not of 'Rank' type")

    @property
    def suit_symbol(self):
        """
        The symbol representing the suit name e.g D for Diamonds

        Returns
        -------
        str
            A single character string representing the suit name.
        """
        return self._suit.name[0]

    @property
    def suit_name(self):
        """
        The name of the suit

        Returns
        -------
        str
            The name of the suit.
        """
        return self._suit.name

    @property
    @abc.abstractmethod
    def rank_symbol(self):
        """
        The symbol representing the rank of the card e.g. A, 10, Q.

        Returns
        -------
        str
            A symbol representing the card rank.
        """

    @property
    def short_name(self):
        """
        A shorthand name for the card e.g. 2D for 2 of Diamonds

        Returns
        -------
        str
            A string shorthand name for the card
        """
        return self.rank_symbol + self.suit_symbol


class NumberCard(Card):
    """
    A representation of a numbered card.

    Methods
    ----------
    rank_symbol : str
        The symbol representing the rank of the card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        """
        Initialises a new numbered card

        Parameters
        ----------
        suit : Suit
            The suit of the card
        rank : Rank
            The rank of the card
        """
        super().__init__(suit, rank)
        allowed_ranks = [rank.value for rank in Rank][1:10]
        if rank.value not in allowed_ranks:
            raise ValueError('Rank ' + rank.name + ' is not a valid rank for a number card')
        self._rank = rank

    @property
    def rank_symbol(self):
        """
        The symbol representing the value of the numbered card i.e. 2-10.

        Returns
        -------
        str
            A symbol representing the card rank.
        """
        return str(self._rank.value)


class FaceCard(Card):
    """
    A representation of a faced card.

    Methods
    ----------
    rank_symbol : str
        The symbol representing the rank of the card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        """
        Initialises a new faced card

        Parameters
        ----------
        suit : Suit
            The suit of the card
        rank : Rank
            The rank of the card
        """
        super().__init__(suit, rank)
        allowed_ranks = [rank.value for rank in Rank][10:]
        if rank.value not in allowed_ranks:
            raise ValueError('Rank ' + rank.name + ' is not a valid rank for a face card')
        self._rank = rank

    @property
    def rank_symbol(self):
        """
        The symbol representing the value of the face card i.e. J, Q, K.

        Returns
        -------
        str
            A symbol representing the card rank.
        """
        return self._rank.name[0]


class AceCard(Card):
    """
    A representation of an ace card.

    Methods
    ----------
    rank_symbol : str
        The symbol representing the rank of the card
    """
    def __init__(
        self,
        suit,
        rank,
    ):
        super().__init__(suit, rank)
        if rank.value != rank.ACE.value:
            raise ValueError('Rank ' + rank.name + ' is not a valid rank for an ace card')
        self._rank = rank

    @property
    def rank_symbol(self):
        """
        The symbol representing the value of the ace card i.e. A.

        Returns
        -------
        str
            A symbol representing the card rank.
        """
        return self._rank.name[0]
