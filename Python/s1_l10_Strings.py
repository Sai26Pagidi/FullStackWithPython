name = "sai"
print("Your name is "+name)

"""Now we are adding integer to string"""
# age = 34
# print("Your age is "+age)
# we cannot concatenate int to string in python

# while we can convert int to string datatype
age = str(34)
print("Your age is "+age)

# there is another way we can add int to string without converting datatypes and by using f-string and using braces
age = 44
print(f"Your age is {age}") 

name = "sai"
age = 28
info = f"Your name is {name} and your age is {age}"
print(info)
name = "teja"
print(info)

# above programme is not overriding name teja with sai so there is another function called format to overcome this

