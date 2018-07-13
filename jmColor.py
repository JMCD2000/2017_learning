#! python3
# Program name: jmColor.py
# Author: Jonathan McDonald
# Date last updated: 2/05/2017
# Purpose: Takes two primary colors from user and outputs the secondary color.

# Initialize My Variables #
##myColor1 As String
##myColor2 As String
##mySecondary As String

#my function to check that inputs are primary colors only
def getColorSelect(myChoiceOrder):
        """Get and validate user color input"""
        myClrSlct = ""
        while myClrSlct not in ("red", "blue", "yellow"):
                myClrSlct = input('Enter ' + myChoiceOrder + ' primary color: ')
                #check if user entered a primary color
                if myClrSlct not in ("red", "blue", "yellow"):
                        print('\nThe entered color is not a primary color. \nPlease enter either red, blue or yellow')
                
        return myClrSlct


#my function to check if the same color was entered twice
def checkColors(myColor1, myColor2):
        if myColor1 == myColor2:
                singleColor = True
        else:
                singleColor = False
        return singleColor

#my function to mix the primary colors from the user
def getMixedColor(myColor1, myColor2):
        """Compute the mixed secondary color"""
        if myColor1 and myColor2 in ("red", "Blue"):
                mixedColor = "purple"
        elif myColor1 and myColor2 in ("red", "yellow"):
                mixedColor = "orange"
        elif myColor1 and myColor2 in ("blue", "yellow"):
                mixedColor = "green"
        else:
                mixedColor = "bad"

        return mixedColor


#inform user what this program accepts for input
print('This program uses the primary color values of red, blue or yellow only.')

#call my getColorSelect function to get user colors
##I am keeping two variables open and not reusing them
myColor1 = getColorSelect("first")
myColor2 = getColorSelect("second")

#call my getMixedColor function to calculate secondary color
strongCheck = checkColors(myColor1, myColor2)
if strongCheck == False:
        myMixedColor = getMixedColor(myColor1, myColor2)
        #print mixed color to user
        if myMixedColor != "bad":
                print('\nThe secondary color is: ' + myMixedColor)
        elif myMixedColor == "bad":
                print('\nThe color selection encountered a color read error')
        else:
                #assuming untrapped error
                print('\nThe application encountered an error in the color selection.')
elif strongCheck ==True:
        print('\nThe strong primary color is: ' + myColor1)

# End Of Program #

#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
