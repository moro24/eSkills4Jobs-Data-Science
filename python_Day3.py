# ## generate seq of numbs b/n 1 and 10 
# for each_number in range(1, 10):
#     print("Each Number: <= ", each_number)

# ## generate seq of even numbs b/n 1 and 10 (inclusive)
# for each_number in range(2, 11, 2):
#     print("Each Number: <= ", each_number)

# ## generate seq of numbs b/n 1 and 10 
# for each_number in range(10, 1, -1):
#     print("Each Number: <= ", each_number)

# # group_of_items = 'Moro'
# class_reg = ['Nat', 'Jul', 'Oscar', 'Tah', 'Lyd']
# for each_item in class_reg:
#     print(each_item)


# user_name = input("Enter your name: ")
# number_times = int(input("Number of times"))
# for each_name in range(1, number_times + 1):
#     print("Your name is: ", user_name )

# user_name = input("Enter your name: ")
# user_number = int(input("Enter the number of times: "))

# if (user_number < 10):
#     for each_name in range(1, user_number + 1):
#         print(user_name)
# else:
#     for each_message in range(1, 4):
#         print("Too High!!!")

# again = "yes"
# # again = input("Enter yes or no")
# while (again == "yes"):
#     print("Hello")
#     ## loop control
#     again = input("Do you want to continue: ")
# print("Goodbye")

# total = 0
# while (total <= 10):
#     print("Counter => ", total)
#     print("Hello World")
#     total = total + 1
    
# print("Goodbye")

# print("CLASS ATTENDANCE REGISTER")
# attendance = input("Have you registered or not ?")
# while (attendance == 'no'):
#     username = input("Enter you name to register: ")
#     print("Confirm Name: ", username)

#     ## loop control 
#     attendance = input("Have you registered or not ?")

# 046
# Ask the user to enter a number. Keep asking until they enter a 
# value over 5 and then display the message 
# “The last number you entered was a [number]” and stop the program

user_input = 0
while (user_input < 5 ): 
    ## loop control 
    user_input = int(input("Enter a number: "))
print("The last number you entered was [", user_input , "]")
print(f"----------------------------------------------")
print(f"The last number you entered was [{user_input}]")