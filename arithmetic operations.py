 # we are going to look at arirthmetic operations in python.
# addition
# we use the plus sign (+) to add numbers.

friends = 5
# to add a new person to the friends variable. you do it this way 
friends = friends + 1
# you can also shorthen this line of code like this 
friends += 1 # this would do the same thing.
#this (+=) is known as an argumentative assignment program

#SUBTRACTION

friends = friends - 1
friends -= 1

# MULTIPLICATION

friends = friends * 2
friends *= 2

#DIVISION
# division is a float by nature. so when you use a division sign, the numbers become a float

friends = friends / 2
friends /= 2

#EXPONATE (RAISE POWER OR POWER OF )

friends = friends ** 2
friends **= 2

#MAJULUS (IT'S THE REMAINDER OF ANYTHING DIVIDED)
#so we would create another variable to store the remainder
# we used the majulus to determine if the number is odd or even
# because it would divide by two without any remainder if the number is even
remainder = friends % 3

print(remainder)

print(friends)

x = 3.14
y = 4
z = 5

# there is a built-in round function that can round decimal numbers
result = round(x)
# there is also an abs (absolute value). it helps to find the absolute value of a number. 
#the absolute value is the distant of a number from 0
#lets say
w = -5
results = abs(w)
print(results)

#there is a built-in power function(like raise power to). you would need two numbers when using it.
# like 2 raise power 3 = 2*2*2 = 8
r = 2
e = 3
ans = pow(r, e)
print(ans)

# there is a max (maximum) functon. it helps to find the maximum(highest) value of numbers.
maxy = max(x, y, z)
print(maxy)
# there is also min(minimum) function. finds the (lowest) value
mini = min(x, y, z)
print(mini)



# to also get more functions, you need to import math like this

#then if you need something. for example pi.you just do this
print(math.pi)
#you can also do math.e , if you ever work with physics
print(math.e)
#if you need the square root of a function, you just do this.
t = 25
square = math.sqrt(t)
print(square)
#there is a ceil function. ceil would always round a number up.
# like 9.1 would be 10
f = 9.1
seil = math.ceil(f)
print(seil)
#then a floor function that would always round a number down.
g = 9.8
flour = math.floor(g)
print(flour)

# EXCERCISES
# calculate the circumference of a circle.
# formula = 2₶r

r = float(input("Enter the radius for the circle (numbers only): "))
circumference = 2 * math.pi * r
print(f"The circumference of the circle is : {round(circumference)}cm")

# calculate the area of a circle
#formula = a = ₶r²

radius = float(input("Enter the radius of the circle (numbers only): ")) ** 2

area = math.pi * radius
print(round(area, 2))

# another way this could be done

radiuses = float(input("Enter the  radius: "))
areas = math.pi * pow(radiuses, 2)

print(round(areas))

# calculate the hypotesis of a right triangle
# formula = c = ⩗a² + b²
import math
a = float(input("Enter the cm of adjacent side of the triangle (numbers only): "))
b = float(input("Enter the cm of the opposite side of the triangle (numbers only): "))

square_root = pow(a, 2) + pow(b, 2)
c = math.sqrt(square_root)
print(c)
