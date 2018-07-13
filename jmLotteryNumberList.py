#! python3
# Program name: jmLotteryNumberList.py
# Author: Jonathan McDonald
# Date last updated: 3/10/2017
# Purpose: This program generates six numbers, each, in range of 0 to 99 inclusive.
#           Like a lottery number picker, less the already picked numbers bit.

# import modules #
import random

# Initialize My Variables #
##myLotNum As List
#myLotNum = []
#Number Constant as integer
#NUM_CONST = 6

#my function to write the random numbers to my Lottery Numbers
#'my main function
def main():
    """Main program work space"""
    ##myLotNum As List
    myLotNum = []
    #Number Constant as integer
    NUM_CONST = 6
    
   #run random generator
    i = 0
    while i < (NUM_CONST):
         #my Random Value in a range as integer
        myRanVal = random.randint(0,100)
        #write the data
        myLotNum.insert(i, myRanVal)
        i = i + 1

    #return the winning numbers to the user
    print('\nYour winning numbers are;')
    for num in myLotNum:
        print(str(num))
        
#inform user what this program does
print('This program generates six numbers for a winning lottery pick!')

#get winning numbers from main
main()

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
