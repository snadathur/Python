#Password generator
import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t' 'u','v','w','x','y', 'z']
#UpperCaseLetters = map(str.upper, Letters)

print("What is the max lenght you would like you password to be?\n")

lenght = int(input())

for x in range(0,lenght):

	print(Letters[random.randint(0,25)])
