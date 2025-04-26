# This will allow the user 5 chances to guess the number

import random
number = random.randint(1, 10) # creating the number
# first get the users name
print('Hello, what is your name?')

name = input()

print('Well ' + name + ', I am thinking of a number between 1 and 10. Take a guess, you have 5 chances!')

for guesses in range(1, 6):
    print('What is your number?')
    userNumber = int(input())
    # creating a spot to make sure they stay within the range
    if userNumber <= 0 or userNumber >= 11:
        print("I'm sorry, that is outside your range.")
    elif userNumber == number:
        print('WOW! You got it !!!')
        break
    elif userNumber < number:
        print('Nope, that is too low, please try again.')
    elif userNumber > number:
        print('Nope, that is too high, please try again.')

if guesses != number:
    print('You took ' + str(guesses) + ' guesses already, my number was ' + str(number))
elif guesses == 1:
    print('You took ' + str(guesses) + ' guess!!!!!!')
else:
    print('You took ' + str(guesses) + ' guesses.')


