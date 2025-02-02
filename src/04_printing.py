"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("row 1: x is %i, y is %d, z is \"%s\" " %(x, y, z))

# Use the 'format' string method to print the same thing
print("row 2: x is {}, y is {:1.2f}, z is \"{}\" ".format(x, y, z))

# Finally, print the same thing using an f-string
print(f"row 3: x is {x}, y is {y:1.3}, z is \"{z}\"")
