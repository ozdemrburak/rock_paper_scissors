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

        game = input("Do you want to compete against Mr.Computer ? (y/n): ").strip().lower()
        try:
            if game == "y":
                play_game()

            elif game == "n":
                print("Did you scare or what ? HUH!  ")
                break

            else:
                raise ValueError("Invalid input. Please write 'y' or 'n'. ")

        except ValueError as e:
            print(e)


def play_game():
    moves = ["rock", "paper", "scissors"]
    print("Let's play! First to win 2 rounds, wins the game!")
    while True:

        move = input("\nNow make your move! (rock/paper/scissors): ")
        try:
            if move not in moves:
                raise ValueError("Invalid move. Your possible moves are 'rock','paper' or 'scissors'.")
            else:
                print("Valid move!")
                break

        except ValueError as e:
            print(e)


def tas_kagit_makas_BURAK_OZDEMIR():
    get_rules_preference()
    get_game_preference()


# print(rules())
print(tas_kagit_makas_BURAK_OZDEMIR())
