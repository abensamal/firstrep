import collections
from random import choice
#first
#second
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:

	ranks = [str(n) for n in range(2,11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
										for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]
	
beer_card = Card('7', 'diamonds')
deck = FrenchDeck()

print(beer_card)
print(len(deck))
print(deck[:3])
print(deck[12::13])
print(choice(deck))

for card in deck:
	print(card)

for card in reversed(deck):
	print(card)


