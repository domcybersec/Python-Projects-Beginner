# creating a simple password generator

# import random so i can shuffle through lists
import random

# write the intro
print('Welcome to Dom\'s Password Generator. Lets make your stuff a vault!')

# you need to have 3 lists, one for letters, symbols, and numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# find out how many letters you would like in your password
passwordLettersNum = int(input('How many letters would you like in your password?\n'))

# find out how many symbols you would like in your password
passwordSymbolsNum = int(input('How many symbols would you like in your password?\n'))

# find out how many numbers you would like in your password
passwordNumbersNum = int(input('How many numbers would you like in your password?\n'))

# create an empty list to add random choices to
masterList = []

# create a for loop for each to add random choices to the new lists
for randLetter in range(passwordLettersNum):
    randLetter = random.choice(letters)
    masterList.append(randLetter)
for randSymbol in range(passwordSymbolsNum):
    randSymbol = random.choice(symbols)
    masterList.append(randSymbol)
for randNum in range(passwordNumbersNum):
    randNum = random.choice(numbers)
    masterList.append(randNum)

# shuffle the items in the list
random.shuffle(masterList)

# pull the items from the list and add them to the string
strongPassword = ''.join(masterList)

# notify the user of their password
print(f'Congrats, your new password is: {strongPassword}')