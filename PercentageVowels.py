print('Enter some text')
text = input('Enter text here: ')
count = 0
vowels = 0
while(count<len(text)):
    print('textcount is {}, vowels is {}, count is {}'.format(text[count],vowels,count))
    if(text[count] == 'a'):
        print('You have entered the fist if statement')
        vowels+=1
    elif(text[count] == 'e'):
        print('You have entered the second if statement')
        vowels+=1
    elif(text[vowels] == 'i'):
        print('You have entered the third if statement')
        vowels+=1
    elif(text[vowels] == 'o'):
        print('You have entered the fourth if statement')
        vowels+=1
    elif(text[vowels] == 'u'):
        print('You have entered the fifth if statement')
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

    print("The text contains {:0.2f}% vowels, {:0.2f}% consonants, {:0.2f}% the letter a, {:0.2f}% the letter e, {:0.2f}% the letter i{:1.2f}% the letter o, {:0.2f}% the letter u.".format(percentvowels,percentconsonants,percentleta,percentlete,percentleti,percentleto,percentletu))
else:
    quit()