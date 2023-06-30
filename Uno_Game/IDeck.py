from ICard import ICard
import random


class IDeck:
    def __init__(self):
        self.colors = ['Red', 'Green', 'Blue', 'Yellow']
        self.values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Skip', 'Reverse', 'Draw Two']
        self.cards = self.generate_deck()

    def generate_deck(self):
        cards = []
        for color in self.colors:
            cards.append(ICard(color, 0))
            for value in self.values[1:]:
                cards.append(ICard(color, value))
                cards.append(ICard(color, value))

        return cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
