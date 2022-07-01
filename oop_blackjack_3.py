class PlayingCard:
    def __init__(self):
        # attributes
        self.suit = ""
        self.rank = ""
        self.value = ""
    
class Deck:
    def __init__(self):
        # attributes
        self.cards = [] # array of PlayingCard
    
    # methods
    def deal(self, num_cards):
        pass

class Player:
    def __init__(self, name):
        # attributes
        self.name = name
        self.score = ""

player_name = input("What is your name? ")
game_player = Player(player_name)
print(f"Welcome to the Game of Blackjack {game_player.name}")
