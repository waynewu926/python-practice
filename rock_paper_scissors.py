import random

user_wins = 0
computer_wins = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:\n").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer pick {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("You won!")
    elif user_input == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("You won!")
    elif user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("You won!")
    else:
        computer_wins += 1
        print("You lose!")


print(f"You win {user_wins} times")
print(f"Computer win {computer_wins} times")
print("Goodbye!")
