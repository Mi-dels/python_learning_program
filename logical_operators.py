# logical operators helps ua to evaluate multiple conditions and we can link them toghether. they are 
# or = at least one condition must be true. with or we can check more than one condition. if at least one condition is true, 
# 
# and = both conditions must be true
# not = inverts the condition (not false, not true)
# 
# so example of or
money = 400
mummy_is_not_around = False

if money <= 500 or mummy_is_not_around:
    print("go and buy")  
else:
    print("stay home")

# it would show go and buy because one condition is true which is the money is less than 500.
# if i change that false to true in t
# boolean mummy-is-not-around, the statement would be true.

# SO EXAMPE FOR AND
data = 1000
battery = "full"
if data >= 900 and battery == "full":
    print("go to class")
else:
    print("stay at home")

# it would show go to class because the both conditions are true.

# SO EXAMPLE FOR NOT
door_is_closed = False
if not door_is_closed :
    print("door is closed")
else:
    print("door is not closed")
    

