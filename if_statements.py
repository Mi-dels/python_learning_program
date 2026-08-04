# # if statememnts is used if some conditions are true or if not true you use else
# # e.g if it's 5.00 the alarm should ring if not don't ring.
# #also elif is included if you have different conditions to work on. elif is always before else. 
# # else is always the last. if the if statement is false. it moves to the elif, if the elif is false ,
# # it moves to the else. you can add as many elif statements
# # EXAMPLE
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are accepted.")

# elif age <= 0:
#     print("Not acceptable.")
# else:
#     print("Only accept thoose who are 18 and above")

# # another example
# # == is for comparison while = is for aasignment.
# # upper is used to make all letters capital letters.

# response = str(input("Would you like to eat (Y/N): "))

# if response.upper() == "Y":
#     print("Have some food.")
# else:
#     print("Okay. Have a nice day.")


# the use of boolean with if statements.
#still coming back to this.
# example
for_rent = False

if for_rent:
    print("This item is NOT for rent")
else:
    print("this item is for rent")

#1:06:02
# EXERCISE
#python calculator 
num_1 = int(input("input the first number: "))   
num_2 = int(input("input the second number: "))
math = input("input the type of calculation you want done e.g /,+,- :")

if math == "+":
    result = num_1 + num_2
    print(result)
elif math == "-":
    result = num_1 - num_2
    print(result)
elif math == "/":
    result = num_1 / num_2
    print(result)
elif math == "*":
    result = num_1 * num_2
    print(result)


#python weight converter


    