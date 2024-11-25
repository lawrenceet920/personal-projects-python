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
monster_stats = statline('Bat', 50, 0, 10, 25)
player_stats = statline(input('what is your name?\n     '), 100, 0, 50, 100)
gold = 100
phase = 'combat'
player_haste = 0
pickspell = False
# Spells
# Spell layout  0 name, 1description 2 min damage, 3 max damage, 4 total casts, 5 casts left, 6+ special effects
def new_spell(name, description, min_d, max_d, casts):
    '''Creates new basic spell'''
    return [name, description, min_d, max_d, casts, casts]
cantrip = new_spell('Firebolt', 'Your basic relyable attack, low damage', 5, 10, 100)
heal = new_spell('Cure Wounds', 'heal yourself, medium healing', 50, 100, 3)
spell3 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
# spell4 = new_spell('Dev.kill', 'testing 123', 1000, 1001, 10)

def random_spell():
    SPELL_COUNT = 7
    rand = random.randint(1, SPELL_COUNT)
    # Luck modifier
    rand += int(player_stats[1])
    if rand > SPELL_COUNT:
        rand = SPELL_COUNT
    elif rand < 1:
        rand = 1
    # pick spell from list based on roll + luck
    if rand == 1:
        player_stats[1] += 2
        return new_spell('Quarter-staff', 'Low damage', 7, 13, 100)
    elif rand == 2:
        player_stats[1] += 1
        return new_spell('Lightning', 'Meduim damage', 20, 30, 10)
    elif rand == 3:
        return new_spell('Drain Life', 'Medium damage and heal', 0, 0, 3)
    elif rand == 4:
        return new_spell('Fireball', 'high damage', 30, 50, 5)
    elif rand == 5:
        return new_spell('Chaos Bolt', 'Wildly varying damage', 0, 100, 5)
    elif rand == 6:
        return new_spell('Power Word Kill', 'A single use spell use it wisely', 9998, 9999, 1)
    elif rand == 7:
        player_stats[1] -= 1
        return new_spell('Haste', 'Take 2 additional actions (stacks)', 0, 0, 5)
# Unique Spells
def spell_nothing():
    print('You do nothing at all')

def spell_drain_life():
    attack_damage = random.randint(20, 30) 
    attack_damage += attack_damage * (player_stats[2] / 100)
    monster_stats[4] -= int(attack_damage)
    player_stats[4] += 10
    print(f'You did {attack_damage} damage to the monster, and healed yourself by 10!')

def spell_haste():
    global player_haste
    player_haste += 3

# Player & turn functions
def options():
    print(f'1: {cantrip[0]} : {cantrip[1]}')
    print(f'2: {heal[0]} : {heal[1]} : {heal[5]} casts left (restocks automaticly on shop)')
    print(f'3: {spell3[0]} : {spell3[1]} : {spell3[5]} casts left')
    print(f'4: {spell4[0]} : {spell4[1]} : {spell4[5]} casts left')
# End turn
def turn_end():
    global turn
    global player_haste
    if player_haste > 0:
        player_haste -= 1
        print(f'\nYou are hasted ({player_haste} turns left)\n')
        time.sleep(0.5)
    else:
        turn = 'stage'

def levelup(exp):
    print(f'You leveled up!')
    player_stats[2] += exp / 10
    player_stats[3] += exp
    player_stats[4] += exp
    player_stats[0] += exp / 2
    print(f'You got {exp * 30} gold')
    return exp * 30
# Game loop
turn = 'stage'
time.sleep(0.5)

while phase != 'game over':
    # Combat
    while phase == 'combat':
        # Turn Decider
        initiative_total = player_stats[0] + monster_stats[0]
        turn_picker = random.randint(1, initiative_total)
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
                    attack_damage = random.randint(cantrip[2], cantrip[3]) 
                    attack_damage += attack_damage * (player_stats[2] / 100)
                    monster_stats[4] -= int(attack_damage)
                    print(f'You did {attack_damage:.0f} damage to the monster!')
                    turn_end()
                elif player_action == '2':
                    if heal[0] == 'Nothing':
                        spell_nothing()
                    else:
                        attack_damage = random.randint(heal[2], heal[3]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        player_stats[4] += int(attack_damage)
                        print(f'You healed yourself for {attack_damage:.0f} health!')
                        # max health
                        if player_stats[4] > player_stats[3]:
                            player_stats[4] = player_stats[3]
                    heal[5] -= 1
                    if heal[5] == 0:
                        print(f'You Ran out of casts for {heal[0]} (They will restock when you enter the shop)')
                        heal = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn_end()
                elif player_action == '3':
                    # Unique Spell slot 1
                    if spell3[0] == 'Nothing':
                        spell_nothing()
                    elif spell3[0] == 'Drain Life':
                        spell_drain_life()
                    elif spell3[0] == 'Haste':
                        spell_haste()
                    else:
                        attack_damage = random.randint(spell3[2], spell3[3]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage:.0f} damage to the monster!')

                    spell3[5] -= 1
                    if spell3[5] == 0:
                        print(f'You Ran out of casts for {spell3[0]}')
                        spell3 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn_end()
                elif player_action == '4':
                    # Unique Spell slot 2
                    if spell4[0] == 'Nothing':
                        spell_nothing()
                    elif spell4[0] == 'Drain Life':
                        spell_drain_life()
                    elif spell4[0] == 'Haste':
                        spell_haste()
                    else:
                        attack_damage = random.randint(spell4[2] + player_stats[1], spell4[3] + player_stats[1]) 
                        attack_damage += attack_damage * (player_stats[0] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage:.0f} damage to the monster!')

                    spell4[5] -= 1
                    if spell4[5] == 0:
                        print(f'You Ran out of casts for {spell4[1]}')
                        spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn_end()
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
                percent_health = monster_stats[4] / monster_stats[3]
                if percent_health > 0.5:
                    percent_health = 0.5
                attack_damage = monster_stats[2] + monster_stats[1]
                attack_damage = attack_damage * (percent_health + 0.5)
                player_stats[4] -= int(attack_damage)
                print(f'The {monster_stats[5]} attacks for {attack_damage:.0f} damage!')
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
        # name, initiative, luck, power, max_hp
        if monster_stats[5] == 'Bat':
            gold += levelup(5)
            monster_stats = statline('Goblin', 75, 0, 10, 70)
            monster_intro = 'The first true battle of an adventure'
        elif monster_stats[5] == 'Goblin':
            gold += levelup(10)
            monster_stats = statline('Troll', 30, 0, 30, 150)
            monster_intro = 'A slow powerful monster'
        elif monster_stats[5] == 'Troll':
            gold += levelup(15)
            monster_stats = statline('Royal Guard', 100, 0, 20, 100)
            monster_intro = 'Into the palice no turning back now'
        elif monster_stats[5] == 'Royal Guard':
            gold += levelup(20)
            monster_stats = statline('PJ', 400, 0, 20, 200)
            monster_intro = 'The first trial to fight the king.'
        elif monster_stats[5] == 'PJ':
            gold += levelup(30)
            monster_stats = statline('Matthew', 25, 0, 100, 250)
            monster_intro = 'The second trial to fight the king.'
        elif monster_stats[5] == 'Matthew':
            gold += levelup(30)
            monster_stats = statline('Trent', 100, 0, 20, 500)
            monster_intro = 'The final trial before the king'
        elif monster_stats[5] == 'Trent':
            gold += levelup(30)
            monster_stats = statline('King', player_stats[1], 0, player_stats[2], player_stats[3])
            monster_intro = 'You finally stand before the king, now strike.'
        else:
            monster_stats = statline('Reaper', monster_stats[0] * 2, monster_stats[1] * 2, monster_stats[2] * 2, monster_stats[3] * 2)
            monster_intro = 'You won! now fall.\nDeath attacks for 500 damage!'
            player_stats[4] -= 500
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
        print(f'2: Full heal: 100gp     Current health:{(player_stats[4]/player_stats[3]*100):.0f}% HP')
        print(f'3: PJ\'s boots (+ initiative): {(player_stats[0] * 2):.0f}gp')
        print(f'4: Matthew\'s gloves (+ power): {(player_stats[2] * 4):.0f}gp')
        print(f'5: Trent\'s Armor (+ max health) {(player_stats[3] * 0.2):.0f}gp')
        print('6: Random new spell: 250gp')
        print('7: Upgrade cantrip: 300gp')

        # Player Input
        buy = input('\n ')
        if buy == '2':
            if gold > 99:
                gold -= 100
                player_stats[4] = player_stats[3]
                print('Your health is now maxxed!\n')
        elif buy == '3':
            if gold > player_stats[0] - 1:
                gold -= player_stats[0] * 2
                player_stats[0] += int(player_stats[0]) / 10
                print(f'Your initiative is now {player_stats[0]}.\n')
        elif buy == '4':
            if gold > (player_stats[2] * 4) - 1:
                gold -= player_stats[2] * 4
                player_stats[2] += int(player_stats[2]) / 10
                print(f'Your power is now {player_stats[2]}.\n')
        elif buy == '5':
            if gold > (player_stats[3] * 0.2) - 1:
                gold -= player_stats[3] * 0.2
                player_stats[3] += int(player_stats[3] / 10)
                print(f'Your max health is now {player_stats[3]}.\n')
        elif buy == '6':
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
        elif buy == '7':
            if gold > 299:
                gold -= 300
                cantrip[2] += 1
                cantrip[3] += 2
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