# Loops 
# For Loops
name = 'Abhishek'
for i in name:
    print(i)
    if(i == "b"):
        print("This is something special!")
        
colors = ["Red", "Green", "Blue", "Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

Range
# for k in range(5):
#     print(k+2)
# for k in range(1, 20001):
#     print(k)
    
for k in range(1, 12, 3):
    print(k)