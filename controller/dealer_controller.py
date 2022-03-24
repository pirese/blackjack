from model.constants import HOUSE_STICKS_ON
from model.constants import MAX_HAND_VALUE
from model.constants import RoundStatus
from model.constants import Choice
from model.dealer import Dealer
from view.round_view import RoundView
import msvcrt


"""
A module to control a dealer of cards.
"""


class DealerController:
    """
    A controller for a dealer of cards.

    Methods
    ----------
    start_round : None
        Tells the dealer to start a new round
    play_house_hand : None
        Tells the dealer to play the house hand
    display_round : None
        Displays the current round
    """
    def __init__(
        self,
    ):
        """
        Initialises a new dealer controller
        """
        self._dealer = Dealer()
        self._roundView = None
        
    def start_round(
        self,
    ):
        """
        Tell the dealer to start a new round
        """
        self._dealer.start_round()
        self._roundView = RoundView(self._dealer.round)
        self._roundView.welcome()

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

    def play_player_hand(
        self,
    ):
        while not self._dealer.round.status == RoundStatus.DEAD:
            self._ask_player()
            choice = int(input())
            if choice == Choice.STICK.value:
                break
            elif choice == Choice.HIT.value:
                self._dealer.hit_player()
                self.view_round()

    def _ask_player(
        self,
    ):
        if not self._dealer.round.player_hand.is_bust:
            if not self._dealer.round.player_hand.is_blackjack:
                self._roundView.ask_player()

    def view_round(
         self,
    ):
        """
        Displays the round
        """
        self._roundView.view()
