# Course: CIS 117 PythonProgramming
# Name:   Chamith Gamage
# Description:  GUI 
# Application:  CCreating a Kilometer to Miles Converter 
# Development Environment:  macOSX 12.4
# Version:  Python 3.10.4
# Date:  10/25/22


# Program Source Statements

import tkinter
from tkinter import END, messagebox

class KmtoMconverter:
    """
    class that holds components of converter app
    """

    
    
    def __init__(self):
        """
        create GUI of the converter
        """
        
        #create the main window, define the size.
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x200+500+300")
        self.main_window.title("Kilometers to miles converter")
        
        # create widgets lable, input fields and buttons.
        # defines the functionality of each button.
        self.label = tkinter.Label(text="Insert the kilometer value below")
        self.input = tkinter.Entry()
        self.convert_btn = tkinter.Button(self.main_window,
                                        text= "Convert",  
                                        command=self.convert)
        self.quit_btn = tkinter.Button(self.main_window,
                                    text= "Quit",
                                    command=self.main_window.destroy)
        
        # inset widgets to main window.
        self.label.pack(padx=20,pady=10)
        self.input.pack(padx=20,pady=10)
        self.convert_btn.pack( padx=20,pady=10)
        self.quit_btn.pack(padx=20,pady=10)
        tkinter.mainloop()
        
    def convert(self):
        """executes conversion functiolality
        """
        
        ## retrives value of the input field.
        input = self.input.get()
        
        # if value is numeric, do the conversion.
        # display results in a message box
        if(input.isnumeric()):
    
            result = round(float(input) * 0.621371,2) 
            messagebox.showinfo(title="Results",
                                message= str(input) + 
                                "\n Kilometer(s) equals to \n"+str(result) + 
                                "\nmiles")
            
        # if input is not numeric, display error message
        # clear the input field.
        else:
            messagebox.showinfo(title="Error",
                                message="Please enter a numric value!!")
            self.input.delete(0, END)



my_app = KmtoMconverter()