# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# global variables
secret_guess = 0
turns_left = 7
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global turns_left, num_range
    
    if num_range == 100:
        secret_guess = random.randint(0, 100)
        turns_left = 7
        print "\nNew game. Range is from 0 to 100"
    elif num_range == 1000:
        print "\nNew game. Range is from 0 to 1000"
        turns_left = 10

    # define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game  
    global secret_guess, num_range
    secret_guess = random.randint(0, 100)
    num_range = 100
    new_game()
    print secret_guess

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_guess, num_range
    secret_guess = random.randint(0, 1000)
    num_range = 1000
    new_game()
    print secret_guess
    
def input_guess(guess):
    # main game logic goes here	
    
    global turns_left
    
    print "\nGuess was", guess
    
    if int(guess) > secret_guess:
        turns_left -= 1
        if turns_left > 0:
            print "Number of guesses left is", turns_left
            print "You guessed too high"
        else:
            print "You ran out of guesses, the number was", secret_guess
            new_game()
    elif int(guess) < secret_guess:  
        turns_left -= 1
        if turns_left > 0:
            print "Number of guesses left is", turns_left
            print "You guessed too low"
        else:
            print "You ran out of guesses, the number was", secret_guess
            new_game()
    else:
        print "You guessed correctly"
        new_game()

    
# create frame
f = simplegui.create_frame("Home", 200, 300)

# register event handlers for control elements and start frame
f.add_button("Range 0 - 100", range100, 200)
f.add_button("Range 0 - 1000", range1000, 200)
f.add_input("Enter guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
