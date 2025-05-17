age = 28
my_comp = age<18 and age>20
print(my_comp)

age = 28
my_comp = age<18 or age>20
print(my_comp)

# examples
print(bool(0))
print(bool(13))
print(bool(""))
print(bool("sai"))
print(bool([]))
print(bool([1,2,3,4,5,6,]))

machine_default_name = "Python"
user_name = input("Please Enter Your Name: (optional)")
greeting = machine_default_name or user_name
print(f"Hello, {greeting}")

x = True
cmp = x and 18
print(cmp)

age = int(input("Enter your age: ")) #user enters 16
side_job = True
print(age > 18 and age < 65 or side_job) #False and True or True
#we evaluate from left to right (False and True -- False)--> (False or True -- True)
#last output will be True