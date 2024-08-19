import random
game_counter = 1


def rules():
    return """
            -> You will compete against computer.
            -> Each round win equals to 1 points.
            -> First to reach 2 points wins the game.
              ###### GAME RULES ######
            1. Rock wins against scissors.
            2. Scissors win against paper.
            3. Paper wins against rock.
            4. Otherwise, it is a tie!
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
    global game_counter
    computer_preference_list = [1, 0]
    computer_preference = random.choice(computer_preference_list)

    while True:

        if game_counter == 1:
            game_preference = input("Do you want to compete against computer ? (y/n): ").strip().lower()
            try:
                if game_preference == "y":
                    play_game()
                    break

                elif game_preference == "n":
                    print("HUH! Did you scare or what ?")
                    break

                else:
                    raise ValueError("Invalid input. Please write 'y' or 'n'. ")

            except ValueError as e:
                print(e)

        elif game_counter > 1 and computer_preference == 0:
            print("Well played! You've put up a good fight, but I'm starting to get tired. How about a break?")
            break

        elif game_counter > 1 and computer_preference == 1:
            game_preference = input("I would like to play more, but how about you ? (y/n): ").strip().lower()
            try:
                if game_preference == "y":
                    play_game()
                    break

                elif game_preference == "n":
                    print("Ah, I see! I guess I'll just go and sharpen my circuits. Catch you later!")
                    break

                else:
                    raise ValueError("Invalid input. Please write 'y' or 'n'. ")

            except ValueError as e:
                print(e)


def play_game():
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


def tas_kagit_makas_BURAK_OZDEMIR():
    get_rules_preference()
    get_game_preference()


if __name__ == "__main__":
    tas_kagit_makas_BURAK_OZDEMIR()