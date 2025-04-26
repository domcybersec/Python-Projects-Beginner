# creating a small choose your own adventure game

# opening lines
print('''      Welcome to Treasure Island!
      Your mission is to find the treasure.
      You're at a cross road. Where do you want to go....and beware.''')

firstChoice = input('Type "left" or "right"\n')

if firstChoice == 'left':
    print('You\'ve come to a lake. There is an island in the middle of the lake.')
    secondChoice = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if secondChoice == 'wait':
        print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?')
        thirdChoice = input('Type "red", "yellow", or "blue". Hopefully your luck will hold.\n')
        if thirdChoice == 'red':
            print('Wooooooow that really sucks, crazy maniac with a flamethrower on the other end. Yea, you burnt to a crisp. Better luck next time!')
        elif thirdChoice == 'blue':
            print('I mean, your luck could have been worse but it still sucked. Guy with an ice pick on the other side. He got you straight in the jugular. Your dead.')
        else:
            print('Congrats! Your luck withstood the test of this game. You lived and you open the door to find a note on the ground letting you know that the treasure is the joy along the way. Not that great of a treasure. Someone bring this up to HR!!!')
    else:
        print('Welp, that sucks this was a croc infested lake. Congrats, you were death rolled and brought to a slow and painful end.')
else:
    print('You don\'t do well under pressure do you? You ran straight into a bear and were mauled to death. Congrats, what a way to go.')