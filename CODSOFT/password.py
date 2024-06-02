import string
import random
len = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Digits
		2. Letters
		3. Special characters
		4. Exit''')

characterList = ""
while(True):
	choice = int(input("choose a number "))
	if(choice == 1):
	
		characterList += string.digits
	elif(choice == 2):
		
		characterList += string.ascii_letters
	elif(choice == 3):
		
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Please choose a valid option!")

password = []

for i in range(len):
	randomcharacter = random.choice(characterList)
	
	password.append(randomcharacter)

print("The random password is " + "".join(password))