# Ethan Lawrence
# November 8 2024
# Untitled Project

import random
# Start
'''
Plan:
Battler:
fight foe, Win/Lose, Get buffs for next fight, Fight boss & win
buffs: new spells / more options, more damage, faster innititive
'''
# stat order:   0 initiative, 1 luck, 2 power, 3 max health, 4 current health, 5 name
player_stats = [100, 5, 50, 1000, 1000]
monster_stats = [50, 0, 10, 100, 100, 'bat']
phase = 'combat'

# Spells
# Spell layout  0 name, 1description 2 min damage, 3 max damage, 4 total casts, 5 casts left, 6+ special effects
spell1 = ['Firebolt', 'Your basic relyable attack, low damage', 5, 10, 100, 100]
spell2 = ['Cure Wounds', 'heal yourself, medium healing', 5, 10, 3, 3]
spell3 = ['Wait', 'Do nothing at all']

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
            print(f'it is the {turn}\'s turn.')
            print(f'Your health is {int(player_stats[4])}/{int(player_stats[3])}')
            print(f'{monster_stats[5]} health is {int(monster_stats[4])}/{int(monster_stats[3])}')
            while turn == 'player':
                print(f'{spell1[0]} : {spell1[1]}')
                print(f'{spell2[0]} : {spell2[1]}')
                player_action = input('What do you do?:     ')
                # Player Actions
                if player_action == spell1[0]:
                    attack_damage = random.randint(spell1[2] + player_stats[1], spell1[3] + player_stats[1]) 
                    attack_damage += attack_damage * (player_stats[2] / 100)
                    monster_stats[4] -= int(attack_damage)
                    print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == spell2[0]:
                    attack_damage = random.randint(spell2[2] + player_stats[1], spell2[3] + player_stats[1]) 
                    attack_damage += attack_damage * (player_stats[2] / 100)
                    player_stats[4] += int(attack_damage)
                    print(f'You did {attack_damage} damage to the monster!')
                    turn = 'stage'
                elif player_action == spell3[0]:
                    print('You stand there like a fool.')
                    player_stats[0] = 1
                    player_stats[1] = 0
                    turn = 'stage'
                else:
                    print('Oops that wasn\'t an option try again (capitalisation matters)')
            # End Of Player turn while
        else:
            # Monster turn
            turn = 'monster'
            print(f'it is the {monster_stats[5]}\'s turn.')
            while turn == 'monster':
                # (monster_stats[4] + monster_stats[1], monster_stats[3] + monster_stats[1])
                attack_damage = random.randint(monster_stats[4], monster_stats[3]) 
                attack_damage += attack_damage * (monster_stats[2] / 100)
                player_stats[4] -= int(attack_damage)
                print(f'The monster attacks for {attack_damage} damage!')
                turn = 'stage'
        # Health Check
        if player_stats[4] < 1:
            phase = 'game over'
        elif monster_stats[4] < 1:
            phase = 'battle won'
    # End Of combat While statement
    while phase == 'battle won':
        print('You won the battle!')
        phase = 'shop'
    while phase == 'shop':
        print('Welcome to the shop!')
        monster_stats = [50, 0, 10, 100, 100, 'new monster']
        phase = 'end'

if phase == 'game over':
    print('You lose!')
    phase = 'end'