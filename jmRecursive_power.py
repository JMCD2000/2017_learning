#!  python3.6
# Program name: jmRecursive_power.py
# Author: Jonathan McDonald
# Date last updated: 4/28/2017
# Purpose: This program takes a user base number and a power number
#                   it then computes the answer.

# import modules #
# import antigravity
# import this
# none

# Initialize My Variables #
# myBase = 0 As Int
# myPow = 0 As Int
# myAnswer = 0 As Int


# my function to print asterisks
def myRaiseToPower(basenum, raisepow):
    """
    myRaiseToPower -> Integer.
    Take myBase and raise it with myPow and return answer.
    """
    if raisepow > 1:
        if raisepow == 2:
            raised_base = basenum * basenum
            # return raised_base
        else:
            raised_base = basenum * myRaiseToPower(basenum, raisepow - 1)

#    elif raisepow == 1:
#        return basenum
#    elif raisepow == 0:
#        return 1

    return raised_base

# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Get user base number
    try:
        myBase = int(input('Enter the base number: '))
        # Check if a zero value
        if myBase == 0:
            while myBase == 0:
                myBase = int(input('Enter a number that is greater than or equal to 1: '))
    except:
        print('A character was detected. Expected integers. Now exiting.')
        return

    # Get user raise to power number
    try:
        myPow = int(input('Enter the exponent (power) as a non-negative integer: '))
        if myPow < 0:
            while myPow < 0:
                myPow = int(input('Enter the exponent (power) as a whole number, => 0: '))
    except:
        print('A character was detected. Expected integers. Now exiting.')
        return

    # Check for power of zero or one or higher
    if myPow == 0:
        print(str(myBase) + ' raised to the power of ' + str(myPow) + ' is 1.')

    elif myPow == 1:
        print(str(myBase) + ' raised to the power of ' + str(myPow) + ' is ' + str(myBase))

    else:
        myAnswer = myRaiseToPower(myBase, myPow)
        print(str(myBase) + ' raised to the power of ' + str(myPow) + ' is ' + str(myAnswer))


# inform user what this program does
print('This program takes a user entered base and \nraises it a user entered power and \nreturns the answer.\n')

# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
