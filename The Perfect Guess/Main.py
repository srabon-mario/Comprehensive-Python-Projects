#THIS GAME INCLUDE MULTIPLE PLAYERS.

import random

def playGames():

    # Level selection
    print("Select the mode difficulty :")
    print("1.Easy(1-50)")
    print("2.Medium(1-100)")
    print("3.Hard(1-500)\n")

    choice = int(input("Enter the mode(1/2/3):"))

    if choice == 1:
        upper = 50
    elif choice == 2:
        upper = 100
    elif choice == 3:
        upper = 500
    else:
        print("Wrong Choice!")
        return

    name1 = input("\nName of player 1 : ")
    name2 = input("Name of player 2 : ")

    # PLAYER 1
    print(f"\nPlayer {name1} is playing Now ---\n")

    n1 = random.randint(1, upper)
    a = -1
    guesses1 = 0

    while a != n1:
        try:
            if guesses1 == 0:
                a = int(input(f"Hey {name1}, guess a number between 1 and {upper}: "))
            else:
                a = int(input("Guess again: "))

            guesses1 += 1

            if a > n1:
                print("<<Lower number please>>")
            elif a < n1:
                print("<<Higher number please>>")

        except ValueError:
            print(f"Hey {name1}, wrong input!")
            continue

    print(f"{name1}, you guessed the number in {guesses1} attempts.")

    # PLAYER 2
    print(f"\nPlayer {name2} is playing Now ---\n")

    n2 = random.randint(1, upper)
    a = -1
    guesses2 = 0

    while a != n2:
        try:
            if guesses2 == 0:
                a = int(input(f"Hey {name2}, guess a number between 1 and {upper}: "))
            else:
                a = int(input("Guess again: "))

            guesses2 += 1

            if a > n2:
                print("<<Lower number please>>")
            elif a < n2:
                print("<<Higher number please>>")

        except ValueError:
            print(f"Hey {name2}, wrong input!")
            continue

    print(f"{name2}, you guessed the number in {guesses2} attempts.")

    # SCOREBOARD
    print("\nSCOREBOARD ---")
    print(f"{name1} guessed number {n1} in {guesses1} attempts.")
    print(f"{name2} guessed number {n2} in {guesses2} attempts.\n")

    if guesses1 > guesses2:
        print(f"Congratulations {name2}, you win!")
    elif guesses1 == guesses2:
        print("Match Draw!")
    else:
        print(f"Congratulations {name1}, you win!")

playGames()
