import random
def comp_game(user_input):
# Guess game for computer vs human
# Declaring var for int 1-15
    var= random.randint(1,15)
# print(var)
# Check computer number vs human input
    if user_input == var:
        print("You guessed", user_input, "Computer guessed", var)
    else:
        print("You guessed", user_input, "Computer guessed", var)
user_input= int(input ("Please provide your number "))
comp_game(user_input)