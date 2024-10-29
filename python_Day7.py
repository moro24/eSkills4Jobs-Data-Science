# ## create an empty class register 
# class_reg = []

# reg_count =  int(input("Enter the number of students to register: "))
# ## 25 participants 

# for each_user in range(1, reg_count + 1):
#     ## ask for the users fullname 
#     user_input = input("Enter your fullname: ")

#     ## store the users name in the class register 
#     class_reg.append(user_input)

# ## display the class register 
# print(class_reg)

# timer = 0
# while (timer <= 30): 
#     ##do something 

#     timer = timer + 1

## function to take two inputs from a user 

## global 
def users_inputs():
    user_input1 = int(input("Enter your first number: "))
    user_input2 = int(input("Enter your second number: "))

    # return user_input1
    return user_input1, user_input2


## creating to add two numbers
def addition(num1, num2):
    
    result =  num1 + num2 
    return result 

# Computing a sales commission, given the sales amount
# and the commission rate.

def multiplication(num1, num2):
    pass 

def division(num1, num2):
    pass 

def substraction(num1, num2):
    pass

## performing addition 
num1, num2 = users_inputs()
add = addition(num1, num2)
print("The sum of adding two numbers: ", add)
print(f"The sum of adding two numbers: {add}")


# ## performing substraction 
# num1, num2 = users_inputs()
# sub = substraction(num1, num2)
# print("Subtracting  two numbers: ", sub)
# print(f"Subtracting two numbers: {sub}")