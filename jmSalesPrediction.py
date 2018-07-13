#! python3
# Program name: jmSalesPrediction.py
# Author: Jonathan McDonald
# Date last updated: 1/27/2017
# Purpose: Takes imputed total sales and returns expected profit.

# Initialize My Variables #
##myTotalSales As Float
##myProfitPercent As Float
##myEstimateProfit As Float
##testSales As String

#assign my variables and get user input
print('This program only works with numbers.')
myTotalSales = float(input('Enter the total sales amount: '))

#set to enter the value test
testSales = 'Bad'

#check if user entered amount greater than 0
while testSales == 'Bad':
        if myTotalSales <= 0:
            print('\nThe entered Total Sales is equal to or less than 0. \nPlease enter amount greater than 0.00')
            myTotalSales = float(input('Enter the total sales amount: '))
        elif myTotalSales > 0:
            testSales = 'Good'
        else:
            print('\nAn error has occurred, exiting the program...')
            testSales = 'Error'

#if sales amount is Good the do math and return values
if testSales == 'Good':
    myProfitPercent = 0.23 #typical annual profit percentage
    myEstimateProfit = myTotalSales * myProfitPercent

    #return values to the user, with separate print statements
    #### commented out to use one function call instead of three
    ##print('\nTotal Sales: $' + format(myTotalSales, '.2f'))
    ##print('Typical profit percent: ' + format(myProfitPercent, '.0%'))
    ##print('Estimated Profit: $' + format(myEstimateProfit, '.2f'))

    #return values to the user, with one print statement much better optimized
    print('\nTotal Sales: $' + format(myTotalSales, '.2f') + '\n'
           'Typical profit percent: ' + format(myProfitPercent, '.0%') + '\n'
           'Estimated Profit: $' + format(myEstimateProfit, '.2f') )

else:
    #An error has occurred
    #let user know program has finished
    print('\nProgram has ended in error, good bye.')

# End Of Program #
#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
