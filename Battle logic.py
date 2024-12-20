import random
from pokemon_list import pokemon_data

def choose_move(pokemon):
    print(f"Choose a move for {pokemon}:")
    for i, move in enumerate(pokemon_data[pokemon]["Moves"], 1):
        print(f"{i}. {move}")
    choice = int(input("Enter the number of the move: ")) - 1
    move = pokemon_data[pokemon]["Moves"][choice]
    move_name, damage = move.split(" (")
    damage = int(damage[:-1])
    return move_name, damage

def battle():
    print("Welcome to Pokémon Battle!")

    # choose a Pokémon
    player_pokemon = input("Choose your Pokémon: ")
    if player_pokemon not in pokemon_data:
        print("Invalid Pokémon. Try again.")
        return

    # Random Pokémon
    opponent_pokemon = random.choice(list(pokemon_data.keys()))
    print(f"Your opponent chose {opponent_pokemon}!")

    
    player_hp = pokemon_data[player_pokemon]["HP"]
    opponent_hp = pokemon_data[opponent_pokemon]["HP"]

    # Battle loop
    while player_hp > 0 and opponent_hp > 0:
        print(f"\n{player_pokemon}: {player_hp} HP")
        print(f"{opponent_pokemon}: {opponent_hp} HP")

        # Player's turn
        move_name, damage = choose_move(player_pokemon)
        print(f"{player_pokemon} used {move_name}! It dealt {damage} damage!")
        opponent_hp -= damage

        if opponent_hp <= 0:
            print(f"{opponent_pokemon} fainted! You win!")
            break

        # Opponent's turn
        opp_move = random.choice(pokemon_data[opponent_pokemon]["Moves"])
        opp_move_name, opp_damage = opp_move.split(" (")
        opp_damage = int(opp_damage[:-1])
        print(f"{opponent_pokemon} used {opp_move_name}! It dealt {opp_damage} damage!")
        player_hp -= opp_damage

        if player_hp <= 0:
            print(f"{player_pokemon} fainted! You lose!")
            break

if __name__ == "__main__":
    battle()
