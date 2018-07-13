#!  python3.6
# Program name: jmProperty_tax_GUI.py
# Author: Jonathan McDonald
# Date last updated: 5/3/2017
# Purpose: This program displays takes user property value
# 		and displays assessment and taxes in a tk frame.

# import modules #
# import antigravity
# import this
import tkinter

# Initialize My Variables #
# None

import tkinter

class PropertyTaxes:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        # Name the window.
        # self.main_window.title('Property Assessment')
        # Size the window, left to right
        # window X by Y size plus upper left coordinates x by Y of desk top screen
        # self.main_window["geometry"] = "400x400+300x350"

        # Create the frames to group widgets.
        self.getValue_frame = tkinter.Frame(self.main_window)
        # self.assessValue_frame = tkinter.Frame(self.main_window)
        # self.taxValue_frame = tkinter.Frame(self.main_window)
        self.returnValues_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for the entered property value
        self.getvalue_label = tkinter.Label(self.getValue_frame, text='Enter the property value: $')
        self.getvalue_entry = tkinter.Entry(self.getValue_frame, width=10)
        self.getvalue_label.pack(side='left')
        self.getvalue_entry.pack(side='left')
        
        # Create and pack the widgets for the assessment.
        self.myassessment = tkinter.StringVar() # To update assessment_label
        # self.assessment_label = tkinter.Label(self.assessValue_frame, text='Assessment Value: ')
        # self.assessment_output = tkinter.Label(self.assessValue_frame, textvariable=self.myassessment)
        self.assessment_label = tkinter.Label(self.returnValues_frame, text='Assessment Value: ')
        self.assessment_output = tkinter.Label(self.returnValues_frame, textvariable=self.myassessment)
        self.assessment_label.pack() # (side='left')
        self.assessment_output.pack() # (side='top')
		
        # Create and pack the widgets for the tax.
        self.mytax = tkinter.StringVar() # To update mytax_label
        # self.tax_label = tkinter.Label(self.assessValue_frame, text='Property Tax: ')
        # self.tax_output = tkinter.Label(self.assessValue_frame, textvariable=self.mytax)
        self.tax_label = tkinter.Label(self.returnValues_frame, text='Property Tax: ')
        self.tax_output = tkinter.Label(self.returnValues_frame, textvariable=self.mytax)
        self.tax_label.pack() # (side='bottom')
        self.tax_output.pack() # (side='bottom')
        
        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate', command=self.show_myPropInfo)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.getValue_frame.pack()
        # self.assessValue_frame.pack()
        # self.taxValue_frame.pack()
        self.returnValues_frame.pack()
        self.button_frame.pack()

        # Start the main loop. Keeps frame open and lisining.
        tkinter.mainloop()

        
    def show_myPropInfo(self):
        # Get and store entered property value
        self.myValue = float(self.getvalue_entry.get())

        # Assign myassessment value.
        self.assessValue = self.myValue * 0.60
		
        # Assign mytax value.
        self.taxValue = (self.assessValue//100) * 0.75

        # Update the myassessment_label widget by storing
        # the value of self.myassessment in the StringVar
        # object referenced by assessment.
        self.myassessment.set(format(self.assessValue, ',.2f'))
        self.mytax.set(format(self.taxValue, ',.2f'))


# my main function
def main():
    """
    main -> void
    Main program work space
    """
    # Create an instance of the myassessment class.
    my_address = PropertyTaxes()


# Inform user what this program does

# Run Main program
main()

# End Of Program #

# let user know program has finished

# End Of Line #
