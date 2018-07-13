# This program demonstrates a group of Radiobutton widgets.

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create three frames. One for the Radiobuttons
        # one for the user data entry
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = tkinter.IntVar()
        
        # Set the intVar object to 1.
        self.radio_var.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.top_frame, \
                    text='Daytime (6:00 am - 5:59 pm), $0.07/minute', variable=self.radio_var, value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame, \
                    text='Evening (6:00 pm - 11:59 pm), $0.12/minute', variable=self.radio_var, value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame, \
                    text='Off-Peak (midnight - 5:59 am), $0.05/minute', variable=self.radio_var, value=3)

        # Pack the Radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create the text entry widget for time collection
        self.userTime_label = tkinter.Label(self.middle_frame, \
                        text='Enter the length of the call (in minutes):')
        self.userTime_entry = tkinter.Entry(self.middle_frame, width=10)

        # Pack the text and time collection
        self.userTime_label.pack(side='left')
        self.userTime_entry.pack(side='left')
        
        # Create an Calculate button and a Quit button.
        self.calc_button = tkinter.Button(self.bottom_frame, \
                      text='Calculate cost', command= self.calc_cost)
        self.quit_button = tkinter.Button(self.bottom_frame, \
                      text='Quit', command=self.main_window.destroy)

        # Pack the Buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        # Start the mainloop.
        tkinter.mainloop()

    # The calc_cost method is the callback function for
    # the calc_button widget.

    def calc_cost(self):
        # Get the number of minutes and store it in a variable.
        self.userMinutes = float(self.userTime_entry.get())

        # Get the Radio button selection
        self.callRate = int(self.radio_var.get())

        # Set rate multiplier
        if self.callRate == 1:
            self.perMinute = 0.07

        elif self.callRate == 2:
            self.perMinute = 0.12

        elif self.callRate == 3:
            self.perMinute = 0.05

        else:
            self.perMinute = 0.0

        # Calculate the cost of the call.
        self.callCost = float(self.userMinutes * self.perMinute)

        # Show the Cost of the call
        tkinter.messagebox.showinfo('Call cost', 'The cost of the call is: $' + str(self.callCost))
        tkinter.messagebox.showinfo('Call cost', 'The cost of the call is: $' + format(self.callCost, ',.2f'))

# Create an instance of the MyGUI class.
my_gui = MyGUI()
