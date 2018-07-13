#! python3
# Program name: jmKilometers.py
# Author: Jonathan McDonald
# Date last updated: 2/26/2017
# Purpose: This program converts user entered Kilometers to Miles and displays both back to the user

# Initialize My Variables #
##myMile as Float
##MY_K_M_CONST As Float
MY_K_M_CONST = 0.6214 #conversion constant for miles per kilometer
##usrMile as Float
##usrKM as Int

#my function get the user input
def compute_miles(myKm):
    """Convert Kilometers to Miles"""
    ##myMile as Float
    myMile = 0.0
    
    #convert Km to miles
    ##should make 0.6214 a constant
    myMile = myKm * MY_K_M_CONST

    #return computed miles
    return myMile


#my function get the user input
def getUserNum():
    """Get and validate user Kilometer input"""
    #set myNum as neg one to accept zero as an input
    myNum = -1
    #set myInputCheck as false to enter input loop
    myInputCheck = False
    
    while myInputCheck == False:
        #ask user for number of kilometers
        myNum_Validation = (input(u'Enter the Kilometers for conversion: '))
            
        #call my getValidation to check values entered
        myNum = getValidation(myNum_Validation)

        #check if user entered a valid number
        if myNum == -1:
            print('\nPlease enter your number. \nEnter a positive real number >= 0')
            myInputCheck = False
            
        elif myNum == 0:
            print('\nYou have entered 0 for the number of Kilometers.')
            myInputCheck = True
            
        elif myNum > 0:
            #number is greater than zero
            myInputCheck = True
            
        else:
            #number is not greater than zero
            myInputCheck = False
            
    return int(myNum)


#my function to check that inputs are numbers only
def getValidation(myInput):
    """Validate user input is a number"""
    if myInput == "":
        print('You did not enter a number.')
        return -1
    elif myInput.isnumeric() == False:
        if myInput == str(-99):
            return -1
        elif isfloat(myInput) == True:
            if float(myInput) < 0:
                print('You entered a negative  value, please enter positive numbers only.')
                return -1
            else:
                return float(myInput)
        else: 
            print('You entered a negative or a text value, please enter numerical digits only.')
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
print('This program accepts positive integer values equal to or greater than 0 only.')

#initilize user kilometers
usrKM = 0
#get user kilometer input
usrKM = getUserNum()

#initilize user miles conversion
usrMile = 0.0
#run user K to M conversion
usrMile = compute_miles(usrKM)

#return the Kilometers to Miles to the user
print('\nKilometers ' + str(usrKM) + ' is equal to ' + format(usrMile, '.2f') + ' miles')

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
