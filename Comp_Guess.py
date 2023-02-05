# Guess two numbers against a computer's guess
import random
# Define function for computer's guess
def comp_guess(user_data):
    var= random.randint(1,10)
    while user_data != var:
        user_data= int(input("Please enter guess number "))
    if user_data == var:
        print("User number is ", user_data, "Computer guessed", var)
    else:
        print("User number is ", user_data)
# Collect data from user
user_data= int(input("Please enter guess number "))
# Close argument
comp_guess(user_data)



