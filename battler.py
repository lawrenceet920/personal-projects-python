# Ethan Lawrence
# November 8 2024
# Battler

import random
import time
print('Use "stats" in combat to see your stats\n')
# Character creator
# stat order:   0 initiative, 1 luck, 2 power, 3 max health, 4 current health, 5 name
def statline(name, initiative, luck, power, max_hp):
    '''Creates new statline'''
    return [initiative, luck, power, max_hp, max_hp, name]
monster_stats = statline('Bat', 50, 0, 10, 100)
player_stats = statline(input('what is your name?\n     '), 100, 5, 50, 1000)
gold = 0
phase = 'combat'

# Spells
# Spell layout  0 name, 1description 2 min damage, 3 max damage, 4 total casts, 5 casts left, 6+ special effects
def new_spell(name, description, min_d, max_d, casts):
    '''Creates new basic spell'''
    return [name, description, min_d, max_d, casts, casts]
cantrip = new_spell('Firebolt', 'Your basic relyable attack, low damage', 5, 10, 100)
heal = new_spell('Cure Wounds', 'heal yourself, medium healing', 50, 100, 3)
spell3 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
print('')
# Unique Spells
def spell_nothing():
    print('You do nothing at all')

time.sleep(0.5)
# Game loop
while phase != 'game over':
    # Combat
    while phase == 'combat':
        # Turn Decider
        initiative_total = player_stats[0] + monster_stats[0]
        turn_picker = random.randint(1, initiative_total) - player_stats[1] + monster_stats[1]
        print('')
        if turn_picker < player_stats[0]:
            # player turn
            turn = 'player'
            # Give information
            print(f'    it is {player_stats[5]}\'s turn.')
            time.sleep(0.5)
            while turn == 'player':
                print(f'1: {cantrip[0]} : {cantrip[1]}')
                print(f'2: {heal[0]} : {heal[1]}')
                print(f'3: {spell3[0]} : {spell3[1]}')
                print(f'4: {spell4[0]} : {spell4[1]}')
                player_action = input('What do you do?:     ')
                # Player Actions
                if player_action == '1':
                    attack_damage = random.randint(cantrip[2] + player_stats[1], cantrip[3] + player_stats[1]) 
                    attack_damage += attack_damage * (player_stats[2] / 100)
                    monster_stats[4] -= int(attack_damage)
                    print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == '2':
                    attack_damage = random.randint(heal[2] + player_stats[1], heal[3] + player_stats[1]) 
                    attack_damage += attack_damage * (player_stats[2] / 100)
                    player_stats[4] += int(attack_damage)
                    print(f'You healed yourself for {attack_damage} health!')
                    turn = 'stage'
                elif player_action == '3':
                    # Unique Spell slot 1
                    if spell3[0] == 'Nothing':
                        spell_nothing()
                    else:
                        attack_damage = random.randint(spell3[2] + player_stats[1], spell3[3] + player_stats[1]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == '4':
                    # Unique Spell slot 2
                    if spell3[0] == 'Nothing':
                        spell_nothing()
                    else:
                        attack_damage = random.randint(spell4[2] + player_stats[1], spell4[3] + player_stats[1]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == '/kill':
                    attack_damage = 99999
                    monster_stats[4] -= int(attack_damage)
                    print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == 'stats':
                    print(f'\nYour health is {int(player_stats[4])}/{int(player_stats[3])}')
                    print(f'{monster_stats[5]} health is {int(monster_stats[4])}/{int(monster_stats[3])} \n')
                    time.sleep(0.5)
                else:
                    print('Oops that wasn\'t an option try again (1, 2, 3, or 4)')
            # End Of Player turn while
        else:
            # Monster turn
            turn = 'monster'
            print(f'    it is the {monster_stats[5]}\'s turn.')
            time.sleep(0.5)
            while turn == 'monster':
                # (monster_stats[4] + monster_stats[1], monster_stats[3] + monster_stats[1])
                attack_damage = random.randint(monster_stats[4], monster_stats[3]) 
                attack_damage += attack_damage * (monster_stats[2] / 100)
                player_stats[4] -= int(attack_damage)
                print(f'The monster attacks for {attack_damage} damage!')
                turn = 'stage'

        if turn == 'stage':
            # Health Check
            time.sleep(0.5)
            if player_stats[4] < 1:
                phase = 'game over'
            elif monster_stats[4] < 1:
                phase = 'battle won'

    # End Of combat While statement
    time.sleep(1)
    while phase == 'battle won':
        print('\nYou won the battle!')
        print(f'You got {monster_stats[3]} gold')
        gold += monster_stats[3]
        # name, initiative, luck, power, max_hp
        if monster_stats[5] == 'Bat':
            monster_stats = statline('Goblin', 75, 3, 50, 250)
        else:
            monster_stats = statline('Reaper', monster_stats[0] * 2, monster_stats[1] * 2, monster_stats[2] * 2, monster_stats[3] * 2)
        print(f'Up next is a {monster_stats[5]}\n')
        input('Ready to continue?\n')
        phase = 'shop'

    while phase == 'shop':
        print('\nWelcome to the shop! \nHere is what you can buy\nOr you can buy nothing and leave')
        print(f'you have {gold} gold\n')

        # Options
        print('Full heal: 100')
        print(f'Improved boots: {player_stats[0]}')
        print('Nothing: Free!')
        # Player Input
        buy = input('\n ')
        if buy == 'Full heal':
            if gold > 99:
                gold -= 100
                player_stats[3] = player_stats[4]
        elif buy == 'Nothing':
            phase = 'combat'
        else:
            print('Oops, capitalisation matters\n')

if phase == 'game over':
    print('You lose!')
    phase = 'end'