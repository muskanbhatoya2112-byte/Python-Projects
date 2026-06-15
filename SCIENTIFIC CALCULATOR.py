import math

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square Root")
print("7. Sine")
print("8. Cosine")
print("9. Tangent")
print("10. Logarithm")

choice = int(input("Enter your choice: "))

if choice <= 5:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", a + b)
    elif choice == 2:
        print("Result =", a - b)
    elif choice == 3:
        print("Result =", a * b)
    elif choice == 4:
        print("Result =", a / b)
    elif choice == 5:
        print("Result =", a ** b)

else:
    n = float(input("Enter a number: "))

    if choice == 6:
        print("Result =", math.sqrt(n))
    elif choice == 7:
        print("Result =", math.sin(n))
    elif choice == 8:
        print("Result =", math.cos(n))
    elif choice == 9:
        print("Result =", math.tan(n))
    elif choice == 10:
        print("Result =", math.log(n))
    else:
        print("Invalid Choice")