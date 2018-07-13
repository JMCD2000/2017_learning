# Program name: jmCelsiusToFah.py
# Author: Jonathan McDonald
# Date last updated: 2/17/2017
# Purpose: This program prints a conversion table of Celsius and Fahrenheit temperatures 
#	   from 1 through 20 degrees Celsius.

# Initialize My Variables #
##my_PL_inc As Int #this is my print line increment
my_PL_inc = 0
##myStart as Int
myStart = 0
##myEnd as Int #the range stops at n-1 or myEnd-1
myEnd = 21 
##myR_inc as Int #this is my range incrementation
myR_inc = 1

#my function to convert deg Fahrenheit to deg Celsius
def getF_to_C(myDeg_F):
    """Get degree Fahrenheit and convert to Celsius"""
	
    ##deg_C As Float
    #explicit float
    deg_C = 0.0
	
    #do math conversion
    deg_C = (5.0/9.0)*(myDeg_F - 32.0)
	
    return deg_C


#my function to convert deg Celsius to deg Fahrenheit
def getC_to_F(myDeg_C):
    """Get degree Celsius and convert to Fahrenheit"""
	
    ##deg_F As Float
    #explicite float
    deg_F = 0.0
    
    #do math conversion
    deg_F = (myDeg_C * (9.0/5.0)) + 32.0
	
    return deg_F


#my function to print the conversion table
def showDegreeOutput(myDeg_In, myDeg_Equ, myCurLine):
    """Prints out the degree conversion table"""
	
    ##first call
    if myCurLine == 0:
        print('\t________________')
        print('\t|  Deg C\t|  Deg F\t|') #there are two leading spaces
    elif myCurLine < (myEnd - 1):
        #print('\t-----------------------------')
        print('\t|   ' + format(myDeg_In, '.1f') + '\t|   ' + format(myDeg_Equ, '.1f') + '\t|') #there are three leading spaces
    elif myCurLine == (myEnd - 1):
        #print('\t-----------------------------')
        print('\t|   ' + format(myDeg_In, '.1f') + '\t|   ' + format(myDeg_Equ, '.1f') + '\t|') #there are three leading spaces
        print('\t-----------------------------')
    else:
        print('Loop control count error.')


#inform user what this program accepts for input
print('This program output the degree Fahrenheit from 0 to 20 degrees in Celsius.\n')

##for myDegree in range(0, 21, 1):
##changed from hard coded to varible values
for myDegree in range(myStart, myEnd, myR_inc):
    #increment range starting at 0 but ends at n-1
    #deg_equ as float, degree equlivulant
    deg_equ = 0.0 #explicit float reset and initial value
	
    #call my getC_to_F function to convert degree
    deg_equ = getC_to_F(myDegree)
	
    #call showDegreeOutput
    showDegreeOutput(myDegree, deg_equ, my_PL_inc)
	
    #increment line control
    my_PL_inc = my_PL_inc + 1


# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
