# conditionl statements in python

# 3 types of conditional statements
# 1. if statement
# 2. if else statement
# 3. if elif else statement

# if statement
a = 10
if a > 5:
    print("a is greater than 5")

# if else statement
b = 15
if b < 10:
    print("b is less than 10")
else:
    print("b is greater than or equal to 10")

# if elif else statement

age = int(input("Enter your age:   "))

if int(age) <= 18:
    print("your are eligible for voting")
elif int(age) == 18:
    print("your age is 18 you are eligible for voting")
else:
    print("your are not eligible for voting")