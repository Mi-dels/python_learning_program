# # input function in python 
# # The input function is a function that prompts the user to enter a data and it returns
# # the data as a string
# #   Example

# input("what is your name? : ")

# # when writing an input function. you put a prompt to help the user understand what to write . 
# # Then a colon (:) must follow and a space. the prompt should be in quotes ("").
# # For now we can see get the data return to us because we did not save it .
# # to do so, you assign it to a variable. like this.
# #   Example

# name = input("what is your name? : ")
# print(name)

# # We can also use an f string to send a message with that answer we saved. Remem

# print(f"Hello {name}")

# # Let us try again. and this time add typecasting 
# # remember to add an int to a string . you need to type cast that string to an int
# age = input("How old are you? : ") # this would come out as a string remember.
# # to add one to the age outcome . we need to make the age give us back an int usig typecasting.

# age = int(age) # age becomes an integar or int. now lets add
# age = age + 1

# print(f"You are {age} years old.")

# # you know you can also typecast immediately on the input function and add the + 1 and,
# # it would still give the same result.

# ages = int(input("what is your age? : ")) + 1

# print(ages)

# # lets do a small exercise. lets calculate a rectangle area using input function,
# # typecasting and multiplication and assiging variables.

# #  Excercise 1

# length = float(input("Enter value of the length : "))# i used float because float accepts decimal and,
# # this calaculation may lead to decimal. so to have a correct answer at all times, you use float to accomo
# #date decimal answers.
# width = float(input("Enter value of the width : "))
# area = width * length
# print(f" The area is {area}cm². ")

# #   Exercise 2

# # lets do a shopping cart program.

# item = input("what tem would you like to buy : ")
# price = float(input("what is the price : "))
# quantity = int(input(f"how many quantity of the {item} would you like to buy : "))

# total = price * quantity
# print(total)
# #32.45

#MADLIBS WORD GAME
adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place or thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter a verb ending with ing: ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit, i saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}")