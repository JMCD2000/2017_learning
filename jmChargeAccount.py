#! python3
# Program name: jmChargeAccount.py
# Author: Jonathan McDonald
# Date last updated: 3/12/2017
# Purpose: This program reads in account data. Then takes user imput
#           to check if the account exsist.

# import modules #

# Initialize My Variables #
##myAccountsData
myAccountsData = []
##myFile As Object
##data file name
#MY_FILE_CONST = 'charge_accounts.txt'  #file output and input name

#my function to read in the account data
def getAccounts():
    """Read in Account Data to list"""

    try:
        #open the file
        #myfile = open(MY_FILE_CONST, 'r')
        myfile = open('charge_accounts.txt', 'r')

        #read values and insert in mylist
        i = 0
        for line in myfile:
            if line != ' ':
                myLine = line
                myLine = myLine.rstrip('\n')
                myLine = int(line)                
                myAccountsData.insert(i, myLine)
                i = i + 1
            else:
                #do nothing
                break

        #close the file
        myfile.close
        #return True
    except:
        print('File read error has occurred.')
        #return False

#'my main function
def main():
    """Main program work space"""
    #Call the getAccounts function
        #TODO: check return for T/F secuess
    getAccounts()

    #Display list of accounts
    ##for account in myAccountsData:
        ##print(str(account))
        
    ##myAccountLookup as Integer
    myAccountLookup = int(input('What 7-digit account do you want to look-up: '))
    
    #check account if is in account list
    try:
        myAccountsData.index(myAccountLookup)
        print('That is a valid account.')
        
    except ValueError:
        print('That account number is invalid.')
        
           
#inform user what this program does
print('This program checks if the account number is valid')

#run main
main()

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
