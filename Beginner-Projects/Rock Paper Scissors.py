# making a small and randomized rock paper scissors game

# first import the random module so the computer can play

import random

# ascii art for the different choices

art = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

# introduce the game to the user
print('Let\'s play a game! Good old fashioned Rock Paper Scissors')

# get the user's choice
userChoice = int(input('What do you choose? Type "0" for Rock, "1" for Paper, or "2" for Scissors\n'))
# create a quick if statement just in case an invalid number is chosen
if userChoice <= 3 or userChoice < 0:
    print(art[userChoice])
else:
    print('No art available: Invalid Number!!')

# use the random module to get the computers choice
computerChoice = random.randint(0, 2)
print(f''' Computer chose:
      
      {art[computerChoice]}''')

# now create an if statement to actually play the game

if userChoice >= 3 or userChoice < 0:
    print('You typed an invalid number. You lose!')
elif userChoice == 0 and computerChoice == 2:
    print('YOU WIN!!! YOU HAVE BEATEN THE COMPUTER!!!')
elif userChoice == computerChoice:
    print('Wow it\'s a draw. Please try again')
elif computerChoice > userChoice:
    print('What a shame. You LOSE!')
elif computerChoice == 0 and userChoice ==2:
    print('What a shame. You LOSE!')
elif userChoice > computerChoice:
    print('YOU WIN!!! YOU HAVE BEATEN THE COMPUTER!!!')
