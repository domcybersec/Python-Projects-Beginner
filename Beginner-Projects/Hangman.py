# creating a hangman game

# import random to pick a word
import random

# introduce to user

print('Hello, welcome to Hangman, where the only life you lose is your own!')

# create a life counter
lifeCounter = 6

# create a list of words to be used
wordList = ['rabbit', 'apple', 'aardvark', 'house', 'mouse', 'pineapple']

# generate a random word
chosen_word = wordList[random.randint(0, len(wordList) - 1)]
print(chosen_word)

# make as many blanks as letters in that word
placeholder = ''

for letter in range(len(chosen_word)):
    placeholder += '_'

print(placeholder)

# get the user to guess a letter

gameOver = False

correctLetters = []

while not gameOver:
    if lifeCounter > 1:
        print(f'You have {lifeCounter} lives remaining!')
    else:
        print(f'You have {lifeCounter} life remaining!!!!!!!')
    guess = input('Please guess a letter:\n').lower()

    if guess in correctLetters:
        print(f'You have already guessed {guess}')

    display = ''

    for i in chosen_word:
        if i == guess:
            display += guess
            correctLetters.append(i)
        elif i in correctLetters:
            display += i
        else:
            display += '_'
    print(display)

    if guess not in chosen_word:
        lifeCounter -= 1
        print('That is not one of the words, you lose a life!!')
        if lifeCounter == 0:
            gameOver = True
            print(f'YOU LOSE!! The word was {chosen_word}')

    if '_' not in display:
        print('You win!!')
        gameOver = True