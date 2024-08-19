import random
game_counter = 1


def rules():
    return (
            "\n-> You will compete against the computer.\n"
            "-> Each round win equals 1 point.\n"
            "-> First to reach 2 points wins the game.\n"
            "-> You will be able to choose the game version: Classic or Extended.\n"
            "######CLASSIC GAME'S RULES ######\n"
            "1. Rock crushes scissors.\n"
            "2. Scissors cut paper.\n"
            "3. Paper covers rock.\n"
            "4. Otherwise, it is a tie!\n"
            "######EXTENDED GAME'S RULES ######\n"
            "1. Rock crushes Scissors and crushes Lizard.\n"
            "2. Scissors cuts Paper and decapitates Lizard.\n"
            "3. Paper covers Rock and disproves Spock.\n"
            "4. Rock crushes Lizard.\n"
            "5. Lizard poisons Spock and eats Paper.\n"
            "6. Spock smashes Scissors and vaporizes Rock.\n"
            "7. Otherwise, it is a tie!\n"
    )


def get_rules_preference():
    print(
        "Welcome to the Rock, Paper, Scissors game!\n"
        "Let's get started.\n"
        "In this game, you will be able to play Rock, Paper, Scissors, and also the Extended version: Lizard-Spock.\n"
        "The Extended version includes additional rules for Lizard and Spock, making the game even more exciting!\n"
        "If you want to play the extended version, make sure to check the rules. "
    )

    while True:
        check_rules = input("Do you want to see game rules? (y/n): ").strip().lower()
        try:
            if check_rules == "y":
                print(rules())
                break
            elif check_rules == "n":
                print("Alright! Everybody knows the rules. ")
                break
            else:
                raise ValueError("Invalid input. Please write 'y' or 'n'. ")
        except ValueError as e:
            print(e)


def get_game_preference():
    global game_counter
    computer_preference_list = [1, 0]
    computer_preference = random.choice(computer_preference_list)

    while True:
        if game_counter == 1:
            game_preference = input("Do you want to compete against computer? (y/n): ").strip().lower()
            try:
                if game_preference == "y":
                    game_version = input("Which version do you want to play? (classic/extended): ").strip().lower()
                    if game_version == "classic":
                        play_classic_game()
                    elif game_version == "extended":
                        play_extended_game()
                    else:
                        raise ValueError("Invalid choice. Please choose 'classic' or 'extended'.")
                    break
                elif game_preference == "n":
                    print("HUH! Did you scare or what ?")
                else:
                    raise ValueError("Invalid input. Please write 'y' or 'n'. ")
                break
            except ValueError as e:
                print(e)
        elif game_counter > 1 and computer_preference == 0:
            print("Well played! You've put up a good fight, but I'm starting to get tired. How about a break?")
            break
        elif game_counter > 1 and computer_preference == 1:
            game_preference = input("I would like to play more, but how about you? (y/n): ").strip().lower()
            try:
                if game_preference == "y":
                    game_version = input("Which version do you want to play? (classic/extended): ").strip().lower()
                    if game_version == "classic":
                        play_classic_game()
                    elif game_version == "extended":
                        play_extended_game()
                    else:
                        raise ValueError("Invalid choice. Please choose 'classic' or 'extended'.")
                    break
                elif game_preference == "n":
                    print("Ah, I see! I guess I'll just go and sharpen my circuits. Catch you later!")
                    break
                else:
                    raise ValueError("Invalid input. Please write 'y' or 'n'. ")
            except ValueError as e:
                print(e)


def play_classic_game():
    global game_counter
    player_score = 0
    computer_score = 0
    round_counter = 1

    moves = ["rock", "paper", "scissors"]
    possibilities = [["rock", "rock"], ["rock", "paper"], ["rock", "scissors"],
                     ["paper", "rock"], ["paper", "paper"], ["paper", "scissors"],
                     ["scissors", "rock"], ["scissors", "paper"], ["scissors", "scissors"]]
    score_chart = [0, -1, 1, 1, 0, -1, -1, 1, 0]

    print("Let's play! First to win 2 rounds, wins the game!")

    while True:

        computer_move = random.choice(moves)
        your_move = input("\nNow make your move! (rock/paper/scissors): ")
        try:
            if your_move not in moves:
                raise ValueError("\nInvalid move. Your possible moves are 'rock','paper' or 'scissors'.")
            else:
                print("Valid move!")
                made_moves = [your_move, computer_move]

                for i, mv in enumerate(possibilities):
                    if mv == made_moves:
                        print(f"Your move is {your_move}, computer's move is {computer_move}.")
                        if score_chart[i] == 1:
                            player_score += 1
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nYou have won the round. Score is {player_score} - {computer_score}")
                        elif score_chart[i] == -1:
                            computer_score += 1
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nComputer have won the round. Score is {player_score} - {computer_score}")
                        else:
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nRound is tie. Score is {player_score} - {computer_score}")
                        round_counter += 1
                        break
        except ValueError as e:
            print(e)

        # checking score
        if player_score == 2:
            print(f"Game number {game_counter} is over. You have won the game {player_score}-{computer_score}.\n")
            game_counter += 1
            get_game_preference()
            break

        elif computer_score == 2:
            print(f"Game number {game_counter} is over. Computer have won the game {player_score}-{computer_score}\n")
            game_counter += 1
            get_game_preference()
            break


def play_extended_game():
    global game_counter
    player_score = 0
    computer_score = 0
    round_counter = 1

    moves = ["rock", "paper", "scissors", "lizard", "spock"]
    possibilities = [
        ["rock", "rock"], ["rock", "paper"], ["rock", "scissors"], ["rock", "lizard"], ["rock", "spock"],
        ["paper", "rock"], ["paper", "paper"], ["paper", "scissors"], ["paper", "lizard"], ["paper", "spock"],
        ["scissors", "rock"], ["scissors", "paper"], ["scissors", "scissors"], ["scissors", "lizard"], ["scissors", "spock"],
        ["lizard", "rock"], ["lizard", "paper"], ["lizard", "scissors"], ["lizard", "lizard"], ["lizard", "spock"],
        ["spock", "rock"], ["spock", "paper"], ["spock", "scissors"], ["spock", "lizard"], ["spock", "spock"]
    ]
    score_chart = [
        0, -1, 1, 1, -1,
        1, 0, -1, -1, 1,
        -1, 1, 0, 1, -1,
        1, -1, -1, 0, 1,
        -1, 1, 1, -1, 0
    ]

    print("Let's play! First to win 2 rounds, wins the game!")

    while True:

        computer_move = random.choice(moves)
        your_move = input("\nNow make your move! (rock/paper/scissors/lizard/spock): ")
        try:
            if your_move not in moves:
                raise ValueError("\nInvalid move. Your possible moves are 'rock', 'paper', 'scissors', 'lizard' or 'spock'.")
            else:
                print("Valid move!")
                made_moves = [your_move, computer_move]

                for i, mv in enumerate(possibilities):
                    if mv == made_moves:
                        print(f"Your move is {your_move}, computer's move is {computer_move}.")
                        if score_chart[i] == 1:
                            player_score += 1
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nYou have won the round. Score is {player_score} - {computer_score}")
                        elif score_chart[i] == -1:
                            computer_score += 1
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nComputer have won the round. Score is {player_score} - {computer_score}")
                        else:
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nRound is tie. Score is {player_score} - {computer_score}")
                        round_counter += 1
                        break
        except ValueError as e:
            print(e)

        # checking score
        if player_score == 2:
            print(f"Game number {game_counter} is over. You have won the game {player_score}-{computer_score}.\n")
            game_counter += 1
            get_game_preference()
            break

        elif computer_score == 2:
            print(f"Game number {game_counter} is over. Computer have won the game {player_score}-{computer_score}\n")
            game_counter += 1
            get_game_preference()
            break


def tas_kagit_makas_BURAK_OZDEMIR():
    get_rules_preference()
    get_game_preference()


if __name__ == "__main__":
    tas_kagit_makas_BURAK_OZDEMIR()
