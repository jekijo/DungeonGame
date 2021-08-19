from actions import intro, choose_your_stats, objects, confrontation, item_pickup, cont, cont2, m_creation


game_score = 0
intro()
player1 = choose_your_stats()
game_rounds = int(input('How many monsters would you like to fight?: '))
print()
current_round = 1
game_on = True
while game_on:
    for i in range(1, game_rounds + 1):
        monster1 = m_creation()
        damage_count = monster1.health
        (item1, item2, item3, item4, item5, item6) = objects()
        print(f"\nConfrontation number {current_round}\n----------------------\n")
        cont2()
        game_on = confrontation(player1, monster1)
        if game_on == 'dead':
            break
        item_found = item_pickup(item1, item2, item3, item4, item5, item6)
        if item_found == 'gs':
            player1.health += item2.effect
            print(f"Health changed by {item2.effect}. Player health is now: {player1.health}")
            cont2()
        if item_found == 'gr':
            player1.strength += item4.effect
            print(f"Strength changed by {item4.effect}. Player strength is now: {player1.strength}")
            cont2()
        if item_found == 'gb':
            player1.speed += item6.effect
            print(f"Speed changed by {item6.effect}. Player speed is now: {player1.speed}")
            cont2()
        if item_found == 'b':
            player1.speed += item5.effect
            print(f"Speed changed by {item5.effect}. Player speed is now: {player1.speed}")
            cont2()
        if item_found == 'r':
            player1.strength += item3.effect
            print(f"Strength changed by {item3.effect}. Player strength is now: {player1.strength}")
            cont2()
        if item_found == 's':
            player1.health += item1.effect
            print(f"Health changed by {item1.effect}. Player health is now: {player1.health}")
            cont2()
        if player1.health <= 0:
            print(f'{player1.name} has died. GAME OVER')
            break
        current_round += 1
        game_score += damage_count
        if current_round == 5 and game_rounds > 5:
            print(f'Congrats, {player1.name} made it five rounds. They found a nice fire to relax by. Health +50.')
            player1.health += 50
    if game_on == 'dead':
        break
    else:
        print(f'YOU WIN! You had {player1.health} health points left.\n')
        if player1.health >= 50:
            print('You cleared the cave easily.')
            game_score += 20
        if 11 <= player1.health < 20:
            print('You\'re a little scratched, but alive.')
            game_score += 10
        if player1.health < 11:
            print('You barely made it out alive.')
        game_on = False

game_score *= current_round
print('\nThe game has ended.')
print(f'\nYour score was {game_score}.')