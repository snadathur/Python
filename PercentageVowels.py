print('Would you like to enter text or open a txt file? Enter file or text !! Note at this time the file option doesnt work')
ans = input()
while(ans.isalpha == False):
    print('There was some non alphabetic charather please try again')
    print('-' * 20)
    ans= input
ans = ans.upper()
if(ans[0] == 'F'):
    print('Enter the file path')
    path = input()
    myfile= open(path)
    text = myfile.read
else:
    print('-' * 20)
    text = input('Enter text here: ')
    while(ans.isalpha == False):
            print('There was some non alphabetic charather please try again')
            print('-' * 20)
            ans= input

count = 0
vowels = 0

while(count<len(text)):
    
    if(text[count] == 'a'):
        vowels+=1
    elif(text[count] == 'e'):
        vowels+=1
    elif(text[count] == 'i'):
        vowels+=1
    elif(text[count] == 'o'):
        vowels+=1
    elif(text[count] == 'u'):
        vowels+=1

    count+=1
    
percentvowels = (vowels/len(text))*100
print('Lenght of word {}'.format(len(text)))
print('Vowels {}'.format(vowels))
print('The text contains {:0.2f}% vowels.'.format(percentvowels))
print('Would you like more info?')
ans = input('Y/N')
ans = ans.upper()
if(ans[0] == 'Y'):
    percentconsonants= 100-percentvowels
    count=0
    leta=0
    lete=0
    leti=0
    leto=0
    letu=0
    while(count<len(text)):
        if(text[count] == 'a'):
            leta+=1
        elif(text[count] == 'e'):
            lete+=1
        elif(text[count] == 'i'):
            leti+=1
        elif(text[count] == 'o'):
            leto+=1
        elif(text[count] == 'u'):
            letu+=1
        count+=1

    percentleta = 100*(leta/len(text))
    percentlete = 100*(lete/len(text))
    percentleti = 100*(leti/len(text))
    percentleto = 100*(leto/len(text))
    percentletu = 100*(letu/len(text))

    print("The text contains {:0.2f}% vowels, {:0.2f}% consonants, {:0.2f}% the letter a, {:0.2f}% the letter e, {:0.2f}% the letter i{:5.2f}% the letter o, {:0.2f}% the letter u.".format(percentvowels,percentconsonants,percentleta,percentlete,percentleti,percentleto,percentletu))
else:
    quit()