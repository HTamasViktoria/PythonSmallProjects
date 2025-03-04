import random

top_of_range = input("Type a number: ")

guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number greater than 0!")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randrange(1, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess! ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("You were under the number")

print("You got it in", guesses, "guesses")