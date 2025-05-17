"""input function is used 
to enter user any input, and input gives output via string format"""
myName = input("Please enter your name: ")
print(f"Your Name is {myName}")


age = input("Enter your age: ")
print(f"you lived for {age*12} months.")
"""above programme converts age times 12 into string to calculate this we need to convert string to int"""

age = int(input("Enter your age: "))
print(f"you lived for {age*12} months.")
