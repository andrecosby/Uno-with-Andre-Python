NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw Two", "Skip", "Reverse"]
COLORS = ["🔴","🟢","🟡","🔵" ]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   


class Player:
    def __init__(self, name):
        self.name = name 
        self.hand = []

        def_str_(self):
            return f'{self.name}'


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)
        

    def shuffle(self):
        shuffle_deck:list = []
        deck_to_shuffle = self.cards.copy()
    while len(deck_to_shuffle) > 0:
        card_to_deal = deck_to_shuffle [randint(0,len(deck_to_shuffle) -1)]
        deck_to_shuffle.remove(card_to_deal)
        shuffle_deck.append(card_to_deal)
    return shuffle_deck

class Game:
    def __init___(self):
        self.deck = Deck(NUMBERS, COLORS).shuffle()
        self.player1 = Player("Sophia")
        self.player2 = Player("Sim-One")
        for card in self.deck:
            print(card)
        print(self.player1, self.player2)


