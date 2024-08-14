import random


def rules():
    return """
            -> You will compete against computer.
            -> Each round win equals to 1 points.
            -> First to reach 2 points wins the game.

              ###### GAME RULES ######
            1. Rock wins against scissors.
            2. Scissors win against paper.
            3. Paper wins against rock.
            4. Otherways It is a tie !
            """


def get_rules_preference():
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
    while True:

        game = input("Do you want to compete against computer ? (y/n): ").strip().lower()
        try:
            if game == "y":
                play_game()
                break

            elif game == "n":
                print("HUH! Did you scare or what ?")
                break

            else:
                raise ValueError("Invalid input. Please write 'y' or 'n'. ")

        except ValueError as e:
            print(e)


def play_game():
    player_score = 0
    computer_score = 0
    round_counter = 1
    game_counter = 1
    moves = ["rock", "paper", "scissors"]
    possibilities = [["rock", "rock"], ["rock", "paper"], ["rock", "scissors"],
                     ["paper", "rock"], ["paper", "paper"], ["paper", "scissors"],
                     ["scissors", "rock"], ["scissors", "paper"], ["scissors", "scissors"]]
    score_chart = [0, -1, 1, 1, 0, -1, -1, 1, 0]

    print("Let's play! First to win 2 rounds, wins the game!")

    while True:

        computer_move = random.choice(moves)
        move = input("\nNow make your move! (rock/paper/scissors): ")
        try:
            if move not in moves:
                raise ValueError("\nInvalid move. Your possible moves are 'rock','paper' or 'scissors'.")
            else:
                print("Valid move!")
                maked_moves = [move, computer_move]

                # main algorithm is here
                for i, r in enumerate(possibilities):
                    if r == maked_moves:
                        print(f"Your move is {move}, computer's move is {computer_move}.")
                        if score_chart[i] == 1:
                            player_score += 1
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nYou have won the round. Score is {player_score} - {computer_score}")
                            round_counter += 1

                        elif score_chart[i] == -1:
                            computer_score += 1
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nComputer have won the round. Score is {player_score} - {computer_score}")
                            round_counter += 1

                        else:
                            print(f"##### Round Number: {round_counter} | Game Number: {game_counter} #####"
                                  f"\nRound is tie. Score is {player_score} - {computer_score}")
                            round_counter += 1

        except ValueError as e:
            print(e)

        # checking score
        if player_score == 2:

            print(f"{game_counter}game is over. You have won the game {player_score} - {computer_score}.\n")
            game_counter += 1
            #get_game_preference()
            break

        elif computer_score == 2:

            print(f"{game_counter}game is over. Mr.Computer have won the game {player_score} - {computer_score}\n")
            game_counter += 1
            #get_game_preference()
            break


def tas_kagit_makas_BURAK_OZDEMIR():
    get_rules_preference()
    get_game_preference()


print(tas_kagit_makas_BURAK_OZDEMIR())
