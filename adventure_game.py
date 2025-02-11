name = input("What's your name? ")
print("Welcome ", name, "to this adventure!")

answer = input("You are on a dirty road, it come to an end, and you can go left or right. Which direction do you choose? ").lower()

if answer == "left":
    answer = input("You reached a bridge, you can cross it or walk around it. For crossing, type cross, for walking around, type walk! ").lower()
    if answer == "walk":
        print("It took too much time, you lost!")
    if answer == "cross":
        print("The bridge was a complete wreck, and you fell to the river. You lost!")
    else: 
        print("Not a valid option.")
elif answer == "right":
    answer = input("You find some fruit-like plant. Do you taste it or not? Type yes or no: ").lower()
    if answer == "yes":
        print("The fruit was poisonous, you lost! ")
    if answer == "no":
        print("Smart decision,", name,  ", the fruit was poisonous. You won!")
    else:
        print("Not a valid option, you lost!")
else :
    print("Not a valid option, you lost!")