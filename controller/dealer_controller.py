"""
A module to control a dealer of cards.
"""


class DealerController:
    """
    A controller for a dealer of cards.
    """
    def __init__(
        self,
        dealer,
    ):
        """
        Initialises a new dealer controller
        """
        self._dealer = dealer 
        
    def start_round(
        self,
    ):
        """
        Tell the dealer to start a new round
        """
        self._dealer.start_round()

    def 
