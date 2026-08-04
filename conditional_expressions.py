# conditional expressions are like one line shortcut for the if-else statement 
# it assigns one or two values based on a condition
# like return x if condition is met else return y
# formular
# x if condition else y

dress = "wet"
print("dress is dry" if dress == "dry" else "dress is not dry")

num = 12
print("even "if num % 2 == 0 else "odd")

# i want to drink water. i can only drink the water if there is bottle water 
# and if the water is cold . if it is not cold then i cant drink it.

print("welcome. would you like to drink water.")
response = str(input("Yes or No :"))
if response == "Yes":
    water = input("do you want cold or room temperature water :")
    type = input("bottle or sachet water :")
    if water == "cold" and not type == "bottle":
        print("have some water.")
    else: 
        print("we only have cold bottle water.")

elif response == "No" :
    print("we don't have any other thing but water")

else:
    print("Invalid syntax. pls choose between Yes or No")


# from this exampe. we see that not deals with boolean . 
# it can make the statement either true or false.

    
