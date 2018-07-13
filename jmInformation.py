#! python3
# Program name: jmInformation.py
# Author: Jonathan McDonald
# Date last updated: 1/27/2017
# Purpose: Print out your name, address, phone number, and college major

# Initialize My Varibles #
##myName As String
##myAddress As String
##myPhoneNumber As String
##myColMajor As String

#assign my varibles and get user input
myName = input('Enter your First and Last Name: ')
myAddress = input('Enter your address with city, state and ZIP: ')
myPhoneNumber = input('Enter your primary phone number: ')
myColMajor = input('What is your college major? ')

#return values to the user, with separate print statements
#### commented out to use one function call instead of four
##print('\nName: ' + myName)
##print('Address: ' + myAddress)
##print('Phone number: ' + myPhoneNumber)
##print('Major: ' + myColMajor)

#return values to the user, with one print statement much better optimized
print('\nName: ' + myName + '\n'
          'Address: ' + myAddress + '\n'
          'Phone number: ' + myPhoneNumber + '\n'
          'Major: ' + myColMajor) #Choosing to left justify, it looks better
	  
# End Of Program #
#let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #