#! python3
# Program name: jmEmployee_Manager
# Author: Jonathan McDonald
# Date last updated: 4/16/2017
# Purpose: This program manages employees with a class module
# and builds a dictionary and saves the objects.

# import modules #
# import antigravity
import jmEmployee
import pickle

# Initialize My Variables #
# Global constants for the menu selection
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
# Global constant for the file name
FILENAME = 'employees.dat'




# my function to read in the account data
def getAlpha_to_Num(varchar):
    """
    getAlpha_to_Num -> string.
    Take varchar and search dictionary and return a string number.
    """
    try:
        mychar = str.lower(varchar)

    except:
        print('varchar to lower case error')
        mychar = varchar

    # myConversionDict as dictionary
    # either lists sets or dicts, I chose dict
    myConversionDict = {
        'a': '2',
        'b': '2',
        'c': '2',
        'd': '3',
        'e': '3',
        'f': '3',
        'g': '4',
        'h': '4',
        'i': '4',
        'j': '5',
        'k': '5',
        'l': '5',
        'm': '6',
        'n': '6',
        'o': '6',
        'p': '7',
        'q': '7',
        'r': '7',
        's': '7',
        't': '8',
        'u': '8',
        'v': '8',
        'w': '9',
        'x': '9',
        'y': '9',
        'z': '9',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '(': '(',
        ')': ')',
        '-': '-',
        ' ': '0'
        }

    # TODO:  '(': 'strip', ')': 'strip', '-': 'strip',
    return myConversionDict.get(mychar, 'nothing')


# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Load the existing employees dictionary and assign it to myEmployees.
    myEmployees = load_employees()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selection till user quits
    while choice != QUIT:
        # Get user's menu selection.
        choice = get_menu_choice()

        # Process selection
        if choice == LOOK_UP:
            look_up(my
    outPhoneStr = ''

    # Get user phone text string
    inPhoneStr = input('Enter the phone text to be converted: ')

    # parse and loop through inPhoneStr
    for varchar in inPhoneStr:
        # Call the getAlpha_to_Num function
        phonechar = getAlpha_to_Num(varchar)

        if phonechar == 'strip':
            # TODO: strip out any symbols
            pass
        elif phonechar != 'nothing':
            outPhoneStr = outPhoneStr + phonechar
        else:
            print('Unrecognized character in your entry.')
            break

    # TODO: use regex to reformat 5555555555 to (555) 555-5555

    # return to user the translated input
    print('"' + inPhoneStr + '"' + ' Is the same number as: ' + outPhoneStr)


# inform user what this program does
print('This program takes a user phone text string and returns a phone number.\nEXAMPLE: XXX-XXX-XXXX or 555-GET-FOOD\n')

# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
