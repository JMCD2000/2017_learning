#!  python3.6
# Program name: jmName_Address.py
# Author: Jonathan McDonald
# Date last updated: 5/2/2017
# Purpose: This program displays name and address in a tk frame.

# import modules #
# import antigravity
# import this
import tkinter

# Initialize My Variables #
# None

import tkinter

class Myaddress:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        # Name the window.
        # self.main_window.title('My Address')
        # Size the window, left to right
        # window X by Y size plus upper left coordinates x by Y of desk top screen
        # self.main_window.geometry('400x400+350x300')

        # Create the frames to group widgets.
        self.address_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for the address.
        self.result_label = tkinter.Label(self.address_frame, \
                        text='\n\n')
        self.address = tkinter.StringVar() # To update myaddress_label
        self.myaddress_label = tkinter.Label(self.address_frame, \
                                    textvariable=self.address)
        self.result_label.pack(side='left')
        self.myaddress_label.pack(side='left')

        # Create and pack the button widgets.
        self.show_button = tkinter.Button(self.button_frame, \
                                     text='Show Info', \
                                     command=self.show_myaddress)
        self.quit_button = tkinter.Button(self.button_frame, \
                                text='Quit', \
                                command=self.main_window.destroy)
        self.show_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.address_frame.pack()
        self.button_frame.pack()

        # Start the main loop. Keeps frame open and lisining.
        tkinter.mainloop()

        # The show_myaddress method is the callback function for
        # the show_button widget.

    def show_myaddress(self):
        # Show my address

        # Assign myaddress value.
        self.myaddress = 'Jonathan McDonald \n123 Main St. \nAnytown IN, 55555'

        # Update the myaddress_label widget by storing
        # the value of self.myaddress in the StringVar
        # object referenced by address.
        self.address.set(self.myaddress)
        
# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Create an instance of the myaddress class.
    my_address = Myaddress()
    


# Inform user what this program does

# Run Main program
main()

# End Of Program #

# let user know program has finished

# End Of Line #
