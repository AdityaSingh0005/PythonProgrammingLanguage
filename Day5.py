# TypeCasting

# The conversion of one data type into other data type is known as type casting in python or any type conversion in python
a = int("1")
b = int("2")
print(a+b) # Type 1
print(int(a)+int(b)) #Type 2

# Types of Typecasting
# two types of typcasting

# 1. Explicit Conversion 
# The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per requirement is known as explicit type convertion

string = "15"
number = 7
string_number = int(string)

sum = number + string_number
print("The Sum of both the numbers is: ", sum)

# Implicit type casting:
# Data types in python do not have the same level ordering of data types is not the same in python. According to the level , One data tpe is converted into other by the python interpreter itself(automatically).This is called , implicit typecasting in python

c = 1.9
d = 8
print(c+d)