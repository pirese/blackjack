from model.deck import Deck

number_of_decks = 1
deck = Deck.build_multi_deck(number_of_decks)
deck.shuffle()

print('\n'.join(card.short_name for card in deck.cards))
