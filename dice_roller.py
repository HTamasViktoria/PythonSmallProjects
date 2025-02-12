import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Number of players must be between 1 and 4")
    else: 
        print("Invalid number of players, try again!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for i in range(players):
        print("Player ", i+1, "'s turn \n")
        print("Your total score is: ", player_scores[i], "\n")
        current_score = 0

        while True: 
            should_roll = input("Would you like to roll? (y): ").lower()

            if should_roll == "y":
                value = roll()
                if value == 1:
                    print("You rolled a 1! Turn done")
                    current_score = 0
                    break
                else: 
                    print("You rolled:", value)
                    current_score += value
                    print("Your current score is:", current_score)
            else:
                break

        player_scores[i] += current_score
        print("Your total score is:", player_scores[i])

max_score = max(player_scores)
winning_index = player_scores.index(max_score)
print("Player ", winning_index+1, "won")
