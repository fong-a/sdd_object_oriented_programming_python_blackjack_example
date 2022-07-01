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

class Player:
    def __init__(self):
        # attributes
        self.name = ""
        self.score = ""
