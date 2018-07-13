# !python3
# Program name: jmCompany_Employee_Demo.py
# Author: Jonathan McDonald
# Date last updated: 4/23/2017
# Purpose: This program manages employees with a class module

# import modules #
# import antigravity
# import this
import jmCompany_Employee

# Initialize My Variables #
# None


# my main function
def main():
    """
    main -> void
    Main program work space
    """

    # Process an employee
    print('Enter the following employee data for a production worker.')
    # emp name
    name = input('Employee Name: ')
    # emp number
    empNumber = ''
    while (len(empNumber) != 5):
        empNumber = input('Employee Number (exactly 5 characters): ')
        if len(empNumber) < 5:
            print('\tThe entered employee number is to short.')
        elif len(empNumber) > 5:
            print('\tThe entered employee number is to long.')
        else:
            # employee number == 5
            pass

    # emp shift num
    shiftNum = 0
    while shiftNum not in range(1, 3):
        shiftNum = int(input('Employee Shift Number (1 or 2 only): '))
        if shiftNum not in range(1, 3):
            print('\tThe entered shift number is not valid.')
            print('\tEnter either a 1 or a 2 for the shift number.')
        elif shiftNum == 1:
            pass
        else:
            # shift number == 2
            pass

    # emp hourly pay rate
    hourlyPay = float(input('Employee Hourly Pay Rate: $'))

    # Create Employee Object
    employee = jmCompany_Employee.ProductionWorker(name, empNumber, shiftNum, hourlyPay)

    # display employee data
    print('\nHere is the Employee data as entered:')
    print('\nEmployee Name: ' + employee.get_name())
    print('Employee Number: ' + employee.get_empNumber())
    print('Employee Shift: ' + str(employee.get_shiftNum()))
    print('Employee Hourly Pay Rate: $' + format(employee.get_hourlyPay(), ',.2f'))


# inform user what this program does
# print()
# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
