from random import shuffle

print('Welcome the Word Scrambler by Vikram Nadathur.\nEnter a word to scramble or type exit to leave')
word=input()    

if word == 'exit':
    print('Have a good day')
    quit()
else:
        word=list(word)
        print(word)
        print('The scrambled word is ')
        shuffle(word)
        print(word)
        


