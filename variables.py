# variables
#type of variables

# strings
first_name = "Olamide"
print(f"my name is {first_name}.")

# integars

age = 19
print(f"I am {age} years old.")

# float

price = 350.85
print(f"I bought a bag of ${price}")

#boolean

bag = False

if bag is True:
    print("The bag is original.")

else:
    print("The bag is fake.")


# Typecasting is the act of changing a variable from one variable type to another variable type.
#    type of typecasting
# str() , bool(), int(), float()



# Examples

# str(), change my integer variable to a string variable.

date = 17

print(str(date))

# int()
sand = 13.55
print(int(sand))

#float()

sands = 13
print(float(sands))

# bool()
noun = "chair"
print(bool(noun))

# for this type of conversion which is str to bool, 
# it always says true as long as the string is not empty,
# if the string is empty, it says false.

print(bool(sands))

# for this type it would always say true except if you're use number 0.


print(bool(sand))