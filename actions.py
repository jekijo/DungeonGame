import random
from models import Player, Monster, Object


def cont():
    move_on = input('')


def intro():
    print('\n\n\n\n\nWelcome to the dungeon simulator. You will make a character and see if they can make it to the end'
          '\nof the dungeon without dying. Along the way you may find items. Red potions boost your strength,'
          '\nblue potions boost your speed, and steaks improve your health. Glowing items have a chance for a much'
          '\nbigger reward, but also for a massive negative effect. You can always choose to not pick up an item.'
          '\nYou will choose how many monsters you will need to defeat, and items may or may not be available.'
          '\nThis game relied HEAVILY on RNG. Press any key to continue the game when stops occur. Good luck.\n\n\n')


def choose_your_stats():
    stat_points = 100
    name = input("What is your player's name?: ")
    print('You have 100 base points to allot to your character')
    while stat_points != 0:
        strength = int(input("How many points would you like to give to strength?: "))
        stat_points -= strength
        print(f'You have {stat_points} points left.\n')
        speed = int(input("How many points would you like to give to speed?: "))
        stat_points -= speed
        print(f'You have {stat_points} points left.\n')
        health = int(input("How many points would you like to give to health?: "))
        stat_points -= health
        print(f'You have {stat_points} points left.\n')
        if stat_points < 0:
            print('You have overused your points. Do it right this time.\n')
            stat_points = 100
            continue
        if stat_points > 0:
            print('You still have points left, try again and make sure to use all of your points.')
            stat_points = 100
            continue
        print(f"\nYour stats are:\nStrength: {strength}\nSpeed: {speed}\nHealth: {health}")
    player1 = Player(name, health, strength, speed)
    print('Your stats are now locked.')
    return player1


def m_creation():
    monster_speed = random.randint(5, 50)
    monster_strength = random.randint(5, 40)
    monster_health = random.randint(15, 70)
    monster1 = Monster(monster_health, monster_strength, monster_speed)
    return monster1


def objects():
    steak = Object('Steak', 20)
    glowing_steak_stat = random.randint(-30, 30)
    glowing_steak = Object('Glowing Steak', glowing_steak_stat)
    red_potion = Object('Red Potion', 10)
    glowing_red_potion_stat = random.randint(-20, 20)
    glowing_red_potion = Object('Dark Red Potion', glowing_red_potion_stat)
    blue_potion = Object('Blue Potion', 10)
    glowing_blue_potion_stat = random.randint(-20, 20)
    glowing_blue_potion = Object('Dark Blue Potion', glowing_blue_potion_stat)
    return steak, glowing_steak, red_potion, glowing_red_potion, blue_potion, glowing_blue_potion


def confrontation(player, monster):
    if player.speed > monster.speed:
        goes_first = player.name
    elif player.speed < monster.speed:
        goes_first = 'Monster'
    else:
        num = random.randint(1, 2)
        if num == 2:
            goes_first = player.name
        else:
            goes_first = 'monster'
    print(f'\nMonster stats:\nHealth: {monster.health}\nSpeed: {monster.speed}\nStrength: {monster.strength}')
    print(f'\nPlayer stats:\nHealth: {player.health}\nSpeed: {player.speed}\nStrength: {player.strength}')
    cont()
    print(f"\n{goes_first} attacked first.")
    cont()
    if goes_first == player.name:
        while (player.health > 0) and (monster.health > 0):
            monster.health -= player.strength
            print(f'Monster lost {player.strength} points of health!')
            print(f'Monster has {monster.health} points of health left.')
            cont()
            if monster.health > 0:
                player.health -= monster.strength
                print(f'{player.name} lost {monster.strength} points of health!')
                print(f'{player.name} has {player.health} points of health left.')
                cont()
            else:
                break
    else:
        while (player.health > 0) and (monster.health > 0):
            player.health -= monster.strength
            print(f'{player.name} lost {monster.strength} points of health!')
            print(f'{player.name} has {player.health} points of health left.')
            cont()
            if player.health > 0:
                monster.health -= player.strength
                print(f'Monster lost {player.strength} points of health!\n')
                print(f'Monster has {monster.health} points of health left.')
                cont()
            else:
                break
    if player.health <= 0:
        print(f'{player.name} has died. GAME OVER')
        return 'dead'
    else:
        print(f"The monster has died. {player.name} has {player.health} health points left.")
        return True


def item_pickup(s, gs, r, gr, b, gb):
    chance = random.randint(1, 100)
    if 1 <= chance <= 8:
        choice = input('You found a glowing steak! Would you like to pick it up?:(y/n) ')
        if choice == 'y':
            return 'gs'
        else:
            print('You chose to walk away.')
    elif 8 < chance <= 17:
        choice = input('You found a glowing red potion! Would you like to pick it up?:(y/n) ')
        if choice == 'y':
            return 'gr'
        else:
            print('You chose to walk away.')
    elif 17 < chance <= 25:
        choice = input('You found a glowing blue potion! Would you like to pick it up?:(y/n) ')
        if choice == 'y':
            return 'gb'
        else:
            print('You chose to walk away.')
    elif 25 < chance <= 45:
        choice = input('You found a steak! Would you like to pick it up?:(y/n) ')
        if choice == 'y':
            return 's'
        else:
            print('You chose to walk away.')
    elif 45 < chance <= 65:
        choice = input('You found a red potion! Would you like to pick it up?:(y/n) ')
        if choice == 'y':
            return 'r'
        else:
            print('You chose to walk away.')
    elif 65 < chance <= 78:
        choice = input('You found a blue potion! Would you like to pick it up?:(y/n) ')
        if choice == 'y':
            return 'b'
        else:
            print('You chose to walk away.')
    else:
        print('You did not find an item :(')

