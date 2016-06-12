#This program generates a random number. The user specifies the min and max values.
import random

#Ask user for parameters
print("Welcome to the Random Number generator created by Vikram Nadathur\n Please enter the minimum value for the random number")
minval=int(input())
print('Please enter the maximum value for the random number')
maxval=int(input())

#Ask user for number of times to generate random number
print('How many random number would you like?')
num=int(input())
for x in range (num):

#Generate random number    
    randnum=random.randint(minval,maxval)

#Print random number
    print(randnum)
