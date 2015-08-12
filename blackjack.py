# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
msg = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def drawBack(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], 
                          CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.card_list = []

    def __str__(self):
        # return a string representation of a hand
        cards = ""
        for card in self.card_list:
            cards = cards + str(card) + " "
        return "Hand contains " + cards

    def add_card(self, card):
        # add a card object to a hand
        self.card_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        ace = False
        val = 0
        for card in self.card_list:
            val += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                ace = True
        if ace and val <= 11:
            val += 10   
        return val
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.card_list:
            pos[0] = pos[0] + 40
            card.draw(canvas,pos)
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.card_deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.card_deck.append(Card(suit, rank))
       
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.card_deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.card_deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        deck_str = ""
        for card in self.card_deck:
            deck_str = deck_str + str(card) + " "
        return "Complete deck " + deck_str

#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, player, c_deck, score, msg
    
    if in_play:
        score -= 1
        in_play = False
        deal()
    else:
        in_play = True
        msg = ""
        outcome = "Hit or stand?"
        c_deck = Deck()
        c_deck.shuffle()
        player = Hand()
        dealer = Hand()
        for i in range(2):
            player.add_card(c_deck.deal_card())
            dealer.add_card(c_deck.deal_card())

def hit():   
    # if busted, assign a message to outcome, update in_play and score
    global outcome, in_play, score, msg
    if in_play:
        if player.get_value() <= 21:
            player.add_card(c_deck.deal_card())
            if player.get_value() > 21:
                msg = "You have busted"
                outcome = "Play again?"
                score -= 1
                in_play = False
       
def stand():
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    global dealer, in_play, score, outcome, msg
    
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(c_deck.deal_card())
        if dealer.get_value() > 21:
            outcome = "Play again?"
            msg = "Dealer is bust, you win"
            score += 1
            in_play = False
        else:
            if player.get_value() <= dealer.get_value():
                outcome = "Play again?"
                msg = "You loose"
                score -= 1
                in_play = False
            elif player.get_value() > dealer.get_value():
                outcome = "Play again?"
                msg = "You win"
                score += 1
                in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    player.draw(canvas, [40, 400])
    dealer.draw(canvas, [40, 200])
    canvas.draw_text("Blackjack", (40,80), 70, "Black")
    out = canvas.draw_text(msg, (250,175), 30, "Black")
    message = canvas.draw_text(outcome, (250,375), 30, "Black")
    canvas.draw_text("Score: " + str(score), (450,550), 30, "Black")
    canvas.draw_text("Player:", (80,375), 30, "Black")
    canvas.draw_text("Dealer:", (80,175), 30, "Black")
    if in_play:
        dealer.card_list[0].drawBack(canvas, [75,199])

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric