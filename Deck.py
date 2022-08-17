import random
class Deck:
    suits= [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
    nums = list(range(2, 10))
    faces = ["T", "J", "Q", "K", "A"]

    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        for num in Deck.nums:
            for suit in Deck.suits:
                card = str(num)+suit
                deck.append(card)
        for face in Deck.faces:
            for suit in Deck.suits:
                card = face+suit
                deck.append(card)

        return deck

    def deck_shuffle(self):
        return random.shuffle(self.deck)
        
    def deal(self):
        
        card = self.deck.pop()
           

        return card

    def restart_deck(self):
        self.deck = self.create_deck()


# """ deck = Deck()
# deck.deck_shuffle()
# hand = deck.deal(15)
# print(hand)
# for card in hand:
#     if card in deck.deck:
#         print("the card is in both places")
#     else:
#         print("OK")
# print(deck.deck)
# print(len(deck.deck))
#  """