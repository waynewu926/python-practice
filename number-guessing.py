import random

top_of_range = input("Type a number as the maximal(it must larger than 0):\n")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.\n")
        quit()
else:
    print("Please type a number next time.\n")
    quit()

random_number = random.randint(0, top_of_range)
times = 0

while True:
    times += 1
    guess = input("guess a number:\n")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time.\n")
        continue

    if guess == random_number:
        print("You got it!\n")
        break
    elif guess >= random_number:
        print("You were above the number!\n")
    else:
        print("You were below the number!\n")

print(f"You take {times} times to get it!")
