
# from Deck import Deck as D

# deck = D()

class Player:
    def __init__(self):
        self.money = 500
        self.hand = []


    def first_hand(self, deck):
        for _ in range(2):
            self.hit(deck)

    
    def hit(self, deck):
        card = deck.deal()
        self.hand.append(card)


    def sum_cards(self):
        
        nums = []
            
        for card in self.hand:
            num= card[0]

            if num.isdigit():
                nums.append(int(num))
            elif num == "A":
               nums.append(11)
            else:
                nums.append(10)
        if sum(nums) > 21:
            for i in range(len(nums)):
                if nums[i] == 11:
                    nums[i] = 1
                    continue 
        
        return sum(nums)

    def restart_hand(self):
        self.hand = []
class Dealer(Player):
    def __init__(self):
        self.hand = []


# p= Player()
# d = Dealer()

# print(p.money)

# deck.deck_shuffle()

# hand = p.first_hand()

# print(hand)
# print(p.sum_cards())
# p.hit()
# print(hand)
# print(p.sum_cards())
# p.hit()
# print(hand)
# print(p.sum_cards())
# p.hit()
# print(hand)
# print(p.sum_cards())