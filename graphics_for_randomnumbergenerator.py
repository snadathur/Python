#Imports modules needed
import tkinter,random
from tkinter import*
tk=Tk()

#Functions needed for program
def create_button(button_text,button_command,backgroundcolor,textcolor):
	btn = Button(tk, text=button_text, command=button_command,)
	btn.pack()

def minnum():
    print('Enter the minimum value for the random number:')
    global minval
    minval=int(input())

def maxnum():
    print('Enter the maximum value for the random number:')
    global maxval
    maxval=int(input())

def randomize():
    randnum=random.randint(minval,maxval)
    print(randnum)

#Gets parameters and gives an into to the program
print('Welcome to the random number generator with a simple GUI by Vikram Nadathur')
minnum()
maxnum()

#Creates buttons
randomize=Button(tk,text="Randomize",command=randomize,bg='blue', fg='white')
randomize.pack()


#   PROGRAM BY VIKRAM NADATHUR 6/11/16                                            
