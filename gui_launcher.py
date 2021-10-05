# Import Necessary Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Import Functions from main.py
#import main

# Creating object of tk class
root = tk.Tk()

# Setting up the Box 
root.geometry("720x480")                      
root.resizable(False, False)
root.iconbitmap('petrol.ico')    
root.title("Petrol Pump Finder")
root.config(background="white")

# Setting up Image for Button
photo = PhotoImage(file = r'Red_button.png')

def Widgets():
    head_label = Label(root,
                    text="FIND ME A PUMP!",
					padx=15,
					pady=15,
					font="Arial 18",
					bg="black",
					fg="white")
    head_label.config(anchor=CENTER)
    head_label.pack()

    button = Button(root,
                    text="Click Me!",
                    image = photo)
    button.config(anchor=CENTER)
    button.pack()

# Calling all Widgets into Action
Widgets()
# Infinite Loop for the Program
root.mainloop()