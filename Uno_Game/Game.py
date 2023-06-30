from IDeck import IDeck
from IPlayer import IPlayer


class UnoGame:
    def __init__(self, players_name: list):
        self.deck = IDeck()
        self.deck.shuffle()
        self.rebound = []
        self.current_player_index = 0
        self.direction = 1
        self.players = [IPlayer(name) for name in players_name]

    def start_game(self):
        self.deal_cards()
        self.play_game()

    def deal_cards(self):
        for num in range(7):
            for player in self.players:
                player.draw_card(self.deck)
        self.rebound.append(self.deck.draw_card())

    def print_info(self):
        last_card = self.rebound[-1]
        print(f"Current card: {last_card}")
        print("Current hand:")
        for index, card in enumerate(self.players[self.current_player_index].hand):
            print(f"{index + 1}. {card}")

    def check_card(self, player):
        last_card = self.rebound[-1]
        for card in player.hand:
            if card.color == last_card.color or card.value == last_card.value:
                return True
        return False

    def next_player(self):
        self.current_player_index += self.direction
        if self.current_player_index < 0:
            self.current_player_index = len(self.players) - 1
        elif self.current_player_index >= len(self.players):
            self.current_player_index = 0

    def get_next_player(self):
        next_player_index = self.current_player_index + self.direction
        if next_player_index < 0:
            next_player_index = len(self.players) - 1
        elif next_player_index >= len(self.players):
            next_player_index = 0
        return self.players[next_player_index]

    def card_effect(self, card):
        if card.value == 'Reverse':
            self.direction *= -1
        elif card.value == 'Skip':
            self.next_player()
        elif card.value == 'Draw Two':
            next_player = self.get_next_player()
            for num in range(2):
                next_player.draw_card(self.deck)
            self.next_player()

    def turn(self, player):
        valid_play = False

        while not valid_play:
            card_index = self.get_valid_index(player)
            card = player.hand[card_index]

            if self.is_valid(card):
                player.play_card(card_index, self.rebound)
                valid_play = True
                self.card_effect(card)
            else:
                print("Invalid card. Please try again.")

    @staticmethod
    def get_valid_index(player):
        while True:
            try:
                card_input = int(input("Enter the index of the card you want to play: ")) - 1
                if 0 <= card_input < len(player.hand):
                    return card_input
                else:
                    print("Invalid card index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def is_valid(self, card):
        last_card = self.rebound[-1]
        return card.color == last_card.color or card.value == last_card.value

    def play_game(self):
        game_over = False
        while not game_over:
            current_player = self.players[self.current_player_index]
            print(f"\nCurrent player: {current_player.name}")
            self.print_info()

            if not self.check_card(current_player):
                print("No playable cards.")
                current_player.draw_card(self.deck)

                drawn_card = current_player.hand[-1]
                print(f"\nDrawn card: {drawn_card}")
                self.print_info()

            if self.check_card(current_player):
                self.turn(current_player)
            else:
                print("Still no playable cards. Turn skipped.")

            if not current_player.has_cards():
                game_over = True
                print(f"\n{current_player.name} wins!")

            self.next_player()


players = ["Pele", "Messi", "Ronaldo"]
game = UnoGame(players)
game.start_game()
