'''
Import Syntax
'''

# import test

# eliminates the needs for dot syntax
from test import fav_foods

# import entrie file, use dot syntax (filename.datastructure) - test.fav_foods
#range len controls the indencies - dont have to deal with that later

# for i in range(len(fav_foods)):
#   print(fav_foods)
# ''''''

# for food in fav_foods:
#   print("I love " + food)
# ''''''

'''
Rules
'''

# Consider these inputs and their corresponding output
# 2 => 5
# 5 => 26
# 10 => 101

# the rule is: x^2 + 1

# What will the output be based on these inputs?
# 1 => 2
# 3 => 10
# 8 => 65

# Consider these inputs and their corresponding output
# "Balloon" => True
# "Globe" => False
# "Elephant" => False
# "Sheep" => True 

# The rule: 2 of the same letter consecutively?
# does the pattern of the output repeat?

# What will be the output based on these inputs?
# "Green" => T
# "Rainbow" => F
# "Cheddar" => F/T
# "Excelsior" => F

'''
Functions
'''

# DEFINE a function
# def: definition of the function (begins the function)

# def function_name(parameters, separated, by, commas):
#   internal_code
#   return return_value

# output = function_call(arguments, separated, by, commas)

# Difference between storing & printing

# def print_shout(name):
#   name = name.upper()
#   print("HELLO " + name + "!")

# print_shout("Chan")

# (demo function that prints directly as well)

# What's the outcome of this code?

# def shout(name):
#   # .upper - upper case
#   name = name.upper()
#   return "HELLO " + name + "!"
# ''''''

# # to "call" a function is to use it 
# output = shout("Marin")
# print(output)

# # function call inside print statement 
# print(shout("Karen"))

# # Challenge: write a function that returns the square of the input + 1

# # my solution
# def square_one(num):
#   num = (num**2)+1
#   return num
# ''''''
# new_num = square_one(8)
# print(new_num)

# # Amina's solution - user input + dont need a parameter cuz get it from user
# def square_num():
#   a = input("choose your number: ")
#   x = int(a)
#   return x**2 +1
# ''''''
# print(square_num())

# # single line solution
# def square(x):
#   return x**2 + 1
# ''''''
# print(square(5))

# we've used functions before - built in functions like len --> https://www.w3schools.com/python/python_ref_functions.asp 


# Multiple parameters
def personalized_age_check(name, age):
  if age >= 25:
    return "Congratulations " + name + "! You're old enough to vote and rent a car."
  elif age >= 18:
    rent_time_left = 25 - age
    return "Sorry, " + name + ", you can only vote, but to rent a car, you need to wait " + str(rent_time_left) + " more years."
  else:
    rent_time_left_2 = 25 - age
    vote_time_left = 18 - age
    return "Sorry, " + name + ". You can't vote for " + str(vote_time_left) + " more years. You can't rent a car for another " + str(rent_time_left_2) + " years."

# # Call the function - parameters in same place
print(personalized_age_check("Jeff", 28))
print(personalized_age_check("Chuck", 21))
print(personalized_age_check("Zara", 14))

# CHALLENGE
# Edit this function to add a condition for being 25 or older—you can rent a car at this age!

# if you're 25+: tell us you can rent a car & vote
# 18 <= age < 25: you can vote, you can't rent a car
# else you can't do either

# STRETCH: write a function that returns the square of the input + 1

# def square_plus_one(num):
#   return num**2 + 1

# print(square_plus_one(4))














# DEFAULT ARGUMENTS

# def greet_player(name = "User"):
#   print("Welcome to the game, " + name + ".")
#   print("Your current level is 1.")

# # greet_player("David") # Code if the user provides their name
# # greet_player()  # Code if the user chooses not to provide their name

# # example with default parameters for range functions
# # for i in range(stop = 4, step = 2):
# #   print(i)

# def greet_player_2(name, high_score):
#   print("Welcome to the game, " + name + ".")
#   print("Your current high score is " + str(high_score))

# # calling functions explicitly using parameter names
# greet_player_2(high_score = 100, name = "Suraj")


# # SCOPE 
# # this is one reference to age
# age = 15

# # NOTE: it is generally bad practice to have same name variables across multiple scores
# def have_a_birthday():
#   # this reference to age is basically a different variable
#   # (different memory space)
#   # even though it has the same name, it behaves independently
#   age = 20
#   age += 1
#   print("Happy birthday! You're now " + str(age))
#   # because we are inside the function, age here is 21!
#   return age


# have_a_birthday()

# # outside of the function, there's only the first age!
# # so this will print 15
# print(age)












# LONGER CHALLENGE:
# Make a function that makes a new user for a social media app:
# 1. Take in name and email.
# 2. Create a DEFAULT password
# 3. Store all the information in a dictionary
# 4. Have the function RETURN a statement based on the dictionary:
# "Hi, username! We contacted you at email."



# def profile(name, email, password = "upperline2022!"):
#   user = {}
#   user["name"] = name
#   user["email"] = email
#   user["password"] = password

#   return "Hi " + user["name"] + "! We contacted you at " + user["email"] + ". Your password is currently " + user["password"]

# print(profile("suraj", "abc123@gmail.com"))



# A FINAL EXAMPLE
# def greet(player):
#   if player == "Octavia":
#     return "Welcome, agent Spencer. We're big fans."
#   else:
#     return "Welcome, " + player

# # Use a variable to collect and store user input
# name1 = input("Enter player 1's name") 

# # Pass in our `name1` variable as the argument for our greet function.
# print(greet(name1)) 

# name2 = input("Enter player 2's name")
# print(greet(name2))

# what's the output?
# def add(x, y):
#   total = x + y

# print(add(5, 22))
