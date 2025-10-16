import random

class Card:
    values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10, 'A': 11
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(s, r) for s in suits for r in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if not self.cards:
            raise ValueError("No cards left in the deck!")
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value +=card.value
        if card.rank == "A":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10 
            self.aces -= 1

class Chips:
    def __init__(self,total = 100):
        self.total = total
        self.bet=0
    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

class Player:
    def __init__(self,name = "player",chips=100):
        self.name=name
        self.chips=Chips(chips)
        self.hand = Hand()
        
    def hit(self,deck):
        self.hand.add_card(deck.deal())

    def place_bet(self,amount):
        if amount > self.chips.total:
            raise ValueError("Not enough chips to bet!")
        self.chips.bet = amount

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def play(self, deck):
        while self.hand.value < 17:
            self.hand.add_card(deck.deal())


def play_blackjack():
    c=1
    while you.chips.total>0:
        deck = Deck()
        deck.shuffle()

        you = Player()
        dealer = Dealer()

        you.place_bet(10)

        for _ in range(2):
            you.hit(deck)
            dealer.hand.add_card(deck.deal())

        print("\nDealer's Hand: <hidden card>,", dealer.hand.cards[1])
        print("Player's Hand:", ', '.join(str(card) for card in you.hand.cards))
        print("Player's value:", you.hand.value)

        while you.hand.value < 21:
            move = input("Hit or stand? (h/s): ").lower()
            if move == 'h':
                you.hit(deck)
                print("You drew:", you.hand.cards[-1])
                print("Total value:", you.hand.value)
            else:
                break

        if you.hand.value > 21:
            print("You bust!")
            you.chips.lose_bet()
        else:
            dealer.play(deck)
            print("Dealer's Hand:", ', '.join(str(card) for card in dealer.hand.cards))
            print("Dealer's value:", dealer.hand.value)

            if dealer.hand.value > 21 or dealer.hand.value < you.hand.value:
                print("You win!")
                you.chips.win_bet()
            elif dealer.hand.value > you.hand.value:
                print("Dealer wins.")
                you.chips.lose_bet()
            else:
                print("Push (tie).")

        print(f"Your total chips: {you.chips.total}")

if __name__ == "__main__":
    play_blackjack()