# print("My first python program")

# x=100
# # print(x)

# num_of_cats = 198
# num_of_cats = num_of_cats - 1
#  print(num_of_cats)

# friends = num_of_cats
# # print(friends)

# # print(friends/5)

# is_active=True
# # print(is_active)

# Name = "Daisy"
# age = 30
# child = None 
# # print(child)
# # print(Name)

# my_other_str="a hat"
# #print(my_other_str)

# new_line = "hello \nworld"
# #print(new_line)

# new_str = "Hello\\World"
# #print(new_str)

# quotation = "my cat said \"meow\""
# #print(quotation)

# mountains = "/\\/\\/\\"
# #print(mountains)

# message = "Hello \n World"
# #print(message)

# str_one="your"
# str_two="face"
# str_three= str_one + " " + str_two
# #print(str_three)

# username = "Blue"
# #print("Hello there, " + username)

# name = "a" + "b" + "z"
# #print(name)

# st_one = "ice"
# st_one += " cream"
# #print(st_one)

# x = 10 
# formatted = f"I've told you {x} times"
# #print(formatted)


# answer = "yes"
# #print(answer)

# decimal = 12.56348734934
# integer = int(decimal)
# #print(integer)

# num = 12
# num = float(num)

# str(8)
# #print(str)

# int = "I am just a number"
# #print(int)

# print("How many kilometers did you cycle today?")
# kms = input()
# miles = float(kms)/1.60934
# miles = round(miles,2)
# print(f"Your {kms}km ride is {miles}mi ")

# name = "Bob"

# if name == "Arya Stark":
#     print("Valar Morghulis")
# elif name == "Jon Snow":
#     print("you know nothing")
# elif name == "Bob":
#     print("you know nothing")
# else:
#     print("Carry On")

# x =  1 
# print("yay")
# x is 1 
# elif x = "2":

# animal = input("enter your favourite animal")

# if animal:
#     print (animal + " is my favourite animal to")
# else: 
#     print("you didn't say anything")

# city = input("where do you live?")

# if city == "los angeles" or city == "san francisco":
#     print("You live in Cali")
# else:
#     print("You live elsewhere")

# age = 30
# #2-8 2$ ticket 
# #65 5$ ticket 
# #other 10$ ticket 
# if not ((age >= 2 and age <=8) or age >= 65):
#     print ("you pay 10 dollars")
# else:
#     print("you are a child or senior")

# age = input("How old are you:")
# if age != "":
#     age = int(age)
#     if age >= 18 and age < 21: 
#         print("You can enter but need a wrist band")
#     elif age >= 21:
#         print("You are good to come in and drink")
#     else: 
#         print("You can't come in, little one! :(")
# else:
#     print("enter an age")

# for number in range(1,8):
#     print(number)
#     print(number * number)

# for letter in "coffee":
#     print(letter)

# times = input("How many times do I gave to tell you? ")
# times = int(times)

# for time in range(times):
#     print(f"time {time+1}:Clean up your room!")

# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# num = 1 
# while num < 11: 
#     print(num)
#     num +=2

# for num in range(0,11):
#     count = 1
#     smileys = ""
#     while count <= num:
#         smileys += "b"
#         count += 1
#         print("b" * num)

# msg = input("Say somethig: ")

# while msg != "stop copying me": 
#     print(msg)
# while True:
#     command = input("Type 'exit' to exit:")
#     if (command == "exit" ):
#         break
# times = int(input("How many times do I have to tell you "))
# for time in range(times):
#     print("Clean up your room")
#     if time >= 4:
#         print("do you even listen anymore")
#         break


# import random  # use randint(a, b) to generate a random number between a and b
# number = 0 # store random number in here, each time through
# i = 0  # i should be incremented by one each iteration

# while number != 5:
#     i += 1 
#     number= randint(1, 10)

# import random 

# random_number = random.randint(1,10)
# guess = None 

# while guess != random_number:
#     guess = input("pick a number from 1 to 10: ")
#     guess = int(guess)
#     if guess < random_number:
#         print ("Too low!")
#     elif guess > random_number:
#         print("Too High!")
#     else:
#         print("You Won!")
# print(random_number)

# colors = ["yellow", "blue", "red"]
# for color in colors:
#     print(color)

# colors = ["yellow", "blue", "red"]
# index = 0 
# while index < len(colors):
#     print(f"{index}:{colors[index]}")
#     index += 1

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s
# result = result.upper()

# data = [1, 2, 3]
# data.append("purple")
# print (data)

# numbers = [5,6,7,8,9,10]

# numbers.index(6) 
# numbers.index(9)
# print (numbers)

instructors = [""]
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
x="instructors".join("Colt" "Blue" "Lisa")
print(x)