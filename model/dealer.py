"""
A module to model a dealer of cards.
"""

from model.deck import Deck
from model.hand import Hand
from model.round import Round


class Dealer:
    """
    A representation of a dealer of cards.

    Properties
    ----------
    round : Round
        The current round

    Methods
    -------
    start_round : None
        Initialises a new round
    hit_player : None
        Deal a card to the player's hand
    hit_house : None
        Deal a card to the house's hand
    """
    def __init__(
        self,
        deck_multiple=1,
    ):
        """
        Initialises a new dealer
        """
        if not isinstance(deck_multiple, int):
            raise TypeError("Parameter 'deck_multiple' is not of 'int' type")
        if not deck_multiple:
            raise TypeError("Parameter 'deck_multiple' is not greater than zero")
        self._deck_multiple = deck_multiple
        self._renew_deck()
        self._round = None

    @property
    def round(
        self,
    ):
        """
        The current round
        """
        return self._round

    def _renew_deck(
        self,
    ):
        self._deck = Deck.build_multi_deck(self._deck_multiple)
        self._deck.shuffle()

    def start_round(
        self,
    ):
        """
        Starts a new round
        """
        self._renew_deck()
        player_cards = [self._deck.draw()]
        house_cards = [self._deck.draw()]
        player_cards.append(self._deck.draw())
        house_cards.append(self._deck.draw())
        player_hand = Hand(player_cards)
        house_hand = Hand(house_cards)
        self._round = Round(player_hand, house_hand)

    def hit_player(
        self,
    ):
        """
        Deals a card to the player
        """
        self._round.player_hand.add(self._deck.draw())

    def hit_house(
        self,
    ):
        """
        Deals a card to the house
        """
        self._round.house_hand.add(self._deck.draw())
