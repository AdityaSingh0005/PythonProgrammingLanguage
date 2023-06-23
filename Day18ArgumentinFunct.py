# Arguments in Python
# Default Argument

def average(a, b, c=1):
    print("The average is ", (a+b+c)/2)
    
average(1,5)
    
    
def name(fname, mname = "Thakur", lname = "Aditya"):
    print("Hello,", fname, mname, lname)
    
name("Thakur", "Aditya", "Singh")

# Keyword Argument
average(b=9, a=21)

# Required Argument
average(5, 6)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum/len(numbers))
    
average(5,6,7,1)