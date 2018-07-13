#! python3
"""Class Company Employee Module."""
# Program name: jmCompany_Employee.py
# Author: Jonathan McDonald
# Date last updated: 4/23/2017
# Purpose: This is a class constructor for the Company_Employee Supperclass that
# that will hold the attributes: Employee name and Employee number.

# import modules #
# import antigravity
# import this
# none

# Initialize My Variables #
# none for global scoping


# Class Employee
class Employee:
    """Class Employee Constructor for Class Instances."""

    # initialize the object's data attributes
    def __init__(self, name, empNumber):
        """Initialize the self."""
        self.__name = name  # employee full name
        self.__empNumber = empNumber  # employee ID number

    # Setter Methods #
    # public method to set name, a private data attribute
    def set_name(self, name):
        self.__name = name

    # public method to set ID number, a private data attribute
    def set_idNumber(self, empNumber):
        self.__empNumber = empNumber

    # Getter Methods #
    # public method to return the data attribute name, a private data attribute
    def get_name(self):
        return self.__name

    # public method to return the data attribute ID number, a private data attribute
    def get_empNumber(self):
        return self.__empNumber

    # Print or return Object's state as a string #
    def __str__(self):
        return "Name: " + self.__name + \
               "\nEmployee Number: " + self.__empNumber


# Class ProductionWorker
class ProductionWorker(Employee):
    """
    SubClass ProductionWorker Constructor for Class Instances.
    Is a sub class of Employee
    """

    # initialize the object's data attributes
    def __init__(self, name, empNumber, shiftNum, hourlyPay):
        """Initialize the self."""
        Employee.__init__(self, name, empNumber) # Call super class Employee
        self.__shiftNum = shiftNum  # employee shift number, integer
        self.__hourlyPay = hourlyPay  # employee hourly pay, float

    # Setter Methods #
    # public method to set shift number, a private data attribute
    def set_shiftNum(self, shiftNum):
        self.__shiftNum = shiftNum

    # public method to set hourly pay, a private data attribute
    def set_hourlyPay(self, hourlyPay):
        self.__hourlyPay = hourlyPay

    # Getter Methods #
    # public method to return the data attribute shift number, a private data attribute
    def get_shiftNum(self):
        return self.__shiftNum

    # public method to return the data attribute hourly pay, a private data attribute
    def get_hourlyPay(self):
        return self.__hourlyPay

    # Print or return Object's state as a string #
    def __str__(self):
        return "Shift: " + self.__shiftNum + \
               "\nHourly Pay Rate: $" + format(self.__hourlyPay, '.2f')


# End Of Program #

# let user know program has finished

# End Of Line #
