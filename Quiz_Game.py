print("Welcome to the quiz game!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()


print("Okay, let's play :)")

score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else: 
    print("Incorrect")



answer = input("What does GPU stand for? ")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else: 
    print("Incorrect")



answer = input("What does RAM stand for? ")

if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else: 
    print("Incorrect")



answer = input("What does PSU stand for? ")

if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else: 
    print("Incorrect")

print("You got ", score, "correct answers")
print("You reached ", int(score/4*100), "%")