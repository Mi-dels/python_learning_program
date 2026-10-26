# # indexing allows us to access elements of a sequence using this bracket "[]". it is somehow like arrays but
# # this time for strings. it follows this formula [start:end:step]
# # EXAMPLE
# credit_number = "1234-5678-9012-3456"
# print(credit_number[1])
# # it would give me the number 2 because all index start with 0. calling one index would mean, you
# # are calling the start. if i wnt the first 4 digits of that number. i would call the start then 
# # the end of where i want 
# print(credit_number[0:4])
# # this would give me the first four digits, starting with index 0 because i am starting from the begining,
# # then the 4 means the end , though the index 4 is not going to show because it is exclusive
# # so if i had wanted 5, it would be 0:5 but also the index 5 would not show. but the starting index would be
# # the index of where you want to start counting, like for example, i need the next set of digits 5678.
# # i would check for the index which would be index 5 in this case , index 5 would be my starting index[5:]
# # while index 9 would be my ending index because i need to add one index that would be excluded but it is 
# # still needed. so it would be [5:9].

# # now if i do this [:4]. it means print from the beginning to index 4, because assume the empty index to be 
# # the first index which is 0. then if i do this [5:], it means from index 5 , print to the ending.
# # python assumes that to mean the end, because remember the formula is [start:end]. as far as it is two even 
# # if one is not specified the formula means start or end, so it start from the first index or end
# # at the last index 

# # if you need the last index of the string you could use [-1]. negative start counting from the back of 
# # the string
# print(credit_number[-2])

# # so for step, we can access the characters of a string by a given step, we can count by two or three.
# # Example
# print(credit_number[::2])
# # now we can leave the start and end blank and we know python would assume it to be the start of the string
# # and the end of the sring. now the two means it would count by two. for example ,let us say it is 
# # 123456, the two means , it would be 135. it would skip the 246, the same goes for [::4]or 5  or 6

# # Example
# # find the last four digits of the credit card.
# last_digits = credit_number[-4:]
# print(f"xxxx-xxxx-xxxx-{last_digits}")
# # i used -4 because negative index counts from the end of the strings. so -4 just means the last 4 digits 
# # or character of the string. to reverse a string set the step to -1. example
# print(credit_number[::-1])

#  Exercise
print("Welcome to Dcut. please sign in to make your orders.")
username = input("Username:")



if username.isalpha() == True :
    print(f" Username {username} has been accepted.")
    password = input("Password :")
    if password.isalpha() == False:
        if password.find(" ") == -1:
            print("Password has been accepted.")
            phone_number = input("Phone Number :")
            if phone_number.isdigit() == True:
               print("Phone Number is saved.")
            else:
                print("Phone Number should be all digits.")
    else:
        print("Password should have letters and digits but no space.")


else: 
    print(f"Username {username} is not accepted. Username should only contain letters.")
    print("refresh the page and start again")

print("You can now be paid for your orders.")
credit_number = input("Enter your bank account number to be paid.:")
answer = input(f"Is this your bank account number last digits {credit_number[-4:]} :")
if answer == "yes":
    print("Thank you , your payments would be made.")
else:
    print("pls rewrite your bank account number")

