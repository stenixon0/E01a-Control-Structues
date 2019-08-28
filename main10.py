#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #prints 'Greetings! to terminal
colors = ['red','orange','yellow','green','blue','violet','purple'] #sets list of colors
play_again = '' #instantiates play_again
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #while conditions set to terminate on 'n' or 'no'
    match_color = random.choice(colors) #color to match is set to a random color from colors[]
    count = 0 #instantiates count to 0
    color = '' #instantiates color to ''
    while (color != match_color): #while conditions set to terminate when color == match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line and input is asked for and set to color
        color = color.lower().strip() #makes string lowercase and strips whitespace
        count += 1 #add 1 to count
        if (color == match_color): #check is input matches match_color
            print('Correct!') #prints correct
        else: #triggers if color != match_color
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #prints count with message
    print('\nYou guessed it in {0} tries!'.format(count)) #prints count with message after while loop ends
    if (count < best_count): #checks whether current count is less that best_count
        print('This was your best guess so far!') #prints positive message that triggers with passed if statement
        best_count = count #sets best_count to count with passed if statement
    play_again = input("\nWould you like to play again? ").lower().strip() #asks if user would like to run while loop again
print('Thanks for playing!') #prints when while loop ends