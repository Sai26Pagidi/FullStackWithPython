age = 40
greeting = f"your age is {age}"
print(greeting)
age = 50
print(greeting)
# your age is 40
# your age is 40

# here age 40 cannot override with age 50 to overcome this problem we use format function

age = 40
que = "Your age is {}"
# we need to put braces empty so it is not a f-string
age_que = que.format(age)
# format(age) this will replace the braces with age 40
print(age_que)

age = 50
age_que = que.format(age)
print(age_que)