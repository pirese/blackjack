from model.constants import HOUSE_STICKS_ON
from model.constants import MAX_HAND_VALUE
from model.dealer import Dealer
from view.round import Round

"""
A module to control a dealer of cards.
"""


class DealerController:
    """
    A controller for a dealer of cards.

    Methods
    ----------
    start_round : None
        Tell the dealer to start a new round
    """
    def __init__(
        self,
    ):
        """
        Initialises a new dealer controller
        """
        self._dealer = Dealer()
        
    def start_round(
        self,
    ):
        """
        Tell the dealer to start a new round
        """
        self._dealer.start_round()

    def play_house_hand(
        self,
    ):
        """
        Tells the dealer to play the house hand up to the target
        """
        while self._dealer.round.house_hand.max_value < HOUSE_STICKS_ON:
            self._dealer.hit_house()
        if self._dealer.round.house_hand.max_value > MAX_HAND_VALUE and \
           not self._dealer.round.house_hand.is_bust:
            while self._dealer.round.house_hand.min_value < HOUSE_STICKS_ON:
                self._dealer.hit_house()

    def display_round(
         self,
    ):
        """
        TODO
        """
        Round(self._dealer.round).display()
