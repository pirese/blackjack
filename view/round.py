"""
A module to view a round of blackjack.
"""

SEPARATOR = "--------------------"


class Round:
    """
    A view of a hand in blackjack.
    """

    def __init__(
        self,
        round,
    ):
        """
        TODO
        """
        self._round = round

    def display(
        self,
    ):
        """
        Display the current round
        """
        print(SEPARATOR)
        self._print_cards()
        self._print_result()

    def _print_cards(self):
        print("Player: " + self._cards_string(self._round.player_hand.cards))
        print("House : " + self._cards_string(self._round.house_hand.cards))

    def _print_result(self):
        print("Result: " + self._round.result.name)

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
