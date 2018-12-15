#Pre-Cond: The text must contain only alphabetic charaters.
#Returns a tuple containing the number of vowels followed by the number of consonants.
#Post-Cond: Returns -1,-1 if there is an error.

def numvowelsconsonants(text):
    vowels=0
    consonants=0
    for let in text:
        if(let.isalpha() == False):
            return(-1,-1)
        else:
            if(let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u'):
                # alternatively, you can create a tuple  vowels = ('a', 'e', 'i', 'o' , 'u')
                # then you can check 
                #  if let in vowels :
                #      do something...
                # the in statement will work for lists, tuples and sets
                vowels+=1
            else:
                consonants+=1

    return (vowels,consonants)

def get_text():
    print("Enter the word")
    ans = input()
    for letter in ans:
        if(letter.isalpha() == False):
            print('There was an error try again')
            get_text()
            # we have not exited the original loop.  Try to test this function by itself.
    return ans

# Add documentation for this function, and test it by itself. pytest is best for this kind of things.
def moreinfo():
    print('''Would you like more info?
    Y/N''')
    ans = input()
    for let in ans:
        if(let.isalpha() == False):
            print('One of the characthers was dected as non-alphabetic. Please try again')
            # isalpha returns true if char is alphanumeric.
            moreinfo()  # this is recursion. calling function from inside itself. 
        else:
            continue
    ans = ans.upper()
    if(ans[0] == 'Y'): return True
    else: return False

def letmoreinfo(text):
    v=0
    for let in text:
        if let == 'a':
            v+=1
    print('The word contains the letter a {} times.'.format(v))
    v=0
    for let in text:
        if let == 'e':
            v+=1
    print('The word contains the letter e {} times.'.format(v))
    v=0
    for let in text:
        if let == 'i':
            v+=1
    print('The word contains the letter i {} times.'.format(v))
    v=0
    for let in text:
        if let == 'o':
            v+=1
    print('The word contains the letter o {} times.'.format(v))
    v=0
    for let in text:
        if let == 'u':
            v+=1
    print('The word contains the letter u {} times.'.format(v))

def gettextfile():
    print('Enter the path to the text file:')
    path = input(':')
    myfile = open(path,'r')
    vowels = 0
    consonants = 0
    if(myfile.readable() == False):
        print('There was some error with the file and it was unreadable. Please try again.')
        gettextfile()
    else:
        for line in myfile:
            currentline = line.strip()
            currentline = line.replace(' ','')
            tup1 = numvowelsconsonants(currentline)
            vowels+=tup1[0]
            consonants+=tup1[1]

    return (vowels,consonants)

def intro():
    print('Would you like to enter some text or use a file? text/file')
    ans = input()
    ans = ans.upper()
    for let in ans:
        if(let.isalpha() == False):
            print('There was some non-aplhabetic character dected, please try again.')
            intro()

    if(ans[0] == 'T'):
        print('true')
        return True
    elif(ans[0] == 'F'):
        print('false')
        return False
    else:
        print('none')
        return None


if(intro() == True):
    stuff = get_text()
    data = numvowelsconsonants(stuff)
    print("The word is {}% vowels.".format(100*(data[0]/(data[0]+data[1]))))
    # comment everything till here and get it to work from here.
    if(moreinfo() == True):
        print('data[0] is {} data[1] is {}, the sum is {}'.format(data[0],data[1],data[0]+data[1]))
        percentv = (data[0]/(data[0]+data[1]))
        percentc = (1-percentv)
        print('There are {} vowels and {} consonants'.format(data[0],data[1]))
        print('The word is {vowels}% vowels and {cons}% consonants'.format(vowels = percentv*100,cons = percentc*100))
        letmoreinfo(stuff)
        
elif(intro() == False):
   data = gettextfile()
   print("The word is {}% vowels.".format(100*(data[0]/(data[0]+data[1]))))
   if(moreinfo() == True):
        print('data[0] is {} data[1] is {}, the sum is {}'.format(data[0],data[1],data[0]+data[1]))
        percentv = (data[0]/(data[0]+data[1]))
        percentc = (1-percentv)
        print('There are {} vowels and {} consonants'.format(data[0],data[1]))
        print('The word is {vowels}% vowels and {cons}% consonants'.format(vowels = percentv*100,cons = percentc*100))
        letmoreinfo(stuff)

