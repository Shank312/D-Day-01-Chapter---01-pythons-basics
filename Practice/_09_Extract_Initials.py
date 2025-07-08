
# Task: Ask for full name and print the initials.

name = input("Enter your full name : ")
initials = [word[0].upper() for word in name.split()]
print("Initials : ", ".".join(initials))