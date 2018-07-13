#! python3
# Program name: jmBugs.py
# Author: Jonathan McDonald
# Date last updated: 3/08/2017
# Purpose: This program takes the number of bugs collected each day and returns the total number collected.

# Initialize My Variables #
##total_bugs As Int
total_bugs = 0
##bugs_today As Int
##day_counter As Int
day_counter = 0
##NUM_DAYS As Constant As Int
NUM_DAYS = 5

#my function to get user input
def getBugsToday(myDay):
    """Get and validate user bug count input"""
    #set bugs_today as neg one to accept zero as an input
    bugs_today = -1
    while bugs_today < 0 :
        myBugs_Validation = (input(u'Enter the number of bugs collected on day ' + str(myDay) + ' : '))
        #call my getValidation to check values entered
        bugs_today = getValidation(myBugs_Validation)
        #check if user entered a valid number
        if bugs_today == -1:
            print('\nPlease enter the number of bugs collected. \nEnter a whole integer number >= 0')
                
    return bugs_today


#my function to check that inputs are numbers only
def getValidation(myInput):
    """Validate user input is a number"""
    if myInput == "":
        print('You did not enter the number of bugs collected.')
        return -1
    elif myInput.isnumeric() == False:
        print('You entered a negative or a text value, please enter numerical digits only.')
        return -1
    elif myInput.isnumeric() == True:
        return int(myInput)
    else:
        print('There has been a read error, please reenter your number')
        return -1
    

#inform user what this program accepts for input
print('This program accepts positive integer values and 0 only.\n')

while day_counter < NUM_DAYS :
    #increment day count plus one
    day_counter = day_counter + 1
    #clear reset myDayCount
    myDayCount = 0
    #call my getBugsToday function to get user bug count
    ##using a running total and recycled counter variable instead of a set of variables
    myDayCount = getBugsToday(day_counter)
    #accumulate total bugs
    total_bugs = total_bugs + myDayCount
    

#return the total count to the user
print('\nThe total number of bugs collected in the ' + str(day_counter) + ' day period is : ' + str(total_bugs))

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
