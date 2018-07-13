#! python3
# Program name: jmInsurance.py
# Author: Jonathan McDonald
# Date last updated: 2/26/2017
# Purpose: This program gets the replacement cost and returns the minimun amount of insurance needed back to the user

# Initialize My Variables #
##MY_MIN_PERCT_CONST As Float
MY_MIN_PERCT_CONST = 0.80 #constant for 80% of total value

#my function get the user input
def compute_insurance(myReplacement):
    """Caculate Minimum Insurance Amount"""
    ##myInsAmt as Float
    myInsAmt = 0.0
    
    #caculate the minumin insurance amount
    ##should make 80% a constant
    myInsAmt = myReplacement * MY_MIN_PERCT_CONST

    #return computed miles
    return myInsAmt


#my function get the user input
def getUserNum():
    """Get and validate user input"""
    #set myNum as neg one to accept zero as an input
    myNum = -1.0
    #set myInputCheck as false to enter input loop
    myInputCheck = False
    
    while myInputCheck == False:
        #ask user for replacement cost
        myNum_Validation = (input(u'Enter the replacement cost of building: $'))
            
        #call my getValidation to check values entered
        myNum = getValidation(myNum_Validation)

        #check if user entered a valid number
        if myNum == -1.0:
            print('\nPlease enter your number. \nEnter a positive dollar amount >= $0.00')
            myInputCheck = False
            
        elif myNum == 0.0:
            print('\nYou have entered $0.00 for the replacement cost.')
            myInputCheck = True
            
        elif myNum > 0.0:
            #number is greater than zero
            myInputCheck = True
            
        else:
            #number is not greater than zero
            myInputCheck = False
            
    return float(myNum)


#my function to check that inputs are numbers only
def getValidation(myInput):
    """Validate user input is a number"""
    if myInput == "":
        print('You did not enter a number.')
        return -1.0
    elif myInput.isnumeric() == False:
        if myInput == str(-99):
            return -1.0
        elif isfloat(myInput) == True:
            if float(myInput) < 0.0:
                print('You entered a negative  value, please enter positive numbers only.')
                return -1.0
            else:
                return float(myInput)
        else: 
            print('You entered a negative or a text value, please enter numerical digits only.')
            return -1.0
    elif myInput.isnumeric() == True:
        return float(myInput)
    else:
        print('There has been a read error, please re-enter your number')
        return -1.0


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
print('This program accepts positive dollar amounts equal to or greater than $0.00 only.')

#initilize user replacement cost
usrReplaceCost = 0.0
#get user input
usrReplaceCost = getUserNum()

#initilize user insurance coverage amount
usrCoverage = 0.0
#run user insurance amount
usrCoverage = compute_insurance(usrReplaceCost)

#return the Insurance coverage amount to the user
print('\nYour replacement cost of  $' + format(usrReplaceCost, '.2f') + ' should have a minumin coverage amount of  $' + format(usrCoverage, '.2f') + ' for insurance.')

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
