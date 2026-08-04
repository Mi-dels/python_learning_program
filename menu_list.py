def rice():
    print("1. Jellof rice")
    print("2. Fried rice")
    print("3. White rice and Stew")
    print("4. Coconut rice")
    
    choose = input("What type of rice would you like.: ")
    if choose == "1":
        choose = "Jellof Rice"
        print(f"{choose} has been added to your order list.")
    
    elif choose == "2":
        choose = "Fried Rice"
        print(f"{choose} has been added to your order list.")

    elif choose == "3":
        choose = "White Rice and Stew"
        print(f"{choose} has been added to your order list.")

    elif choose == "4":
        choose = "coconut Rice"
        print(f"{choose} has been added to your order list.")

    else:
        print("Invalid number. pls try again")
    

def spaghetti():
    print("1. Jellof Sphagetti")
    print("2. White Spaghetti and Stew")
    
    
    choose = input("What type of Spaghetti would you like.: ")
    if choose == "1":
        choose = "Jellof Spaghetti"
        print(f"{choose} has been added to your order list.")
    
    elif choose == "2":
        choose = "White Spaghetti and Stew"
        print(f"{choose} has been added to your order list.")

    else:
        print("Invalid number. pls try again")

def swallow():
    print("1. Semo")
    print("2. Fufu")
    print("3. Amala")
    print("4. Pounded Yam")
    print("5. Eba")
    
    choose = input("What type of swallow would you like.: ")
    if choose == "1":
        choose = "Semo"
        print(f"{choose} has been added to your order list.")
    
    elif choose == "2":
        choose = "Fufu"
        print(f"{choose} has been added to your order list.")

    elif choose == "3":
        choose = "Amala"
        print(f"{choose} has been added to your order list.")

    elif choose == "4":
        choose = "Pounded Yam"
        print(f"{choose} has been added to your order list.")

    elif choose == "5":
        choose = "Eba"
        print(f"{choose} has been added to your order list.")

    else:
        print("Invalid number. pls try again")
  
    
def soups():
    print("1. Egusi Soup")
    print("2. Afang Soup ")
    print("3. Amala")
    print("4. Pounded Yam")
    print("5. Eba")
    
    choose = input("What type of swallow would you like.: ")
    if choose == "1":
        choose = "Semo"
        print(f"{choose} has been added to your order list.")
    
    elif choose == "2":
        choose = "Fufu"
        print(f"{choose} has been added to your order list.")

    elif choose == "3":
        choose = "Amala"
        print(f"{choose} has been added to your order list.")

    elif choose == "4":
        choose = "Pounded Yam"
        print(f"{choose} has been added to your order list.")

    elif choose == "5":
        choose = "Eba"
        print(f"{choose} has been added to your order list.")

    else:
        print("Invalid number. pls try again")
     




print("Welcome To Mide's Resturant")
print("Take a look at our menu list and make your order.")
print("1. Rice")
print("2. Spaghetti")
print("3. Swallow")
print("4. Soups")
print("5. Pepper Soup")

choice = input("what would you like to order?: ")

if choice == "1":
    rice()
elif choice == "2":
    pass
elif choice == "3":
    pass
elif choice == "4":
    pass
elif choice == "5":
    pass
else:
    print("Goodbye. Thanks for stopping by.")
