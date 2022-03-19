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
    shuffle : None
        Shuffles the deck
    draw : Card
        Draws a card from the deck
    replace : None
        Replaces a card back into the deck at the bottom
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
