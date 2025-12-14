# 1. Accept two numbers and print greatest between them

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater  than {num2}")
else :
    print(f"{num2} is greater than {num1}")

print("question 1 complete")
# Accept the gender from the user as char and print the respective greeting message

Gender = str(input("Enter your Gender: "))

if str(Gender) == 'M' or str(Gender) == 'm':
    print("Good Morning Sir")
elif str(Gender) == 'F' or str(Gender) == 'f':
    print("Good morning mam")
else:
    print("Unrecognized Gender")

print("Question 2 complete")