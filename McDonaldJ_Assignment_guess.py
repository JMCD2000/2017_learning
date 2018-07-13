#! python3.4
#######################################################################
# Author: Jonathan McDonald
# CST 100 Fall B
# ID: 1208311061
# Section:
# Date: 11/05/2014
#######################################################################
#   PROGRAM DESCRIPTION
#   This program will play a number guessing game. That will allow a user three
#   attempts to guess a randomly generated number between 1 and 20. A while loop
#   is used to set the maximum number of attempts with if conditionals to catch correct
#   guesses.
#
#   DESCRIPTION OF VARIABLES
#   NAME	| TYPE	| DESCRIPTION
#   -------------------------------------------------------------------
#   intro_name	| str	| the opening introduction to get name
#   intro_num	| str	| the opening introduction to get number
#   too_low	| str	| return string for low guess
#   too_high	| str	| return string for high guess
#   try_again	| str	| return string to try again
#   winner	| str	| return string for correct guess
#   gm_lost	| str	| return string one for out of guesses
#   user_att	| int	| the number of attempts of the player
#   ran_num	| num	| random number used for game
#   user_name       | str	| the name of the player
#   user_number	| num	| the number picked by the player
#   -------------------------------------------------------------------
#######################################################################

##*  MAIN PROGRAM  *##

import random #get extended random functionality#

#*  Declare and initialize variables  *#

intro_name = "Hello! What is your name?"
intro_num = "I am thinking of a number between 1 and 20. Take a guess and give me a number."
too_low = "Your guess is to low."
too_high = "Your guess is to high."
try_again = "Try another guess."
winner = "Winner you have correctly guessed the number"
gm_lost = "Your three guesses are over. The number I was thinking of was"

#*  Set initial conditions  *#

user_att = 0 #set to starting attempts of none#
ran_num = random.randrange (1,21) #initialize the random number between [1,21)#

#*  Define functions  *#
            
def guess_tree (guess, random, attempt): 
    if guess < random: #to low#
        print (too_low)
        guess = int(input(print (try_again)))
    else:
        guess > random #to high#
        print (too_high)
        guess = int(input(print (try_again)))
    return guess, attempt + 1 #if guess = random then it is passed back and caught by the second if statement#

#*  Run the game  *#

user_name = input(print(intro_name )) #get user name and assign#
#print(ran_num ) #this is used for checking the logic flow by displaying the random number. Normally commented out#
user_num = int(input(print("Hi, ", user_name, intro_num ))) #get user number#

if user_num == ran_num: #check for correct first guess#
    print (winner , " on the first try!" )
    
else:
    while user_att < 2: #this is for re guessing#
        if user_num != ran_num:
            user_num, user_att = guess_tree (user_num, ran_num, user_att)
        if user_num == ran_num: #this catches the correct second guess#
            print (winner, "on attempt number", user_att + 1 ) 
            break #this is to prevent an endless loop and to exit while#
    
if user_num != ran_num: #this catches the third try wrong guess#
                print(gm_lost, ran_num)

print("Game Over")

##* END OF MAIN PROGRAM *##

##*  Exit the program  *##

#######################################################################
##* END OF LINE *##
