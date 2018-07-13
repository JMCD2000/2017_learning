#!  python3.6
# Program name: jmRecursive_lines.py
# Author: Jonathan McDonald
# Date last updated: 4/27/2017
# Purpose: This program takes a user integer to display lines
#                   of asterisks in step incrementation.

# import modules #
# import antigravity
# import this
# none

# Initialize My Variables #
myChar = '*'


# my function to print asterisks
def myPrintAstrics(myIntVar):
    """
    myPrintAstrics -> string.
    Take myIntVar and return a string of  asterisks of length myIntVar.
    """
    if myIntVar > 0:
        if myIntVar == 1:
            print(myChar)
        else:
            print(myChar, end='')
            myPrintAstrics(myIntVar - 1)


# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Get user number
    myInc = int(input('Enter the number of lines to be drawn: '))

    # Check if a zero value
    if myInc == 0:
        while myInc == 0:
            myInc = int(input('Enter a number that is 1 or greater: '))

    # Print rows of asterisks
    for step in range(myInc):
        step = step + 1
        myPrintAstrics(step)


# inform user what this program does
print('This program takes a user integer and prints incremental asterisks for row count.\n')

# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
