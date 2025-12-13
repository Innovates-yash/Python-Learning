# operators in python
# 1. Arithmetic operators Used to perform common mathematical operations.
# 2. Assignment operators Used to assign values to variables.
# 3. Comparison operators Used to compare two values. These always return True or False.
# 4. Logical operators Used to combine conditional statements.
# 5. Identity operators Used to compare if objects are actually the same object in memory, not just if they have the same value.
# 6. Membership operators Used to test if a sequence (like a list or string) contains a specific object.
# 7. Bitwise operators Used to compare (binary) numbers. These are less common for beginners but good to know exist.


# Arithmetic Operators
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # float division
print(int(a/b))  # integer division
print(a//b)  # floor division
print(a%b)  # modulus operator
print(a**b)  # exponentiation operator

# Note : python use BODMAS rule for solving expression

# Assignment Operators and compound assignment operators
a = 5
b += 20  # equivalent to b = b + 20
print(b)

c = 10
c += 10

c -= 10
print(c)
