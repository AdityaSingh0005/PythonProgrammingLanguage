
x = int(input("Enter the value of x: "))
# X is a variable to match
match x:
    # if x is 0
    case 0:
        print("X is Zero")
    # Case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # Default case (will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x) 