import tkinter,sys,os,turtle 
from tkinter import*
tk=Tk()
#Imports modules needed
def create_button(button_text,button_command):
	btn = Button(tk, text=button_text, command=button_command)
	btn.pack()
create_button("test",None)
#Creates buttons
create_button("Enter the number of random numbers you want",None)
create_button("Randomize",None)






