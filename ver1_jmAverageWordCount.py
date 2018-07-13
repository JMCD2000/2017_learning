#! python3
# Program name: jmAverageWordCount.py
# Author: Jonathan McDonald
# Date last updated: 3/26/2017
# Purpose: This program takes user input to read in a text file, the program
#           then count the number of lines and the average number of words
#           per line and the total number of words counted.

# import modules #
# none

# Initialize My Variables #
##myLineCount As Int
##myWordCount As Int
##myFileName As Str
##myFile As Object
##data file name
#MY_FILE_CONST = 'charge_accounts.txt'  #file output and input name

#my function to get the file name to read
def getFileName():
    """ getFileName -> string
    Get the file name from the user """
    myFileName = input('Please enter the name of the file: ')

    return str(myFileName)


#my function to open and read in the file data
def openFile(myFileName):
    """ openFile -> list of string
    Open the passed in file name and read into a list """
    
    try:
        #open the file
        myfile = open(myFileName, 'r')

        # TODO: read file to a list
        myContents = myfile.read
        print('my string contents: ' + str(myContents))
        print('my string len: ' + str(len(myContents)))
        #close the file
        myfile.close

        # TODO: return the file contents
        return True, myContents

    except:
        print('File read error has occurred.') #should move print out of this function
        # TODO: return the file contents
        return False, myContents is empty


#my function to perform the file statistics
def getCountStats(myContents):
    """ getCountStats -> line count as int, word count as int
    Perform the line and word counts """

    #if strChr == 

    try:
        if len(myContents) > 1:

            #loop through the lines and words to count totals
            countLine = 0
            countWord = 0
            for myChar in myContents:
                #might need to look for \n if container is a string
                if myChar == '\n':
                    countLine = countLine + 1
                elif myChar == ' ':
                    countWord = countWord + 1
                elif myChar == '\s':
                    countWord = countWord + 1
                else:
                    #should be a char in a word, keep going
                    pass
                    
##            #loop through the lines and words to count totals
##            countLine = 0
##            countWord = 0
##            for line in myfile:
##                #might need to look for \n if container is a string
##                countLine = countLine + 1
##                for word in line:
##                    if word == ' ':
##                        #might need to look at \s and or ' '
##                        countWord = countWord + 1
##                    else:
##                        #should be a char in a word, keep going
##                        pass

            #return line and word counts
            return countLine, countWord
        else:
            print('Length is less than or equal to 1') #should move print out of this function
            # pass
            # raise error, strlen
    
    except:
        print('Object read error has occurred.') #should move print out of this function
        #return False
        # raise error, objread

#'my main function
def main():
    """ main -> None
    Main program work space """
    #Call the getFileName function
    myFileName = getFileName()
    print('myFileName: ' + str(myFileName))
    
    myContiune, myContents = openFile(myFileName)
    print('Contiune: ' + str(myContiune))
    print('my string len: ' + str(len(myContents)))

    if myContiune == True:
        myLines, myWords = getCountStats(myContents)

        #Display returned counts
        print('Line Count: ' + str(myLines))
        print('Word Count: ' + str(myWords))
        # TODO: show average words per line

    else:
        print('myContiune is false')
    
    try:
        myAccountsData.index(myAccountLookup)
        print('Average words per line: ' + str(myWords/myLines))
        #raise div by zero
        
    except ValueError:
        print('Division by Zero Error.')
        
           
#inform user what this program does
print('This program will read in a text file and returns line and word count; \nalong with the computed average of words per line.')

#run main
main()

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
