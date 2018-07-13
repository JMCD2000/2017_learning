#! python3
# Program name: jmMealTotal.py
# Author: Jonathan McDonald
# Date last updated: 1/27/2017
# Purpose: Takes imputed meal amount to calculate 
# 	   the tax and tip to show the meal total.

# Initialize My Variables #
##myMealPrice As Float
##myTax As Float
##myTipPercent As Float
##myTipAmount As Float
##myTotalBill As Float
##testSales As String

#assign my variables and get user input
print('This program only works with numbers.')
myMealPrice = float(input('Enter the price of the meal: '))

#set to enter the value test
testSales = 'Bad'

#check if user entered amount greater than 0
while testSales == 'Bad':
        if myMealPrice <= 0:
            print('\nThe entered meal price is equal to or less than 0. \n'
                      'Please enter amount greater than $0.00')
            myMealPrice = float(input('Enter the price of the meal: '))
        elif myMealPrice > 0:
            testSales = 'Good'
        else:
            print('\nAn error has occured, exiting the program...')
            testSales = 'Error'

#if sales amount is Good the do math and return values
if testSales == 'Good':
    myTax = 0.07 #Local sales tax amount percentage
    myTipPercent = 0.18 #The default tip amount percentage
	
    #calculate the tax on my meal
    myTotalBill = myMealPrice * myTax
    #add the meal price back into myTotalBill
    myTotalBill = myTotalBill + myMealPrice
	
    #calculate the tip on my meal, without including the tax
    myTipAmount = myMealPrice * myTipPercent
    #add the tip amount into myTotalBill
    myTotalBill = myTotalBill + myTipAmount

    #return values to the user, with separate print statements
    #### commented out to use one function call instead of four
    ##print('\nMeal price: $' + format(myMealPrice, '.2f'))
    ##print('Tax amount on meal: $' + format((myMealPrice * myTax), '.2f'))
    ##print('Tip amount on meal: $' + format(myTipAmount, '.2f'))
    ##print('Bill total: $' + format(myTotalBill, '.2f'))

    #return values to the user, with one print statement much better optimized
    print('\nMeal price: $' + format(myMealPrice, '.2f') + '\n'
              'Tax amount on meal: $' + format((myMealPrice * myTax), '.2f') + '\n'
	'Tip amount on meal: $' + format(myTipAmount, '.2f') + '\n'
              'Bill total: $' + format(myTotalBill, '.2f') )

else:
    #An error has occurred
    #let user know program has finished
    print('\nProgram has closed in error, good bye.')

# End Of Program #
#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
