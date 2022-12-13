import random

def play_game():
    # Prompt the user to choose rock, paper, or scissors
    user_choice = input("Please choose rock, paper, or scissors: ")


       # Check if the user's choice is valid
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Sorry, that is not a valid choice. Please try again.")
        user_choice = input("Please choose rock, paper, or scissors: ")

    # Generate a random choice for the computer
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("The computer chose: {}".format(computer_choice))

    # Compare the choices and determine the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        return "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
    else:
        return "The computer wins."


# Play the game three times
wins = 0
losses = 0

for i in range(3):
    result = play_game()
    if "win" in result.lower():
        wins += 1
    elif "tie" in result.lower():
        pass
    else:
        losses += 1

# Print the final score
print("You won {} games and lost {} games.".format(wins, losses))
tie_games = 3 - wins - losses
if tie_games > 0:
    print("There were {} tie games.".format(tie_games))

# Determine the overall winner
if wins > losses:
    print("Congratulations, you are the overall winner!")
elif wins == losses:
    print("It's a tie for the overall game!")
else:
    print("Sorry, the computer is the overall winner.")
