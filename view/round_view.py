"""
A module to view a round of blackjack.
"""


SEPARATOR = "--------------------"


class RoundView:
    """
    A view of a round of blackjack.
    """
    def __init__(
        self,
        round,
    ):
        """
        Initialises a view of a round

        Parameters
        ----------
        round : Round
            The round of blackjack
        """
        self._round = round

    @staticmethod
    def welcome():
        """
        Display the current round
        """
        print(SEPARATOR)
        print("Starting a new round")

    def view(
        self,
    ):
        """
        Display the current round
        """
        print(SEPARATOR)
        self._print_hand()
        self._print_result()

    def _print_hand(
        self,
    ):
        player_hand = self._cards_string(self._round.player_hand.cards)
        player_hand += self._values_string(self._round.player_hand)
        house_hand = self._cards_string(self._round.house_hand.cards)
        house_hand += self._values_string(self._round.house_hand)
        print("Player : " + player_hand)
        print("House  : " + house_hand)

    def _print_result(
        self,
    ):
        print("Result : " + self._round.result.name)

    @staticmethod
    def ask_player():
        """
        Ask the player for input
        """
        print(SEPARATOR)
        print("1) Stick or 2) Hit")

    @staticmethod
    def _values_string(
        hand,
    ):
        values_string = " ("
        if hand.min_value == hand.max_value:
            values_string += str(hand.max_value)
        else:
            values_string += str(hand.min_value)
            values_string += "/" + str(hand.max_value)
        values_string += ")"
        return values_string

    @staticmethod
    def _cards_string(
        cards,
    ):
        cards_string = ""
        card_no = -1
        for card in cards:
            card_no += 1
            cards_string += card.short_name
            if card_no != len(cards) - 1:
                cards_string += ", "
        return cards_string
