# ask someone for their name and age
# print out the following sentence 5 times:
# Your name is <name>, and you are <age> years old.

#old work
# x = 0
# food = input("What type of food do you like to eat? ")
# while x < 5:
#     print(food) #x-0, prints food
#     x = x + 1 

# def user(name, age):
#   i = 0
#   while i < 5:
#     print("Your name is ", name, "You are ", age, "years old")
#     i += 1
# name = input("What is your name ")
# age = input("What is your age ")
# user(name, age)

# Rewrite the function to print the user’s favorite food 5 times by decrementing the variable rather than incrementing.
#for num in range(0,11):
	#print(num)
	#num -= 1
#num=10
#call function

#to print from 11 - 0,
# def user(num):
# 	while num >= 0: #while 10 is greaterthan or equal to 0
# 		print(num)
# 		num -= 1 #reduce value of num(10) by 1
# num = 10
# user(num)

# def user(num):
#   for num in range (0,11):
#     print(num)
#     num -= 1
# num = 11
# user(num)

# a countdown from 15 to 5

#

#Dictionaries
new_dictionary = {
	"name": "Simpsons",
	"genre": "comedy",
	"interesting": "yes"
}
# movie_name = new_dictionary["name"]

# # fruit_list = ["apples", "oranges", "kiwi", "pineapple"]
# # #Print out the fruit at index 1
# # print(fruit_list[1])

# movie_genre = new_dictionary["genre"]

# #the name of the movie is <Simpsons> and it is a <comedy>.
# print("the name of the movie is", movie_name, "and it is a", movie_genre)

#print only the values, keys
# only_values = new_dictionary.values()
# only_keys = new_dictionary.keys()
# get_key_and_value = new_dictionary.items()
# new_dictionary["date"] = 1980
# print(only_keys)
# print(only_values)
# print(get_key_and_value)
# print(new_dictionary)

# for keys, only_values in new_dictionary.items():
# #   print(keys,only_values)

# #try, except block
# try:
# 	print(10/0)#unnamed_variable)
# except NameError:
# 	print("define your variables")
# except:
# 	print("something else is wrong")


#Create a calculator with basic operators

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")