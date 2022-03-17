from model.card import AceCard
from model.card import FaceCard
from model.card import NumberCard
from model.card import Suit
from model.card import Rank

card = NumberCard(Suit.CLUBS, Rank.SEVEN)
print(card.rank.name)
