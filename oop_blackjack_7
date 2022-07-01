import random

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
    def deal(self, player):
        card_position = 0
        top_card = self.cards[card_position]
        player.hand.append(top_card)
        print(f"Your first card is {top_card.get_suit()}{top_card.get_rank()}")
        total_value = player.hand[0].value
        
        while total_value <= 21:
            print(f"Your score is {total_value}")
            card_position +=1
            choice = input("Stick or twist?...")
            if choice.lower() == "stick":
                break
            else:
                next_card = self.cards[card_position]
                player.hand.append(next_card)
                print(f"You draw a {next_card.get_suit()}{next_card.get_rank()}")
                total_value = 0
                for card in player.hand:
                    total_value += card.value
                if total_value > 21:
                    print("Bust!")
            
    def shuffle(self):
        random.shuffle(self.cards)
        print("Shuffling deck... ")
        input()
        print("Deck shuffled")

class Player:
    def __init__(self, name):
        # attributes
        self.name = name
        self.score = ""
        self.hand = []
        
    # getters
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    
    # setters
    def set_score(self,new_score):
        self.score = new_score
    
game_deck = Deck()
player_name = input("What is your name? ")
game_player = Player(player_name)
print(f"Welcome to the Game of Blackjack {game_player.name}")
game_deck.shuffle()
game_deck.deal(game_player)
