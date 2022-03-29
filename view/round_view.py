"""
A module to view a round of blackjack.
"""


from model.constants import RoundStatus


SEPARATOR = "--------------------"


class RoundView:
    """
    A view of a round of blackjack.
    """
    def __init__(
        self,
        round_,
    ):
        """
        Initialises a view of a round

        Parameters
        ----------
        round_ : Round
            The round of blackjack
        """
        self._round = round_

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
        if self._round.status == RoundStatus.DEAD:
            self._print_result()

    def _print_hand(
        self,
    ):
        player_hand = self._cards_string(self._round.player_hand.cards)
        player_hand += self._values_string(self._round.player_hand)
        hide_value = self._round.status == RoundStatus.LIVE
        house_hand = self._cards_string(self._round.house_hand.cards, hide_value)
        house_hand += self._values_string(self._round.house_hand, hide_value)
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
        hide_value=False,
    ):
        values_string = " ("
        if hide_value:
            values_string += "??"
        elif hand.min_value == hand.max_value or hand.is_blackjack:
            values_string += str(hand.max_value)
        else:
            values_string += str(hand.min_value)
            values_string += "/" + str(hand.max_value)
        values_string += ")"
        return values_string

    @staticmethod
    def _cards_string(
        cards,
        hide_last=False,
    ):
        cards_string = ""
        card_no = 0
        for card in cards:
            if card_no < len(cards) - 1:
                cards_string += card.short_name
                cards_string += ", "
            else:
                if hide_last:
                    cards_string += "??"
                else:
                    cards_string += card.short_name
            card_no += 1
        return cards_string
