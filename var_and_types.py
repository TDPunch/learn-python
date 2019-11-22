"""
In this file I will go throught the variables and types tutorial on 
learnpython.org
"""

myint = 1;
print(myint);

# Floating point numbers can be defined in 2 ways
myfloat = 7.0
print(myfloat)
myflooat = float(7)
print(myfloat)

# Strings can be defined with either single quotes or double quotes
# The difference is that single quotes won't allow apostrophes
# it would just terminate the string
mystring = 'hello'
print(mystring)
mystring2 = "42"
print(mystring)

# Simple operators can be executed on numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "Hello"
world = "World"
hello_world = hello + " " + world
print(hello_world)

# Assignments can be done on more than one variable on the same line
a, b = 3, 4
print(a,b)


# Mixing operators between numbers and strings in not supported
# This will not work
print(one + two + hello)
