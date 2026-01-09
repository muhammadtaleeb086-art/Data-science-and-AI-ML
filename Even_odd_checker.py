while True:
    user_input = input("Enter a number (to end program type end): ")

    if user_input == "end":
        print("Program ended.")
        break

    number = int(user_input)

    if number % 2 == 0:
        print(f"Your number {number} is even.")
    else:
        print(f"Your number {number} is odd.")
