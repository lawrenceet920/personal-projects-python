# Ethan Lawnrence
# Nov 4 2024
# Higher or lower

import random

magic_number = random.randint(1, 100)

print('Welcome to higher or lower, In 5 moves guess my number, and I will tell you if it it higher or lower then mine')

for x in range(1, 6):
    guess = int(input(f'Round {x}, enter your guess:    '))
    if guess == magic_number:
        print('Correct, you win!')
        break
    elif guess < magic_number:
        print('Your guess is LOWER then the magic number.\n')
    elif guess > magic_number:
        print('Your guess is HIGHER then the magic number.\n')
    else:
        print('ERROR PLEASE RETRY PROGRAM')
else:
    print(f'You ran out of guesses the number was {magic_number}')