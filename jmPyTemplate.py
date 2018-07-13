# Program name: jmPyTemplate.py
# Author: Jonathan McDonald
# Date last updated: 2/26/2017
# Purpose: This program 

# Initialize My Variables #
##myVar As Type
myVar = 0

#my function get the user input
def getUserNum(myCount):
    """Get and validate user bug count input"""
    #set myNum as neg one to accept zero as an input
    ##passed in myCount is a selection value to output correct message
    myNum = -1.0
    while myNum < 0.0 :
        #ask user for first number
        if myCount == 1:
            myNum_Validation = (input(u'Enter your first number: '))
        #assumed to be follow on iteration
        else:
            myNum_Validation = (input(u'Enter your next number: '))
			
        #call my getValidation to check values entered
        myNum = getValidation(myNum_Validation)
        #check if user entered a valid number
        if myNum == -1:
            print('\nPlease enter your number. \nEnter a positive real number >= 0')
        elif myNum == -99:
            print('\nYou have chosen to stop entering numbers.')
            myNum = 0
            return (myNum, False)
        else:
            return (myNum, True)


#inform user what this program accepts for input
print('This program accepts positive integer or floating point values equal to or greater than 0 only.\n'
       + 'To stop entering numbers enter: -99\n')

while keepGoing == True:
    #increment time in loop plus one
    my_increment = my_increment + 1
    #clear reset myCurNum
    myCurNum = 0
    #call my getUserNum function to get user number
    ##using a running total and recycled counter variable instead of a set of variables
    myCurNum, keepGoing = getUserNum(my_increment)
    #accumulate total
    running_total = running_total + myCurNum

#return the total count to the user
print('\nThe total for all ' + str(my_increment) + ' of your numbers is = ' + str(running_total))

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
