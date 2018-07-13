#! python3
# Program name: jmSumOfNumbers.py
# Author: Jonathan McDonald
# Date last updated: 3/08/2017 # Date created 2/12/2017
# Purpose: This program takes user entered numbers and returns the total number. 
#	   This program also uses a sentinel value to stop data entry, and return results.

# Initialize My Variables #
##running_total As float
running_total = 0.0
##myCurNum As float
##myNum As float
##myCount As Int
##my_increment As Int
my_increment = 0
##keepGoing As Boolean
keepGoing = True

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

                    
#my function to check that inputs are numbers only
def getValidation(myInput):
    """Validate user input is a number"""
    if myInput == "":
        print('You did not enter a number.')
        return -1
    elif myInput.isnumeric() == False:
        if myInput == str(-99):
            return -99
        elif isfloat(myInput) == True:
            if float(myInput) < 0:
                #print('You entered a negative  value, please enter positive numbers only.') #program change, message is displayed in calling Funct. Edit date 3/8/2017
                return -99 #program change to return -99 to end. Edit date 3/8/2017
            else:
                return float(myInput)
        else: 
            print('There has been a read error, please re-enter your number') #program change, message changed to a read error. Edit date 3/8/2017
            return -1
    elif myInput.isnumeric() == True:
        return float(myInput)
    else:
        print('There has been a read error, please re-enter your number')
        return -1
    

#my function to check if a float was provided
def isfloat(myVarCheck):
    """See if string contains a float"""
    try:
        float(myVarCheck)
        #print('Input accepted as a floating point.')
        return True
    except ValueError:
        return False


#inform user what this program accepts for input
print('This program accepts positive integer or floating point values equal to or greater than 0 only.\n'
       + 'To stop entering numbers, enter a negitive number like: -99\n') #program change to accept any negitive number to end. Edit date 3/8/2017

while keepGoing == True:
    #clear reset myCurNum
    myCurNum = 0
    #call my getUserNum function to get user number
    ##using a running total and recycled counter variable instead of a set of variables
    myCurNum, keepGoing = getUserNum(my_increment)
    #accumulate total #program change to not add in the last increment because it is an exit. Edit date 3/8/2017
    if keepGoing == True:
        running_total = running_total + myCurNum
        #increment time in loop plus one
        my_increment = my_increment + 1
    

#return the total count to the user
print('\nThe total for all ' + str(my_increment) + ' of your numbers is = ' + str(running_total))

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
