# Ethan Lawrence
# Oct 9 2024
# Choose your own Adventure
import time

hero_name = input('Old Man:     Hello adventurer and welcome to the kingdom of Chadlantus! \n Tell me, what is your name:   ')
weapon = 0

while weapon == 0:
    hero_class = input(f'Narrator:   {hero_name}, are you a mage, or a fighter? (input either "mage" or "fighter")  ')
    if hero_class == 'mage':
        weapon = input(f'Narrator:   {hero_name}, what is your spellcasting focus? is it a wand, a staff, or something entirly unique?  ')
    elif hero_class == 'fighter':
        weapon = input(f'Narrator:   {hero_name}, what is your weapon? is it a sword, a greataxe, or something entirly unique?')
    else:
        print('OOPS! Please input only mage or fighter!')

print(f'Old Man:    Well then mightly {hero_name}, you have done well to Chadlantus! Now mighty {hero_class}, I need aid please deliver this letter to my daughter in the capital.')
time.sleep(1)
# River
print('Narrator:    You set forth onto adventure, but suddenly you hit a roadblock, the bridge has collapsed!')
time.sleep(1)
if hero_class == 'mage':
    print('Narrator:    Thankfully a mage such as yourself finds no difficulty floating over the bridge with levitation magic.')
    river = 'use levitation magic to cross a river'
    time.sleep(3)
else: 
    river = input('Narrator:    How do you get across:      ')

# Thug
print('Narrator:    After passing the river you find yourself face to face with a thug!')
time.sleep(1)
print(f'Thug:   YOU! {hero_class} gimme that {weapon} or i\'ll... uh ... why are you standing like that give it!')
time.sleep(1)
if hero_class == 'fighter':
    print('Narrator:    You notice the incompitance of the thug and kick there leg and gesture threating them with your {weapon}, they can tell you far outclass them and run away.')
    thug = 'Scare away a thug'
    time.sleep(3)
else:
    thug = input('Narrator:     You are in swinging range of their sword and if you don\'t do somthing quick you won\'t leave here in one piece, what do you do:    ')

# Locate daughter
print('Narrator:    The thug dealt with you make your way to the capital, but you discover you forgot to ask where in the capital the Old man\'s daughter is')
time.sleep(1)
find_her = input('Narrator: You haven\'t time to leave and ask how do you try to find her?      ')
print('You are now face to face with her, you hand her the old man\'s letter and have completed your quest')
time.sleep(1)
print(f'Tou complete your quest you had to {river}, then {thug}, and then locate the daughter by, {find_her}. For these efforts you have been rewareded with 100 GP')