import random

weapons = [1, 2, 3]
comp_action = random.randint(0, 2)
player = False


while not player:

    player_action = int(input("\nEnter your weapon ([1]rock, [2]paper, [3]scissors): "))

    if player_action == weapons[0]:
        player_action = "rock"
    elif player_action == weapons[1]:
        player_action = "paper"
    elif player_action == weapons[2]:
        player_action = "scissors"
    else:
        print("No match! Choose correct weapon.")

    if comp_action == 0:
        comp_action = "rock"
    elif comp_action == 1:
        comp_action = "paper"
    elif comp_action == 2:
        comp_action = "scissors"

    print(f"\nYou chose {player_action}, computer chose {comp_action}.\n")

    if player_action == comp_action:
        print(f"Both players selected {player_action}. It's a tie!")
    elif player_action == "rock":
        if comp_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_action == "paper":
        if comp_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_action == "scissors":
        if comp_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    new_game = input("\nDo you want another game? (y/n): ")
    if new_game == "y":
        player = False
    else:
        print("Thank you!")
        break