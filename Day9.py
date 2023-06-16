# String Methods
# Strings are immutable
a = "Aditya!!!!"
print(len(a))

print(a.upper()) # Upper Case String Method

print(a.lower()) # Lower Case String Method

print(a.rstrip("!"))

print(a.replace("Aditya", "Thakur Aditya Singh"))

print(a.split(" "))

blogHeading = "introduction to python"
print(blogHeading.capitalize())

str1 = "Welcome to Console!!!"

str1 = "He's name is dan. He is an honest man"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))

print(a.count("Aditya"))

print(str1.endswith("!!!"))

print(str1.find("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "Welcome"
print(str1.islower())

str1 = "We have any balls\n"
print(str1.isprintable())

str1 = "We have any balls\n"
print(str1.isspace())

str1 = "Blog Of Code"
print(str1.istitle())

str2 = "Python is a Interpreted Language"
print(str2.startswith("Python"))

str2 = "Python is a Interpreted Language"
print(str2.swapcase())

str2 = "His name is Dan. Dan is an honest man."
print(str2.title())

