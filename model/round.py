"""
A module to model a round of blackjack
"""

from model.constants import RoundResult
from model.constants import RoundStatus


class Round:
    """
    A representation of a dealer of cards.

    Attributes
    ----------
    status : RoundStatus
        The current status of the round
    result : RoundResult
        The current result of the round

    Methods
    -------
    evaluate : None
        Evaluates the status and result of the round
    """
    def __init__(
        self,
    ):
        """
        Initialises a new round
        """
        self._player_hand = []
        self._house_hand = []
        self._status = RoundStatus.LIVE
        self._result = RoundResult.HOUSE

    @property
    def status(
        self,
    ):
        """
        The current status of the round
        """
        return self._status

    @property
    def result(
        self,
    ):
        """
        The current result of the round
        """
        return self._result

    @property
    def player_hand(
        self,
    ):
        """
        The player's hand
        """
        return self._player_hand

    @property
    def house_hand(
        self,
    ):
        """
        The house's hand
        """
        return self._house_hand

    def evaluate(
        self,
    ):
        """
        Evaluates the current status and result of the round
        """
        status = RoundStatus.LIVE
        result = RoundResult.HOUSE
        if self._house_hand.is_blackjack():
            status = RoundStatus.DEAD
            if self._player_hand.is_blackjack():
                result = RoundResult.PUSH
        else:
            if self._player_hand.is_bust():
                status = RoundStatus.DEAD
            else:
                if self._house_hand.is_bust():
                    status = RoundStatus.DEAD
                    result = RoundResult.PLAYER
                else:
                    if self._house_hand.max_value() < self._player_hand.max_value():
                        result = RoundResult.PLAYER
                    elif self._house_hand.max_value() == self._player_hand.max_value():
                        result = RoundResult.PUSH
        self._status = status
        self._result = result
