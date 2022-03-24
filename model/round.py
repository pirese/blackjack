"""
A module to model a round of blackjack
"""

from model.constants import RoundResult
from model.constants import RoundStatus
from model.hand import Hand


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
    TODO
    """
    def __init__(
        self,
        player_cards,
        house_cards,
    ):
        """
        Initialises a new round
        """
        self._player_hand = Hand(player_cards)
        self._house_hand = Hand(house_cards)

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

    @property
    def status(
        self,
    ):
        """
        The current status of the round
        """
        status = RoundStatus.LIVE
        if self._house_hand.is_blackjack:
            status = RoundStatus.DEAD
        else:
            if self._player_hand.is_bust:
                status = RoundStatus.DEAD
            else:
                if self._house_hand.is_bust:
                    status = RoundStatus.DEAD
        return status

    @property
    def result(
        self,
    ):
        """
        The current result of the round
        """
        result = RoundResult.HOUSE
        if self._house_hand.is_blackjack:
            if self._player_hand.is_blackjack:
                result = RoundResult.PUSH
        else:
            if not self._player_hand.is_bust:
                if self._house_hand.is_bust:
                    result = RoundResult.PLAYER
                else:
                    if self._house_hand.max_value < self._player_hand.max_value:
                        result = RoundResult.PLAYER
                    elif self._house_hand.max_value == self._player_hand.max_value:
                        result = RoundResult.PUSH
        return result
