# Ethan Lawrence
# November 8 2024
# Battler

import random
import time
print('Use "/stats" in combat to see your stats\n')
# Character creator
# stat order:   0 initiative, 1 luck, 2 power, 3 max health, 4 current health, 5 name
def statline(name, initiative, luck, power, max_hp):
    '''Creates new statline'''
    return [initiative, luck, power, max_hp, max_hp, name]
monster_stats = statline('Bat', 50, 0, 10, 100)
player_stats = statline(input('what is your name?\n     '), 100, 5, 50, 10000)
gold = 0
phase = 'combat'


# Spells
# Spell layout  0 name, 1description 2 min damage, 3 max damage, 4 total casts, 5 casts left, 6+ special effects
def new_spell(name, description, min_d, max_d, casts):
    '''Creates new basic spell'''
    return [name, description, min_d, max_d, casts, casts]
cantrip = new_spell('Firebolt', 'Your basic relyable attack, low damage', 5, 10, 100)
heal = new_spell('Cure Wounds', 'heal yourself, medium healing', 500, 1000, 3)
spell3 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)

def random_spell(): 
    rand = random.randint(1, 3)
    if rand == 1:
        return new_spell('Kamehameha', 'high damage and can heal', 0, 0, 3)
    elif rand == 2:
        return new_spell('Fireball', 'high damage', 30, 50, 10)
    elif rand == 3:
        return new_spell('Power Word Kill', 'A single use spell use it wisely', 9998, 9999, 1)
# Unique Spells
def spell_nothing():
    print('You do nothing at all')
def spell_kamehameha():
    attack_damage = random.randint(20 + player_stats[1], 30 + player_stats[1]) 
    attack_damage += attack_damage * (player_stats[2] / 100)
    monster_stats[4] -= int(attack_damage)
    player_stats[4] += 10
    print(f'You did {attack_damage} damage to the monster, and healed yourself by 10!')

# Player turn functions
def options():
    print(f'1: {cantrip[0]} : {cantrip[1]}')
    print(f'2: {heal[0]} : {heal[1]} : {heal[5]} casts left (restocks automaticly on shop)')
    print(f'3: {spell3[0]} : {spell3[1]} : {spell3[5]} casts left')
    print(f'4: {spell4[0]} : {spell4[1]} : {spell4[5]} casts left')

# Game loop
turn = 'stage'
time.sleep(0.5)

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
                options()
                player_action = input('What do you do?:     ')
                # Player Actions
                if player_action == '1':
                    attack_damage = random.randint(cantrip[2] + player_stats[1], cantrip[3] + player_stats[1]) 
                    attack_damage += attack_damage * (player_stats[2] / 100)
                    monster_stats[4] -= int(attack_damage)
                    print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == '2':
                    if heal[0] == 'Nothing':
                        spell_nothing()
                    else:
                        attack_damage = random.randint(heal[2] + player_stats[1], heal[3] + player_stats[1]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        player_stats[4] += int(attack_damage)
                        print(f'You healed yourself for {attack_damage} health!')
                    heal[5] -= 1
                    if heal[5] == 0:
                        print(f'You Ran out of casts for {heal[0]} (They will restock when you enter the shop)')
                        heal = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn = 'stage'
                elif player_action == '3':
                    # Unique Spell slot 1
                    if spell3[0] == 'Nothing':
                        spell_nothing()
                    elif spell3[0] == 'Kamehameha':
                        spell_kamehameha()
                    else:
                        attack_damage = random.randint(spell3[2] + player_stats[1], spell3[3] + player_stats[1]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage} damage to the monster!')
                        spell3[5] -= 1
                        if spell3[5] == 0:
                            print(f'You Ran out of casts for {spell3[0]}')
                            spell3 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn = 'stage'
                elif player_action == '4':
                    # Unique Spell slot 2
                    if spell4[0] == 'Nothing':
                        spell_nothing()
                    elif spell3[0] == 'Kamehameha':
                        spell_kamehameha()
                    else:
                        attack_damage = random.randint(spell4[2] + player_stats[1], spell4[3] + player_stats[1]) 
                        attack_damage += attack_damage * (player_stats[0] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage} damage to the monster!')
                        spell4[5] -= 1
                        if spell4[5] == 0:
                            print(f'You Ran out of casts for {spell4[1]}')
                            spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn = 'stage'
                elif player_action == '/devmode':
                    player_stats[5] = 'dev'
                    print('You have entered devmode, type "exit" to leave...')
                    while turn == 'player':
                        player_action = input('Enter command:   /')
                        if player_action == 'kill':
                            attack_damage = 99999
                            monster_stats[4] -= int(attack_damage)
                            print('Success')
                        elif player_action == 'gold':
                            gold = 99999
                            print('Success')
                        elif player_action == 'fail':
                            player_stats[4] = 0
                            print('Success')
                        elif player_action == 'exit':
                            turn = 'stage'
                            print('Success \n')
                        else:
                            print('invalid command')
                elif player_action == '/stats':
                    print(f'\nYour health is {int(player_stats[4])}/{int(player_stats[3])}')
                    print(f'{monster_stats[5]} health is {int(monster_stats[4])}/{int(monster_stats[3])} \n')
                    time.sleep(0.5)
                else:
                    print('Oops that wasn\'t an option try again (1, 2, 3, or 4)')
                    time.sleep(0.5)
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
            print()
            time.sleep(0.5)
            if player_stats[4] < 1:
                phase = 'game over'
            elif monster_stats[4] < 1:
                phase = 'battle won'

    # End Of combat While statement
    time.sleep(0.5)
    while phase == 'battle won':
        print('\nYou won the battle!')
        print(f'You got {monster_stats[3]} gold')
        gold += monster_stats[3]
        # name, initiative, luck, power, max_hp
        if monster_stats[5] == 'Bat':
            monster_stats = statline('Goblin', 75, 3, 50, 250)
            monster_intro = 'The first true battle of an adventure'
        elif monster_stats[5] == 'Goblin':
            monster_stats = statline('PJ', 300, 10, 20, 250)
            monster_intro = 'The first trial to fight the king.'
        elif monster_stats[5] == 'PJ':
            monster_stats = statline('Matthew', 200, 7, 0, 4000)
            monster_intro = 'The second trial to fight the king.'
        elif monster_stats[5] == 'Mathew':
            monster_stats = statline('Final Boss', 200, 100, 100, 1000)
        else:
            monster_stats = statline('Reaper', monster_stats[0] * 2, monster_stats[1] * 2, monster_stats[2] * 2, monster_stats[3] * 2)
        print(f'Up next is a {monster_stats[5]}\n {monster_intro} \n')
        time.sleep(1)
        phase = 'shop'

    while phase == 'shop':
        heal = new_spell('Cure Wounds', 'heal yourself, medium healing', 50, 100, 3)
        print('\nWelcome to the shop! \nHere is what you can buy\nOr you can buy nothing and leave')
        print(f'you have {gold} gold\n')
        time.sleep(0.5)

        # Options
        print('1: Leave store.')
        print('2: Full heal: 100gp')
        print(f'3: Improved boots (+ initiative): {player_stats[0]}gp')
        print(f'4: Combat Training (+ power): {player_stats[2] * 2}gp')
        print('5: Random new spell: 250gp')
        print('6: Upgrade cantrip: 300gp')

        # Player Input
        buy = input('\n ')
        if buy == '2':
            if gold > 99:
                gold -= 100
                player_stats[3] = player_stats[4]
                print('Your health is now maxxed!\n')
        elif buy == '3':
            if gold > player_stats[0] - 1:
                gold -= player_stats[0]
                player_stats[0] += player_stats[0] / 10
                print(f'Your initiative is now {player_stats[0]}.\n')
        elif buy == '4':
            if gold > (player_stats[2] * 2) - 1:
                gold -= player_stats[2] * 2
                player_stats[2] += player_stats[2] / 10
                print(f'Your power is now {player_stats[2]}.\n')
        elif buy == '5':
            if gold > 249:
                gold -= 250
                question = input('Which slot do you want the spell in? 3 or 4:   ')
                time.sleep(0.5)
                if question == '3':
                    spell3 = random_spell()
                    print(f'You have a new spell! {spell3[0]}, {spell3[1]}')
                elif question == '4':
                    spell4 = random_spell()
                    print(f'You have a new spell! {spell4[0]}, {spell4[1]}')
                else:
                    print('Enter either 3 or 4.')
                time.sleep(1)
        elif buy == '6':
            if gold > 299:
                gold -= 300
                cantrip[2] += cantrip[2] * 0.1
                cantrip[3] += cantrip[3] * 0.2
        elif buy == '1':
            phase = 'combat'
        else:
            print('Oops, try again!\n')
            time.sleep(0.5)

        # Gold Check
        if gold == 0:
            print('You have run out of gold...')
            phase = 'combat'
if phase == 'game over':
    print('You lose!')
    phase = 'end'