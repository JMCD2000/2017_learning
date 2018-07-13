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


# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Load the existing employees dictionary and assign it to myEmployees
    myEmployees = load_employees()

    # Initialize a variable for the user's selection
    selection = 0

    # Process menu selection till user quits
    while selection != QUIT:
        # Get user's menu selection
        selection = get_menu_selection()

        # Process the selection
        if selection == LOOK_UP:
            look_up(myEmployees)
        elif selection == ADD:
            add(myEmployees)
        elif selection == CHANGE:
            change(myEmployees)
        elif selection == DELETE:
            delete(myEmployees)

    # Save the myEmployees dictionary to a file
    save_employees(myEmployees)

def load_employees():
    try:
        # Open the employees.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employees_dct = pickle.load(input_file)

        # Close the employees.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employees_dct = {}

    # Return the dictionary.
    return employees_dct

# The get_menu_selection function displays the menu
# and gets a validated selection from the user
def get_menu_selection():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete a employee')
    print('5. Quit the program')
    print()

    # Get the user selection
    selection = int(input('Enter your selection: '))

    # Validate the user selection
    while selection < LOOK_UP or selection > QUIT:
        selection = int(input('Enter a valid selection: '))

    # Return the user selection
    return selection

# The look_up function looks up an item in the
# specified dictionary
def look_up(myEmployees):
    # Get a name to look up
    name = input('Enter a name: ')

    # Look it up in the dictionary
    print(myEmployees.get(name, 'That name is not found.'))

# The add function adds a new entry into the
# specified dictionary
def add(myEmployees):
    # Get the employee info
    name = input('Name: ')
    idNumber = input('ID Number: ')
    dept = input('Department: ')
	jobTitle = input('Job Title: ')

    # Create a Employee object named entry
    entry = employee.Employee(name, idNumber, dept, jobTitle)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value
    if name not in myEmployees:
        myEmployees[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')

# The change function changes an existing
# entry in the specified dictionary
def change(myEmployees):
    # Get a name to look up
    name = input('Enter a name: ')

    if name in myEmployees:
        # Get a new ID Number
        idNumber = input('Enter the new ID Number: ')

        # Get a new Department
        dept = input('Enter the new Department: ')
		
		# Get a new Job Title
        jobTitle = input('Enter the new Job Title: ')

        # Create a employee object named entry
        entry = employee.Employee(name, idNumber, dept, jobTitle)

        # Update the entry
        myEmployees[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

# The delete function deletes an entry from the
# specified dictionary
def delete(myEmployees):
    # Get a name to look up
    name = input('Enter a name: ')

    # If the name is found, delete the entry
    if name in myEmployees:
        del myEmployees[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

# The save_employees function pickles the specified
# object and saves it to the employees file
def save_employees(myEmployees):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myEmployees, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()


