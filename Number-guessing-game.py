
import random

def start_game():
    print("------------------------------------------")
    print(" Welcome to the Number Guessing game!")
    print("------------------------------------------")
    
    random_number = random.randrange(1, 11)
    total_attempts = 0
    while True:
        try:
            player_number = int(input("Pick a number between 1 to 10: "))
            if player_number not in range(1,11):
                print("Please enter the number between 1 to 10")
            elif player_number > random_number:
                print("it is lower")
                total_attempts += 1
            elif random_number > player_number:
                print("it is higher")
                total_attempts += 1
            else:
                print("You got it! It took you {} tries".format(total_attempts))
                answer = input("Do you want to play again? (Yes/No) ").lower()
                if answer == "yes" or answer == "y" :
                    start_game()
                else:
                    print("Thanks for playing..")
                    exit()
        except ValueError:
            print("Invalid Input")

start_game()