#Pre-Cond: The text must contain only alphabetic charaters.
#Returns a tuple containing the number of vowels followed by the number of consonants.
#Post-Cond: Returns -1,-1 if there is an error.

def numvowelsconsonants(text):
    vowels=0
    consonants=0
    for let in text:
        if(text[let].isalpha() == False):
            return(-1,-1)
        else:
            if(text[let] == 'a' or text[let] == 'e' or text[let] == 'i' or text[let] == 'o' or text[let] == 'u'):
                vowels+=1
            else:
                consonants+=1

    return (vowels,consonants)

def get_text():
    print("Enter the word")
    ans = input()
    for letter in ans:
        if(ans[letter].isalpha() == False):
            print('There was an error try again')
            get_text()
    return ans

stuff = get_text()
data = numvowelsconsonants(stuff)
print('There are {} vowels and {} consonants'.format(data[0],data[1]))