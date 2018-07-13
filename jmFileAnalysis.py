#! python3
# Program name: jmFileAnalysis.py
# Author: Jonathan McDonald
# Date last updated: 4/3/2017
# Purpose: This program reads in two files. Then performs
#           some counts and set operations.

# import modules #
# none

# Initialize My Variables #
# myFile1data as set
myFile1data = set()
# myFile2data as set
myFile2data = set()
# myFile1 As Object
# myFile2 As Object
# data file name
# MY_FILE1_CONST = 'textFile1.txt'  # file input name 1
# MY_FILE2_CONST = 'textFile2.txt'  # file input name 2


# my function to read in the account data
def getFilesIntoSets():
    """
    getFilesIntoSets -> boolean
    Read in Files Data to list
    """
    try:
        # open the file
        # myfile1 = open(MY_FILE1_CONST, 'r')
        myfile1 = open('textFile1.txt', 'r')

        # read values and insert in my set 1
        for line in myfile1:
            if line != ' ':
                myLine = line
                myLine = myLine.rstrip('\n')
                myFile1data.add(myLine)
            else:
                # do nothing
                pass

        myfile1.close

        myfile2 = open('textFile2.txt', 'r')
        
        # read values and insert in my set 1
        for line in myfile2:
            if line != ' ':
                myLine = line
                myLine = myLine.rstrip('\n')
                myFile2data.add(myLine)
            else:
                # do nothing
                pass

        # close the file
        myfile2.close
        
        return True

    except:
        return False


# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Call the getAccounts function
    resultstf = getFilesIntoSets()

    if resultstf is True:
        print('Words in first file: ', end ='')
        print(myFile1data)
        print('Words in second file: ', end ='')
        print(myFile2data)
        myunique = myFile1data | myFile2data
        print('Unique words: ', end ='')
        print(myunique)
        myintersect = myFile1data.intersection(myFile2data)
        print('Words in both files: ', end ='')
        print(myintersect)
        mydiffset2 = myFile1data.difference(myFile2data)
        print('Words in first file, not in second: ', end ='')
        print(mydiffset2)
        mydiffset1 = myFile2data.difference(myFile1data)
        print('Words in second file, not in first: ', end ='')
        print(mydiffset1)
        mysymdiff = myFile1data.symmetric_difference(myFile2data)
        print('Words in only one file, not both: ', end ='')
        print(mysymdiff)
    else:
        print('File read error.')


# inform user what this program does
print('This program reads in two file and performs some analysis.\n')

# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
