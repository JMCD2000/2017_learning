# !python3
# Program name: jmPerson_Demo
# Author: Jonathan McDonald
# Date last updated: 4/23/2017
# Purpose: This program manages persons with a class module

# import modules #
# import antigravity
# import this
import jmPerson

# Initialize My Variables #
# None


# my main function
def main():
    """
    main -> void
    Main program work space
    """

    # Process a person or customer
    print('Enter the following customer information.')
    # name
    name = input('Customer Name: ')
    # full address
    address = input('Address, City, State, Zip: ')
    # telephone number
    telephoneNum = input('Telephone Number (ex. 999-555-1212): ')
    # customer number
    customerNum = ''
    while (len(customerNum) != 5):
        customerNum = input('Customer Number (exactly 5 characters): ')
        if len(customerNum) < 5:
            print('\tThe entered customer number is to short.')
        elif len(customerNum) > 5:
            print('\tThe entered customer number is to long.')
        else:
            # employee number == 5
            pass

    # mailing list bool
    mailList = input('Do you want to be on the mailing list ( y = yes, anything else = no): ')
    if mailList == 'y':
        mailList = True
    else:
        mailList = False

    # Create Customer Object
    customer = jmPerson.Customer(name, address, telephoneNum, customerNum, mailList)

    # display employee data
    print('\nHere is the Customer data as entered:')
    print('\nCustomer Name: ' + customer.get_name())
    print('Customer Address: ' + customer.get_address())
    print('Customer Telephone Number: ' + customer.get_telephoneNumber())
    print('Customer Number: ' + customer.get_custNum())
    print('On mailing list? ' + str(customer.get_mailList()))
    print(customer.speak())


# inform user what this program does
# print()
# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
