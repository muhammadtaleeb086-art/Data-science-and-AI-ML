num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))

print("-----Select operation-----")
print("add  sub  mul  div")

option = input("Enter your option: ").lower()

if option == "add":
    print(f"Addition of two numbers is {num1 + num2}")

elif option == "sub":
    print(f"Subtraction of two numbers is {num1 - num2}")

elif option == "mul":
    print(f"Multiplication of two numbers is {num1 * num2}")

elif option == "div":
    if num2 != 0:
        print(f"Division of two numbers is {num1 / num2}")
    else:
        print("Cannot divide by zero")

else:
    print("Invalid option")
