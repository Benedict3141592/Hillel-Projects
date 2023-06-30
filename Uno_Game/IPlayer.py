class IPlayer:
    def __init__(self, name: str):
        self.name = name
        self.hand = []

    def draw_card(self, deck):
        card = deck.draw_card()
        self.hand.append(card)

    def play_card(self, card_index, rebound):
        card = self.hand.pop(card_index)
        rebound.append(card)

    def has_cards(self):
        return len(self.hand) != 0
