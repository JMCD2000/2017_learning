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

#my function to get the file name to read
def getFileName():
    """ getFileName -> string
    Get the file name from the user """
    myFileName = input('Please enter the name of the file: ')
    #return the user string
    return str(myFileName)


#my function to open and read in the file data
def openFile(myFileName):
    """ openFile -> string
    Open the passed in file name and read into a string """
    
    try:
        #open the file
        myFile = open(myFileName, 'r')
        #read whole file into memory as a string
        myContents = myFile.read()
        #close the file
        myFile.close()
        #return the file contents
        return True, myContents

    except:
        print('File read error has occurred.') #should move print out of this function
        #return the file contents
        myContents = '' #set to zero length
        return False, myContents
    

#my function to perform the file statistics
def getCountStats(myContents):
    """ getCountStats -> line count as int, word count as int
    Perform the line and word counts """

    # Initialize My Variables #
    countLine = 1 #correcting for EOF
    countWord = 0
    
    #loop through the lines and words to count totals
    for myChar in myContents:
        #look for \n or space in the file string
        if myChar == '\n':
            countLine = countLine + 1
        elif myChar == ' ':
            countWord = countWord + 1
        elif myChar == '\s':
            countWord = countWord + 1
        elif myChar == 'EOF':
            countLine = countLine + 1
        else:
            #should be a char in a word, keep going
            pass
                
    #return line and word counts
    return countLine, countWord


#'my main function
def main():
    """ main -> None
    Main program work space """
    #Call the getFileName function
    myFileName = getFileName()
    #Call the openFile function
    myContiune, myContents = openFile(myFileName)
    #check my condidtion for true
    if myContiune == True:
        if len(myContents) > 1: 
            myLines, myWords = getCountStats(myContents)
            #Display returned counts
            print('\nLine Count: ' + str(myLines))
            print('Word Count: ' + str(myWords))
            try:
                myLines = float(myLines)
                print('Average words per line: ' + str(format((myWords/myLines), '.1f')))
                #raise div by zero
            except ValueError:
                print('Division by Zero Error.')

        else:
            print('Length is less than or equal to 1') 
            # pass
            # raise error, strlen

    else:
        print('myContiune is false')
        
           
#inform user what this program does
print('This program will read in a text file and returns line and word count; \nalong with the computed average of words per line.')

#run main
main()

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
