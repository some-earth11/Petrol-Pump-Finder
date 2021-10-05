# Import Necessary Libraries
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Import Functions from main.py
from main import *

# Creating object of tk class
root = tk.Tk()

# Setting up the Box 
root.geometry("720x480")                      
root.resizable(False, False)
root.iconbitmap('petrol.ico')    
root.title("Petrol Pump Finder")
root.config(background="white")
