#! python3
# Program name: jmRandomNumberFile.py
# Author: Jonathan McDonald
# Date last updated: 3/05/2017
# Purpose: This program will create and close a file from a series of random numbers. It will then
#   open the file and count the number of numbers and total the numbers.

# import modules #
import random

# Initialize My Variables #
##myFile As Object
##randomNumbers.txt
MY_FILE_CONST = 'randomNumbers.txt'  #file output and input name

#'my main function
def main():
    """Main program work space"""
    #myRangeVar As Integer
    myRangeVar = getUserNum()

    #create file with random numbers by user row
    create_file(myRangeVar)

    #open file and analyse
    #mRV_check As Integer
    mRV_chk, myAcTotal = read_file()

    print('Your row number: ' + str(myRangeVar))
    print('The row count was: ' + str(mRV_chk))
    print('The sum total is: ' + str(myAcTotal))
        
    
#'my function get the user input
def getUserNum():
    """Get and validate user range input"""
    #set myNum as neg one to accept zero as an input
    myNum = -1
    #set myInputCheck as false to enter input loop
    myInputCheck = False
    
    while myInputCheck == False:
        #ask user for number in range
        myNum_Validation = (input(u'Enter an Integer for the Number of rows: '))
            
        #call my getValidation to check values entered
        myNum = getValidation(myNum_Validation)

        #check if user entered a valid number
        if myNum == -1:
            print('\nPlease enter your number. \nEnter a positive integer > 0')
            myInputCheck = False
            
        elif myNum == 0:
            print('\nYou have entered 0.\nPlease enter your number. \nEnter a positive integer > 0')
            myInputCheck = False

        elif myNum > 0:
            #number is greater than zero
            #print('\nYou have entered a valid number.')
            myInputCheck = True
            
        else:
            # myNum < 0:
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
                print('You entered a negative float value, please enter positive integer numbers only.')
                return -1
            else:
                print('You entered a positive float value, please enter positive integer numbers only.')
                return -1
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


#my function to write the random numbers to my file
def create_file(myRow):
    """This generates the file and random numbers"""
    #instructor file reset, open the file and empty it
    myfile = open(MY_FILE_CONST, 'w')
    #close the file
    myfile.close
    
    #open the file in append mode
    myfile = open(MY_FILE_CONST, 'a')

    #run random generator
    i = 0
    while i < (myRow + 1):
         #my Random Value in a range as integer
        myRanVal = random.randint(1, 500)
        #write the data
        myfile.write(str(myRanVal) + '\n')
        i = i + 1
        
    #close the file
    myfile.close


#my function to open and read the random numbers from my file
def read_file():
    """This reads the file and random numbers"""
    #initialize the accumulator
    myTotal = 0
    myRowCount = 0

    try:
        #open the file
        myfile = open(MY_FILE_CONST, 'r')

        #read values and accumulate rows
        for line in myfile:
            if line != ' ':
                myLine = int(line)
                myTotal = myTotal + myLine
                myRowCount = myRowCount + 1
            else:
                #do nothing
                break

        #close the file
        myfile.close

        #correct 0 to 1, one off
        myRowCount = myRowCount - 1
        
        return myRowCount, myTotal

    except:
        print('File read error has occurred.')


#inform user what this program accepts for input
print('This program accepts positive integer values only.')

#get user input in de-scooped functions
main()

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
