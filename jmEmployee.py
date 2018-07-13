#! python3
"""Class Employee Module."""
# Program name: jmEmployee.py
# Author: Jonathan McDonald
# Date last updated: 4/16/2017
# Purpose: This is a class constructor for the Employee class that
# that will hold the attributes: name, ID, dept, and job title.

# import modules #
# import antigravity
# none

# Initialize My Variables #
# none for global scoping


# Class Employee
class Employee:
    """Class Employee Constructor for Class Instances."""

    # initialize the object's data attributes
    def __init__(self, name, idNumber, dept, jobTitle):
        """Initialize the self."""
        self.__name = name  # employee full name
        self.__idNumber = idNumber  # employee ID number
        self.__dept = dept  # employee department
        self.__jobTitle = jobTitle  # employee job title

    # Setter Methods #
    # public method to set name, a private data attribute
    def set_name(self, name):
        self.__name = name

    # public method to set ID number, a private data attribute
    def set_idNumber(self, idNumber):
        self.__idNumber = idNumber

    # public method to set dept, a private data attribute
    def set_dept(self, dept):
        self.__dept = dept

    # public method to set job title, a private data attribute
    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    # Getter Methods #
    # public method to return the data attribute name, a private data attribute
    def get_name(self):
        return self.__name

    # public method to return the data attribute ID number, a private data attribute
    def get_idNumber(self):
        return self.__idNumber

    # public method to return the data attribute dept, a private data attribute
    def get_dept(self):
        return self.__dept

    # public method to return the data attribute job title, a private data attribute
    def get_jobTitle(self):
        return self.__jobTitle

    # Print or return Object's state as a string #
    def __str__(self):
        return "Name: " + self.__name + \
               "\nID Number: " + self.__idNumber + \
               "\nDepartment: " + self.__dept + \
               "\nTitle: " + self.__jobTitle


# End Of Program #

# let user know program has finished

# End Of Line #
