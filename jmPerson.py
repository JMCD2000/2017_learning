#! python3
"""Class Company Employee Module."""
# Program name: jmPerson.py
# Author: Jonathan McDonald
# Date last updated: 4/23/2017
# Purpose: This is a class constructor for the Person Superclass and
# a subclass Customer.

# import modules #
# import antigravity
# import this
# none

# Initialize My Variables #
# none for global scoping


# Class Person
class Person:
    """Class Person Constructor for Class Instances."""

    # initialize the object's data attributes
    def __init__(self, name, address, telephoneNumber):
        """Initialize the self."""
        self.__name = name  # full name
        self.__address = address  # address
        self.__telephoneNumber = telephoneNumber  # telephone number

    # Setter Methods #
    # public method to set name, a private data attribute
    def set_name(self, name):
        self.__name = name

    # public method to set address, a private data attribute
    def set_address(self, address):
        self.__address = address

    # public method to set telephone number, a private data attribute
    def set_telephoneNumber(self, telephoneNumber):
        self.__telephoneNumber = telephoneNumber

    # Getter Methods #
    # public method to return the data attribute name, a private data attribute
    def get_name(self):
        return self.__name

    # public method to return the data attribute address, a private data attribute
    def get_address(self):
        return self.__address

    # public method to return the data attribute telephone number, a private data attribute
    def get_telephoneNumber(self):
        return self.__telephoneNumber

    # public method to speak who is this is
    def speak(self):
        return 'I am a person.'

    # Print or return Object's state as a string #


# Class ProductionWorker
class Customer(Person):
    """
    SubClass Customer Constructor for Class Instances.
    Is a sub class of Person
    """

    # initialize the object's data attributes
    def __init__(self, name, address, telephoneNumber, custNum, mailList):
        """Initialize the self."""
        Person.__init__(self, name, address, telephoneNumber) # Call super class Person
        self.__custNum = custNum  # employee shift number, integer
        self.__mailList = mailList  # employee hourly pay, float

    # Setter Methods #
    # public method to set customer number, a private data attribute
    def set_custNum(self, custNum):
        self.__custNum = custNum

    # public method to set mailing list, a private data attribute
    def set_mailList(self, mailList):
        self.__mailList = mailList

    # Getter Methods #
    # public method to return the data attribute customer number, a private data attribute
    def get_custNum(self):
        return self.__custNum

    # public method to return the data attribute mailing list a private data attribute
    def get_mailList(self):
        return self.__mailList

    # public method to speak who is this is
    def speak(self):
        return 'I am a customer.'

    # Print or return Object's state as a string #
    

# End Of Program #

# let user know program has finished

# End Of Line #
