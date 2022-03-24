"""
A module to model a playing card.
"""

import abc
from model.constants import Suit
from model.constants import Rank


class Card(abc.ABC):
    """
    An abstract representation of a playing card.

    Attributes
    ----------
    suit_symbol : str
        The symbol representing the suit name e.g D for Diamonds.
    suit_name : str
        The name of the suit
    rank_symbol : str
        The symbol representing the rank of the card
    min_blackjack_value : int
        The minimum numeric value of the card in blackjack
    max_blackjack_value : int
        The maximum numeric value of the card in blackjack
    short_name : str
        A string shorthand name for the card
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
    @abc.abstractmethod
    def min_blackjack_value(self):
        """
        The minimum numeric value of the card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """

    @property
    @abc.abstractmethod
    def max_blackjack_value(self):
        """
        The maximum numeric value of the card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
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

    Attributes
    ----------
    rank_symbol : str
        The symbol representing the rank of the card
    min_blackjack_value : int
        The minimum numeric value of the card in blackjack
    max_blackjack_value : int
        The maximum numeric value of the card in blackjack
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

    @property
    def min_blackjack_value(self):
        """
        The minimum numeric value of the numbered card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """
        return self._rank.value

    @property
    def max_blackjack_value(self):
        """
        The maximum numeric value of the numbered card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """
        return self._rank.value


class FaceCard(Card):
    """
    A representation of a faced card.

    Attributes
    ----------
    rank_symbol : str
        The symbol representing the rank of the card
    min_blackjack_value : int
        The minimum numeric value of the card in blackjack
    max_blackjack_value : int
        The maximum numeric value of the card in blackjack
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

    @property
    def min_blackjack_value(self):
        """
        The minimum numeric value of the faced card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """
        return Rank.TEN.value

    @property
    def max_blackjack_value(self):
        """
        The maximum numeric value of the faced card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """
        return Rank.TEN.value


class AceCard(Card):
    """
    A representation of an ace card.

    Attributes
    ----------
    rank_symbol : str
        The symbol representing the rank of the card
    min_blackjack_value : int
        The minimum numeric value of the card in blackjack
    max_blackjack_value : int
        The maximum numeric value of the card in blackjack
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

    @property
    def min_blackjack_value(self):
        """
        The minimum numeric value of the ace card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """
        return Rank.ACE.value

    @property
    def max_blackjack_value(self):
        """
        The maximum numeric value of the ace card in blackjack.

        Returns
        -------
        int
            A numeric value for the card.
        """
        return Rank.TEN.value + 1
