# ==========================================
# PYTHON BASICS - RECTANGLE CALCULATOR
# ==========================================

# Variables and Data Types
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

# Operators
area = length * width
perimeter = 2 * (length + width)

print("\nArea =", area)
print("Perimeter =", perimeter)

# Function
def display():
    print("Rectangle Calculation Completed")

display()

# For Loop
print("\nMultiplication Table of 2")
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)

# While Loop
print("\nNumbers from 1 to 5")
n = 1
while n <= 5:
    print(n)
    n += 1

print("Program Completed")
