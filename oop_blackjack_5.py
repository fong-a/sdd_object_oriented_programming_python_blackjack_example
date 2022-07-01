class PlayingCard:
    def __init__(self, suit, rank, value):
        # attributes
        self.suit = suit
        self.rank = rank
        self.value = value
        
    # getters
    def get_suit(self):
        return self.suit
    def get_rank(self):
        return self.rank
    def get_value(self):
        return self.value

class Deck:
    def __init__(self):
        # attributes
        self.cards = [] # array of PlayingCard
        suits = ["♣️", "♦️","♥️","♠️"]
        ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
        for suit in suits:
            for rank in ranks:
                new_card = PlayingCard(suit,rank,values[ranks.index(rank)])
                self.cards.append(new_card)
    # getters
    def get_cards(self):
        return self.cards
    
    # methods
    def deal(self, num_cards):
        pass

class Player:
    def __init__(self, name):
        # attributes
        self.name = name
        self.score = ""
        
    # getters
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    
    # setters
    def set_score(self,new_score):
        pass
    
game_deck = Deck()
player_name = input("What is your name? ")
game_player = Player(player_name)
print(f"Welcome to the Game of Blackjack {game_player.name}")
for i in game_deck.cards:
    print(i.get_suit(), i.get_rank(), i.get_value())
