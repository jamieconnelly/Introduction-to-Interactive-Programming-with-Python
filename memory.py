# implementation of card game - Memory

import simplegui
import random

deck = []
exposed = []

# helper function to initialize globals
def new_game():
    global deck, exposed, turns, state
    state = 0
    turns = 0
    deck = [i%8 for i in range(16)]
    exposed = [False for _ in range(16)]
    print deck
    random.shuffle(deck)
    label.set_text("Turns = " + str(turns))
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, click1, click2, turns, deck
    choice = int(pos[0] / 50)
    if state == 0:
        state = 1
        click1 = choice
        exposed[click1] = True
    elif state == 1:
        if not exposed[choice]:
            state = 2
            click2 = choice
            exposed[click2] = True
            turns += 1
    elif state == 2:
        if not exposed[choice]:
            if deck[click1] == deck[click2]:
                pass
            else:
                exposed[click1] = False
                exposed[click2] = False
            click1 = choice
            exposed[click1] = True
            state = 1       
    label.set_text("Turns = " + str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for card in range(16):
        if exposed[card]:
            canvas.draw_text(str(deck[card]), (50 * card +10,80), 80, "White")
        else:
            canvas.draw_polygon([(50*card, 0), (50*card, 0), (50*card + 50, -150)
                             , (50*card + 50, 50)], 3, "Black", "White")


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric