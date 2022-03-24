"""
A module containing constants for the model
"""


from enum import Enum


MAX_HAND_VALUE = 21
HOUSE_STICKS_ON = 17


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


class RoundResult(Enum):
    """
    The outcome of a round
    """
    HOUSE = 1
    PLAYER = 2
    PUSH = 3
    UNKNOWN = 4


class RoundStatus(Enum):
    """
    The status of a round
    """
    LIVE = 1
    DEAD = 2
