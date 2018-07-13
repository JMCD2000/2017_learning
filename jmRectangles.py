#! python3
# Program name: jmRectangles.py
# Author: Jonathan McDonald
# Date last updated: 2/05/2017
# Purpose: Takes the width and length of two rectangles imputed and returns the larger one.

# Initialize My Variables #
##myRec1_len As Float
##myRec1_wdth As Float
##myRec2_len As Float
##myRec2_wdth As Float
##myRec1_area As Float
##myRec2_area As Float

#my function to get and check user input for rectangle dimensions
def getRecSide(myDim, recNum):
    """Get and validate user dimension input"""
    recDim = 0.0
    while recDim <= 0.0:
        recDim = float(input('Enter the ' + myDim + ' of rectangle ' + recNum + ': '))
        #check if user entered amount greater than 0
        if recDim <= 0.0:
            print('\nThe entered diminsion is equal to or less than 0. \nPlease enter amount greater than 0.0')

    return recDim


#my function to compute the area of a rectangle
def getRecArea(myLen, myWdth):
    """Compute the area of a rectangle"""
    recArea = myLen * myWdth #floats are referenced

    return recArea


#inform user what this program accepts for input
print('This program uses floating point or integers only.')

#call my getRecSide function to get user dimensions
##I am keeping four variables open and not reusing them
myRec1_len = getRecSide("Length", "one")
myRec1_wdth = getRecSide("Width", "one")
myRec2_len = getRecSide("Length", "two")
myRec2_wdth = getRecSide("Width", "two")

#call my getRecArea function to calculate rectangle area
myRec1_area = getRecArea(myRec1_len, myRec1_wdth)
myRec2_area = getRecArea(myRec2_len, myRec2_wdth)

#determine larger rectangle
if myRec1_area > myRec2_area:
    print('\nThe first rectangle is larger with an area of: ' + str(myRec1_area))
elif myRec1_area < myRec2_area:
    print('\nThe second rectangle is larger with an area of: ' + str(myRec2_area))
else:
    #assuming both are equal to each other in area
    print('\nThe two rectangles are equal in area.')

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
