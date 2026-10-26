# string methods are built in functions that can be used to manipulate strings.
# types of string methods
# len() - its a function that returns the length of a string. it counts the 
# the letters and characters in a string. like for example,
# "well done" would be 9 because it also counts spaces.

# Example of len() function.

name = str(input("what is your fullname :"))
result = len(name)
print(f"The length of your fullname is: {result}")

# the find() method is a string method that returns the index of 
# the first occurrence of a substring in a string. 
# if the substring is not found, it returns -1.

name = str(input("what is your fullname :"))
result = name.find("O")
print(f"The index of the first occurrence of 'o' in your fullname is: {result}")

# to find the last occurence, you use rfind() method

name = str(input("what is your name :"))
character = input("what letter do you want to find :")
result = name.rfind(character)
print(f"the index of the last occurence of {character} in your fullname is: {result} ")

# # the capitalize() method is used to captilize the first letter in a string.
# # example
name = str(input("enter your name :"))
result = name.capitalize()
print(result)

# the upper() method is used to turn all the letters to capital letters.
name = input("name :")
result = name.upper()
print(result)

# the isdigit() method returns a boolean true or false, true if the string is fulling digit(number)
#  and false if there is no digit and if it is mixed with alphabets and digits(numbers), or spaces.
name = input("name :")
result = name.isdigit()
print(result)

# the isalpha() metod checks if the string is fully alphabet, it would return true, if it is mixed alpha, 
# digits or even space. it would bring false.

name = input("names:")
result = name.isalpha()
print(result)

# # the count() method counts a character in a string . for example if i say it should count a
# # it would count all the a in the string.
name = input("name :")
result = name.count("a")
print(result)

# the replace() method replaces a character with another character in a string . for example repace
# a with s.like change a to s.

phone_number = input("enter your phone number :")
result = phone_number.replace("", "-")
print(result)

# TO GET ALL THE METHODS JUST DO
# print(help(str))

# EXERCISE:

username = input("Enter your username :")

if  username.isalpha() is False :
    print("username should not contain spaces or digits.")

elif len(username) > 12:
    print("username should not be more than 12 characters")
else:
    print(f"Welcome. {username} is allowed")

