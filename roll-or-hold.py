# Ethan Lawnrence
# Nov 1 2024
# Roll or hold

import random
import sys

print('Hello, welcome to roll or hold, you will roll a 20 sided die, then will choose if you want to roll again to raise your number, or hold the number. If you can beat my score you win, if you go over 40 you lose. \n')
input('Type anything to begin. \n')

# Player Rolls
score = random.randint(1, 20)
while score < 40:
    reroll = input(f'Your current score is {score}, Roll again? input either y or n:     ').lower()
    if reroll in ['n', 'no']:
        break
    elif reroll in ['y', 'yes']:
        score += random.randint(1, 20)
    else:
        print('OOPS! please either type "y" or "n"')
else:
    sys.exit('You went over 40! Game over!')

# AI Rolls
print(f'Your final score is {score}, My turn!')
ai_score = 0
while ai_score < 40:
    print(f'My score is now {ai_score}')
    if ai_score > score:
        break
    ai_score += random.randint(1, 20)
else:
    print('Fiddlesticks! I pushed too far and rolled over 40.')
    ai_score = 0

# Final Score
if score > ai_score:
    print('You win!')
else:
    print(f'My score of {ai_score} is more then your\'s at {score}. I win!')