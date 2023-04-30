from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])

class HarryDeck:
    ranks = [str(i) for i in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) 
                       for rank in self.ranks 
                       for suit in self.suits]
        
    def __len__(self):
        return len(self._cards)
    
    # use this for get some item from class
    def __getitem__(self, position):
        return self._cards[position]
    
beer_card = Card('6', 'diamonds')
print('beer_card:', beer_card)

deck = HarryDeck()
print('len(deck):', len(deck))

print('deck[0]:', deck[0])

a = 0

# === Sorting ====
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0) # given rank of card

def spades_high(card):
    rank_values = HarryDeck.ranks.index(card.rank)
    # look that what card number are + additional rank from suit_values
    return rank_values * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)


