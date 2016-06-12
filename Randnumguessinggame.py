import random

def intro():
    print('Welcome to the random number guessing game created by Vikram Nadathur in Python.')
    print('Would you like to play? Reply Y/n')
    ans=input()

    if ans == 'Y':
        pass
    else:
        print('Have a good day')
        quit()


intro()

#Ask user for parameters
print("Please enter the minimum value for the random number")
minval=int(input())
print('Please enter the maximum value for the random number')
maxval=int(input())
message='The number was %s'
randnum=random.randint(minval,maxval)

while 1 == 1:
    print('Guess the number. To give up type 99')
    guess=int(input())
    if guess == randnum:
        print('You guessed the number correctly')
    elif guess == 99:
        print(message % randnum)
        print('Play again another day')
        quit()
    else:
        print('Guess the number')
    guess=int(input())
