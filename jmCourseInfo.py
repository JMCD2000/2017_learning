#!python3
# Program name: jmCourseInfo.py
# Author: Jonathan McDonald
# Date last updated: 4/3/2017
# Purpose: This program performs course look-ups using dictionaries.
#          The user input is used to pull the course data, if the data exists.

# import modules #
# none

# Initialize My Variables #
myCourseRoom = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}
myCourseInstructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}
myCourseTimes = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}


# my function to look up course info
def getCourse(myCourseNum):
    """
    getCourse -> Boolean, strings
    Using the user supplied course number, return values from dictionaries
    """
    # not doing any error checking
    # check dictionaries for value
    if myCourseNum in myCourseRoom:
        # chaining to save space assumed one for all
        myroom = myCourseRoom[myCourseNum]
        myinstructor = myCourseInstructor[myCourseNum]
        mytimes = myCourseTimes[myCourseNum]
        mycourse = True
    else:
        myroom = 'N/A'
        myinstructor = 'N/A'
        mytimes = 'N/A'
        mycourse = False

    return mycourse, myroom, myinstructor, mytimes


# my main function
def main():
    """
    main void
    Main program work space
    """
    keepgoing = True

    while keepgoing is True:
        # Get user course info
        userCourseNum = input('Enter a course number (ex. CS101) : ')
        # Call the getCourse function
        rcourse, rroom, rinstructor, rtimes = getCourse(userCourseNum)

        # Check return for true
        if rcourse is True:
            print('Room Number: ' + rroom)
            print('Instructor: ' + rinstructor)
            print('Meeting Time: ' + rtimes)
        else:
            print('Course Number was not found.')

        usrYN = input('\nEnter "Y" to keep going, anything else to quit: ')

        if usrYN == 'Y':
            keepgoing = True
        else:
            keepgoing = False


# inform user what this program does
print('This program looks up Course info.\n')

# run main
main()

# End Of Program #

# let user know program has finished
print('\nProgram has finished, good bye.')

# End Of Line #
