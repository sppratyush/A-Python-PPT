a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Not possible")

print("Even/Odd:")
print(f"{a} is", "Even" if a % 2 == 0 else "Odd")
print(f"{b} is", "Even" if b % 2 == 0 else "Odd")

a_float = float(a)
print("Float value:", a_float)