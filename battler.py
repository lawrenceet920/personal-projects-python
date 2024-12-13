# Ethan Lawrence
# November 8 2024
# Battler

import random
import time

# --- Character creator --- #
# stat order:   0 initiative, 1 luck, 2 power, 3 max health, 4 current health, 5 name
def statline(name, initiative, luck, power, max_hp):
    '''Creates new statline'''
    return [initiative, luck, power, max_hp, max_hp, name]



# --- Spells --- #

# Spell layout  0 name, 1description 2 min damage, 3 max damage, 4 total casts, 5 casts left, 6+ special effects
def new_spell(name, description, min_d, max_d, casts):
    '''Creates new basic spell'''
    return [name, description, min_d, max_d, casts, casts]
def random_spell():
    '''Picks a random spell from the spell list'''
    SPELL_COUNT = 7
    rand = random.randint(1, SPELL_COUNT)
    global player_class
    # Luck modifier
    rand += int(player_stats[1])
    if rand > SPELL_COUNT:
        rand = SPELL_COUNT
    elif rand < 1:
        rand = 1
    
        # Spell table
    if player_class == 'Mage': # Mage Spells
        if rand == 1:
            player_stats[1] += 2
            return new_spell('Quarter-staff', 'Consistant, but Low damage', 10, 11, 100)
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
            return new_spell('Slow', 'Skip the monsters next turn', 0, 0, 1)
        elif rand == 7:
            player_stats[1] -= 1
            return new_spell('Teleport', 'Go directly to the shop (gain 500 gold) and then return to the fight', 0, 0, 1)   # Test me
        # Fighter
    elif player_class == 'Fighter':
        if rand == 1:
            player_stats[1] += 2
            return new_spell('Mace', 'low damage', 15, 20, 5)
        elif rand == 2:
            player_stats[1] += 1
            return new_spell('Greatsword', 'Meduim relyable damage', 20, 25, 20)
        elif rand == 3:
            return new_spell('Warpick', 'Gain gold equil to damage, Meduim damage', 0, 0, 5)
        elif rand == 4:
            return new_spell('Greataxe', 'high damage', 25, 40, 10)
        elif rand == 5:
            return new_spell('Flame Sword', 'HUGE damage', 70, 100, 3)
        elif rand == 6:
            return new_spell('Potion of Strength', 'Do far more damage for an attack', 0, 0, 1)
        elif rand == 7:
            player_stats[1] -= 1
            return new_spell("Potion of Giant's Strength", 'A single use potion use it wisely', 999998, 999999, 1)
        # Rogue
    elif player_class == 'Rogue':
        if rand == 1:
            player_stats[1] += 2
            return new_spell('Twin Daggers', 'Low damage', 7, 13, 100)
        elif rand == 2:
            player_stats[1] += 1
            return new_spell('Poisoned Dagger', 'Meduim damage', 15, 25, 20)
        elif rand == 3:
            return new_spell('Net', 'Slow down your foe for the rest of the encounter', 0, 0, 1)
        elif rand == 4:
            return new_spell('Potion of grand healing', 'Fully Heal', 0, 0, 1)
        elif rand == 5:
            return new_spell('Haste', 'Take 2 additional actions (stacks)', 0, 0, 5)
        elif rand == 6:
            return new_spell('Crystal Dagger', 'high damage', 25, 100, 3)
        elif rand == 7:
            player_stats[1] -= 1
            return new_spell('Friendly Mimic', 'Gain a random ability (with +3 luck)', 0, 0, 2)

#  --- Unique Spells --- #
        
def spell_nothing():
    '''Blank Spell slot'''
    print('You do nothing at all')
def spell_drain_life():
    '''Heal player - damage foe'''
    attack_damage = random.randint(20, 30) 
    attack_damage += attack_damage * (player_stats[2] / 100)
    monster_stats[4] -= int(attack_damage)
    player_stats[4] += 10
    print(f'You did {attack_damage} damage to the monster, and healed yourself by 10!')
def spell_haste():
    '''Player takes 2 additional actions'''
    global player_haste
    player_haste += 3
def spell_slow():
    '''Monster loses next turn'''
    global monster_slow
    monster_slow += 1
def spell_net():
    '''Monster loses half speed'''
    monster_stats[0] = monster_stats[0] / 2
def spell_strength_potion():
    '''Player gains double power for 1 action *number is 2 for ending turn after cast'''
    global strength
    if strength == 0:
        player_stats[2] += player_stats[2]
        strength = 2
def spell_warpick():
    '''Attack that gives gold'''
    global gold
    attack_damage = random.randint(10, 30) 
    attack_damage += attack_damage * (player_stats[2] / 100)
    monster_stats[4] -= int(attack_damage)
    gold += int(attack_damage)
    print(f'You did {attack_damage} damage to the monster, and gained that much gold')

def spell_mimic():
    '''Pick a random class and gain a spell with +3 luck from it'''
    mimic = random.randint(1, 3)
    global player_class
    if mimic == 1:
        player_class = 'Mage'
    elif mimic == 2:
        player_class = 'Fighter'
    mimic = True
    player_stats[1] += 3
    while mimic == True: # False store
        question = input('Which slot do you want the spell in? 3 or 4:   ')
        time.sleep(0.5)
        if question == '3':
            global spell3
            spell3 = random_spell()
            print(f'You have a new spell! {spell3[0]}, {spell3[1]}')
            mimic = False
        elif question == '4':
            global spell4
            spell4 = random_spell()
            print(f'You have a new spell! {spell4[0]}, {spell4[1]}')
            mimic = False
        else:
            print('Enter either 3 or 4.')
    player_class = 'Rogue'
    player_stats[1] -= 3

def spell_grand_heal():
    '''Heal to full'''
    player_stats[4] = player_stats[3]
    print('Your health is now maxxed!\n')
def spell_teleport():
    '''Go to shop and gain 500 gold'''
    global phase
    global gold
    phase = 'shop'
    gold += 500

def odd_contraption():
    print('The machine whirls')
    rand = random.randint(1, 10)
    if rand < 4:
        attack_damage = random.randint(cantrip[2], cantrip[3]) 
        monster_stats[4] -= int(attack_damage)
        print(f'Blades shoot forth! You did {attack_damage:.0f} damage to the monster!')
    elif 3 < rand < 8:
        attack_damage = random.randint(cantrip[2], cantrip[3]) 
        attack_damage += attack_damage * (player_stats[2] / 100)
        monster_stats[4] -= int(attack_damage)
        print(f'Fire shoots forth! You did {attack_damage:.0f} damage to the monster!')
    elif 7 < rand < 10:
        attack_damage = random.randint(cantrip[2], cantrip[3]) 
        player_stats[4] -= int(attack_damage)
        print(f'A magical pulse explodes out! You did {attack_damage:.0f} damage to yourself!')
        attack_damage += attack_damage * (player_stats[2] / 25)
        monster_stats[4] -= int(attack_damage)
        print(f'You did {attack_damage:.0f} damage to the monster!')
    else:
        attack_damage = random.randint(cantrip[2], cantrip[3]) 
        attack_damage += attack_damage * (player_stats[2] / 25)
        monster_stats[4] -= int(attack_damage)
        print(f'Acid spews forth! You did {attack_damage:.0f} damage to the monster!')
    turn_end()

# --- Player & turn functions --- #
    
def options():
    print(f'1: {cantrip[0]} : {cantrip[1]}')
    print(f'2: {heal[0]} : {heal[1]} : {heal[5]} casts left')
    print(f'3: {spell3[0]} : {spell3[1]} : {spell3[5]} casts left')
    print(f'4: {spell4[0]} : {spell4[1]} : {spell4[5]} casts left')
# End turn
def turn_end():
    global turn
    global player_haste
    global strength
    if strength != 0:
        strength -= 1
        if strength == 0:
            player_stats[2] = player_stats[2] / 2
    if player_haste > 0:
        player_haste -= 1
        print(f'\nYou are hasted ({player_haste} turns left)\n')
        time.sleep(0.5)
    else:
        turn = 'stage'
        print('****************************')
# Level up
def levelup(exp):
    print(f'You leveled up!')
    player_stats[2] += exp / 10
    player_stats[3] += exp
    player_stats[4] += exp
    player_stats[0] += exp / 2
    print(f'You got {exp * 30} gold')
    if random.randint(1, 10) == 1:
        print('Fortune smiles on you')
        player_stats[1] += 1
    return exp * 30
# Tutorial
def play_tutorial(entry):
    global player_class
    print()
    if entry == 0:
        print('On your turn you pick 1 of 4 "spells" they will do a varity of things.')
        time.sleep(1)
        print('Your goal is to reduce your foe\'s health to 0.')
        time.sleep(1)
        print('Your first spell is always a infinite use low damage attack, a "Cantrip"!')
        time.sleep(1)
        print(f'This turn type "1" to use your {cantrip[0]} on the {monster_stats[5]}')
    elif entry == 1:
        print('On the monster\'s turn they will attack you!')
        time.sleep(1)
        print('If they reduce your health to 0 you lose the game!')
        time.sleep(1)
        print('On your turn do "/stats" to see how much health you have left.')
        time.sleep(1)
        print('If you are too low on hp, your second spell slot will heal you.')
        time.sleep(1)
        print('It will also restock automaticly after combat in the "Store".')
    elif entry == 2:
        print('After winning a combat you level up!')
        time.sleep(1)
        print('This will give you flat stat bonuses based on the monsters difficulty')
    elif entry == 3:
        print('You are now in the store!')
        time.sleep(1)
        print('any stat increse is persentage based in both cost and effectiveness, so it may not be a great idea to buy any until you have higher stats from levelups.')
        time.sleep(1)
        print('The most powerful purchaces are healing to full, or buying a new spell')
        time.sleep(1)
        print('however both are only short term upgrades, for now I would reccomend getting a new spell.')
    elif entry == 4:
        print('You just bought a new spell! there are 7 different you can get.')
        time.sleep(1)
        print(f'you only have 2 slots to hold it, but it is likly it is far more powerful then your {cantrip[0]}')
        time.sleep(1)
        if player_class == 'Mage':
            print('They are also unique to your class, so you will have entirely different abilitys compared to say a Rogue!')
        else:
            print('They are also unique to your class, so you will have entirely different abilitys compared to say a Mage!')
    time.sleep(3)
    tutorial[entry] = False
    print()

# --- Variables --- #

gold = 100
monster_stats = statline('Bat', 50, 0, 10, 25) # First monster VVV
monster_death = 'The bat screaches as it falls to the ground, wings torn, it is not, dead... but it is now helpless'
phase = 'combat'
turn = 'stage'
boss = False
bossphase = 1
# Blank spells
spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
# Unique spell variables
player_haste = 0
monster_slow = 0
strength = 1


# --- Start of game --- #

time.sleep(0.5)
print('\n\nUse "/stats" in combat to see your health')
time.sleep(0.2)
print('All multiple choice prompts, should be answered with a number\n')
time.sleep(2)
print('Your goal is to defeat the king.')
time.sleep(1)
print('\n\n\n')

while True:
    print('What class are you?')
    print('1: Fighter  (Beginner friendly)')
    print('2: Mage')
    print('3: Rogue')
    player_class = input("Awaiting Input: ")
    print()
    # Class picker
    if player_class == '1':
        player_class = 'Fighter'
        print('The noble fighter, a consistant and lasting type.') # Flavour text
        player_stats = statline(input(f'what is your name, {player_class}?\n     '), 100, -1, 75, 250)
        spell3 = new_spell('Handaxe', 'These things are heavy, best be rid of em sooner or later anyway', 10, 15, 2)
        cantrip = new_spell('Sword', 'Your basic relyable attack, low damage', 6, 13, 100)
        heal = new_spell('Second Wind', 'heal yourself, full healing', 1000, 1001, 1)
        break
    elif player_class == '2':
        player_class = 'Mage'
        print('The mystical mage, a fragile, but powerful one.') # Flavour text
        player_stats = statline(input(f'what is your name, {player_class}?\n     '), 75, 0, 125, 75)
        spell3 = new_spell('Spell Scroll', 'An old relic, but will do the job, shame though...', 30, 50, 1)
        cantrip = new_spell('Firebolt', 'Your basic relyable attack, low damage', 5, 10, 100)
        heal = new_spell('Cure Wounds', 'heal yourself, high healing', 30, 70, 3)
        break
    elif player_class == '3':
        player_class = 'Rogue'
        print('The tricky Rogue, as unpredictable as they are fast.') # Flavour text
        player_stats = statline(input(f'what is your name, {player_class}?\n     '), 200, 2, 0, 150)
        spell3 = new_spell('Acid Vial', 'Packs a punch, (and was all you could get before you left home)', 20, 30, 1)
        spell4 = new_spell('Twin Daggers', 'Better then 1', 7, 13, 100)
        cantrip = new_spell('Dagger', 'Your basic relyable attack, low damage', 5, 10, 100)
        heal = new_spell('Bandages', 'heal yourself, medium healing', 20, 30, 5)
        break
    else:
        print('oops try again!\n')
        time.sleep(1)

print('Do you want game tips?')
print('1: Yes, enable full tutorial')
print('2: No, disable all')
tutorial = input()
if tutorial == '2':
    tutorial = [False, False, False, False, False]
else:
    tutorial = [True, True, True, True, True]



# --- GAME LOOP --- #
time.sleep(0.5)

while phase != 'game over':
    # --- Combat --- #
    while phase == 'combat':
        # Turn Decider
        initiative_total = player_stats[0] + monster_stats[0]
        turn_picker = random.randint(1.0, int(initiative_total))
        print()
        if turn_picker < player_stats[0]:
            # --- PLAYER TURN --- #
            turn = 'player'
            # Give information
            print(f'    it is {player_stats[5]}\'s turn.')
            if tutorial[0]:
                play_tutorial(0)
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
                        # max health enforcer
                        if player_stats[4] > player_stats[3]:
                            player_stats[4] = player_stats[3]
                    heal[5] -= 1
                    if heal[5] == 0:
                        print(f'You Ran out of casts for {heal[0]}')
                        heal = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn_end()

                elif player_action == '3':
                    # -- Unique Spell slot 1 -- #
                    if spell3[0] == 'Nothing':
                        spell_nothing()
                    elif spell3[0] == 'Drain Life':
                        spell_drain_life()
                    elif spell3[0] == 'Haste':
                        spell_haste()
                    elif spell3[0] == 'Potion of Strength':
                        spell_strength_potion()
                    elif spell3[0] == 'Warpick':
                        spell_warpick()
                    elif spell3[0] == 'Potion of grand healing':
                        spell_grand_heal()
                    elif spell3[0] == 'Friendly Mimic':
                        spell_mimic()
                    elif spell3[0] == 'Slow':
                        spell_slow()
                    elif spell3[0] == 'Teleport':
                        spell_teleport()
                    elif spell3[0] == 'Net':
                        spell_net()
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
                    # -- Unique Spell slot 2 -- #
                    if spell4[0] == 'Nothing':
                        spell_nothing()
                    elif spell4[0] == 'Drain Life':
                        spell_drain_life()
                    elif spell4[0] == 'Haste':
                        spell_haste()
                    elif spell4[0] == 'Potion of Strength':
                        spell_strength_potion()
                    elif spell4[0] == 'Warpick':
                        spell_warpick()
                    elif spell4[0] == 'Potion of grand healing':
                        spell_grand_heal()
                    elif spell4[0] == 'Friendly Mimic':
                        spell_mimic()
                    elif spell4[0] == 'Slow':
                        spell_slow()
                    elif spell4[0] == 'Teleport':
                        spell_teleport()
                    elif spell4[0] == 'Net':
                        spell_net()
                    else:
                        attack_damage = random.randint(spell4[2], spell4[3]) 
                        attack_damage += attack_damage * (player_stats[2] / 100)
                        monster_stats[4] -= int(attack_damage)
                        print(f'You did {attack_damage:.0f} damage to the monster!')

                    spell4[5] -= 1
                    if spell4[5] == 0:
                        print(f'You Ran out of casts for {spell4[1]}')
                        spell4 = new_spell('Nothing', 'Do nothing at all', 0, 0, 1)
                    turn_end()

                elif player_action == '/devmode':
                    # devmode
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

            # --- End Of Player turn while --- #
                    
        else:
            # --- MONSTER TURN --- #
            turn = 'monster'
            print(f'    it is the {monster_stats[5]}\'s turn.')
            time.sleep(0.5)
            if tutorial[1]:
                play_tutorial(1)

            while turn == 'monster':
                if monster_slow == 0:
                    if boss == True and bossphase == 2: #   Final Boss moves
                        random_monster_move = random.randint(1, 100)
                        if 0 < random_monster_move < 51:
                            attack_damage = monster_stats[2]
                            player_stats[4] -= int(attack_damage)
                            print(f'The {monster_stats[5]} attacks for {attack_damage:.0f} damage!')
                        elif 50 < random_monster_move < 76:
                            monster_stats[4] += 25
                            print('The King heals for 25hp!')
                        elif 75 < random_monster_move < 91:
                            question = input('Which slot do you care least of? 3 or 4:   ')
                            time.sleep(0.5)
                            if question == '3':
                                spell3 = new_spell('Nothing', 'For you cannot stop me.', 0, 0, 1)
                                print(f'You have a new spell! {spell3[0]}, {spell3[1]}')
                            elif question == '4':
                                spell4 = new_spell('Nothing', 'For you have already lost', 0, 0, 1)
                                print(f'You have a new spell! {spell4[0]}, {spell4[1]}')
                            else:
                                print('Enter either 3 or 4.')
                        elif 90 < random_monster_move < 100:
                            print('The King glares at you, for some reason he is giving you time.')
                        elif random_monster_move == 100:
                            monster_stats = statline('King', player_stats[0], 0, player_stats[2] * 3, player_stats[3] * 2)
                            print('\n!&!&#%#&^$8@^*(@$%&@($*^$@&*^$^')
                            print("Even if you win my heir will take the throne, and finish what I have started. You cannot defeat me in a way that matters.")
                            print('!&!&#%#&^$8@^*(@$%&@($*^$@&*^$^\n')

                    else:   #   Regular monster
                        percent_health = monster_stats[4] / monster_stats[3]
                        if percent_health > 0.5:
                            percent_health = 0.5
                        attack_damage = monster_stats[2] + monster_stats[1]
                        attack_damage = attack_damage * (percent_health + 0.5)
                        player_stats[4] -= int(attack_damage)
                        print(f'The {monster_stats[5]} attacks for {attack_damage:.0f} damage!')
                else:
                    monster_slow = 0
                    print('The slow spell has ended')
                print('****************************')
                turn = 'stage'
        
        # --- STAGE CHECK --- #
        if turn == 'stage':
            # Health Check
            print()
            time.sleep(0.5)
            if player_stats[4] < 1:
                phase = 'game over'
            elif monster_stats[4] < 1:
                if boss == False:
                    phase = 'battle won'
                elif boss == True and bossphase == 1:
                    monster_stats = statline('King', player_stats[1] / 2, 0, player_stats[2] + 50, 1000)
                    print('\n!@#$%^%$#@!@#$%$@@#$%#$%$#!@#')
                    print("You didn\'t think it would be that easy, did you?")
                    print('!@#$%^%$#@!@#$%$@@#$%#$%$#!@#\n')
                    time.sleep(1)
                    bossphase = 2
                elif boss == True and bossphase == 2:
                    phase = 'game won'

    # --- End Of combat While statement --- #
                
    time.sleep(0.5)
    if strength != 0:
        strength = 0
        player_stats[2] = player_stats[2] / 2
    # --- BATTLE WON --- #
    while phase == 'battle won': # This is only a while to handle errors if this repeats in a row something has gone wrong
        print('\n#########################')
        print(monster_death)
        print('\nYou won the battle!')
        if tutorial[2]:
            play_tutorial(2)
        # name, initiative, luck, power, max_hp
        if monster_stats[5] == 'Bat':
            gold += levelup(5)
            monster_stats = statline('Goblin', 75, 0, 10, 70)
            monster_intro = 'The first true battle of an adventure'
            monster_death = 'The goblin falls over, you think it is a feint... then you are proven otherwise'
        elif monster_stats[5] == 'Goblin':
            gold += levelup(10)
            monster_stats = statline('Troll', 30, 0, 30, 150)
            monster_intro = 'A slow powerful monster'
            monster_death = 'The ground rumbles as it falls over the path over the moat is now open.'
        elif monster_stats[5] == 'Troll':
            gold += levelup(15)
            monster_stats = statline('Royal Guard', 100, 0, 20, 200)
            monster_intro = 'Into the palice no turning back now'
            monster_death = ' Their lasts words are: "You treasonous fool! don\'t do it!", you dont bother to remember.'
        elif monster_stats[5] == 'Royal Guard':
            gold += levelup(20)
            monster_stats = statline('PJ', 400, 0, 20, 300)
            monster_intro = 'The first trial to fight the king.'
            monster_death = 'He suddenly vanishes, he won\'t be in fighting shape until after you have won however!'
        elif monster_stats[5] == 'PJ':
            gold += levelup(30)
            monster_stats = statline('Matthew', 35, 0, 100, 300)
            monster_intro = 'The second trial to fight the king.'
            monster_death = 'He recoils at the last strike, you brace yourself, but the Arch-Mage will not see the next century.'
        elif monster_stats[5] == 'Matthew':
            gold += levelup(30)
            monster_stats = statline('Trent', 100, 0, 20, 600)
            monster_intro = 'The final trial before the king'
            monster_death = 'He finaly collapses from your onslaught, you question if the body will ever decompose.'
        elif monster_stats[5] == 'Trent':
            gold += levelup(30)
            monster_stats = statline('King', 100, 0, 50, 500)
            monster_intro = '!!!   You finally stand before the king, now strike while you can.   !!!'
            monster_death = 'You have won! It is over, your people are safe from this kingdom, may the rest of you clan have as much luck'
            boss = True
        else:
            # If no monster can be found this will show to solve the error : Check if there is a typo in what the monster should have been.
            monster_stats = statline('Reaper', monster_stats[0] * 2, monster_stats[1] * 2, monster_stats[2] * 2, monster_stats[3] * 2)
            monster_intro = 'Your eyes fog over, you have a feeling something has gone very wrong'
            monster_death = 'The strange vison fades, you have little time before it comes back.'
        print(f'Up next is a {monster_stats[5]}\n {monster_intro} \n')
        time.sleep(1)
        phase = 'shop'

    # --- SHOP --- #
    while phase == 'shop':
        if player_class == 'Mage':  # Restock healing
            heal = new_spell('Cure Wounds', 'heal yourself, high healing', 30, 70, 3)
        elif player_class == 'Fighter':
            heal = new_spell('Second Wind', 'heal yourself, full healing', 1000, 1001, 1)
        elif player_class == 'Rogue':
            heal = new_spell('Bandages', 'heal yourself, medium healing', 20, 30, 5)
        # Shop startup
        print('\nWelcome to the shop! \nHere is what you can buy\nOr you can buy nothing and leave')
        print(f'you have {gold:.0f} gold\n')
        time.sleep(0.5)
        if tutorial[3]:
            play_tutorial(3)

        # Options
        print('1: Leave store.')
        print(f'2: Full heal: 100gp     Current health:{(player_stats[4]/player_stats[3]*100):.0f}% HP')
        print(f'3: PJ\'s boots (initiative): {(player_stats[0] * 2):.0f}gp')
        print(f'4: Matthew\'s gloves (power): {(player_stats[2] * 4):.0f}gp')
        print(f'5: Trent\'s Armor (max health) {(player_stats[3] * 0.2):.0f}gp')
        print('6: Gain new spell (slot 3/4): 250gp')
        print('7: Upgrade cantrip (slot 1): 300gp')

        # Player Input (BUY STUFF) --- #
        buy = input('\n ')
        if buy == '2': # Heal
            if gold > 99:
                gold -= 100
                player_stats[4] = player_stats[3]
                print('Your health is now maxxed!\n')
            else:
                print('You do not have enough gold for that.')
                time.sleep(0.5)

        elif buy == '3': # Speed
            if gold > player_stats[0] - 1:
                gold -= player_stats[0] * 2
                player_stats[0] += int(player_stats[0]) / 10
                print(f'Your initiative is now {player_stats[0]}.\n')
            else:
                print('You do not have enough gold for that.')
                time.sleep(0.5)

        elif buy == '4': # Power
            if gold > (player_stats[2] * 4) - 1:
                gold -= player_stats[2] * 4
                player_stats[2] += int(player_stats[2]) / 10
                print(f'Your power is now {player_stats[2]}.\n')
            else:
                print('You do not have enough gold for that.')
                time.sleep(0.5)

        elif buy == '5': # Max Health
            if gold > (player_stats[3] * 0.2) - 1:
                gold -= player_stats[3] * 0.2
                player_stats[3] += int(player_stats[3] / 10)
                print(f'Your max health is now {player_stats[3]}.\n')
            else:
                print('You do not have enough gold for that.')
                time.sleep(0.5)

        elif buy == '6': # New Spell
            if gold > 249:
                if tutorial[4]:
                    play_tutorial(4)
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
            else:
                print('You do not have enough gold for that.')
                time.sleep(0.5)

        elif buy == '7': # Upgrade cantrip
            if gold > 299:
                gold -= 300
                cantrip[2] += 1
                cantrip[3] += 2
            else:
                print('You do not have enough gold for that.')
                time.sleep(0.5)

        elif buy == '1': # --- Quit --- #
            print('#########################')
            phase = 'combat'
        else:
            print('Oops, try again!\n')
            time.sleep(0.5)

        # Gold Check
        if gold == 0:
            print('You have run out of gold...')
            print('#########################')
            phase = 'combat'
if phase == 'game over':
    print('You lose!')
    print(f'Your final stat\'s: {player_class} : {player_stats}')
    phase = 'end'
elif phase == 'game won':
    print('You have won, the king is slain and your people are safe, you return to your home a hero.')