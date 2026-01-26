account_holder = input("Enter account holder name: ")
balance = 0
transactions = []

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount

            transaction = {
                "type": "Deposit",
                "amount": amount,
                "balance_after": balance
            }
            transactions.append(transaction)
            print("Deposit successful.")
        else:
            print("Invalid amount.")

    elif choice == "2":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount

            transaction = {
                "type": "Withdraw",
                "amount": amount,
                "balance_after": balance
            }
            transactions.append(transaction)
            print("Withdrawal successful.")

    elif choice == "3":
        print("Current Balance:", balance)

    elif choice == "4":
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            print("\n--- Transaction History ---")
            for t in transactions:
                print(
                    "Type:", t["type"],
                    "| Amount:", t["amount"],
                    "| Balance After:", t["balance_after"]
                )

    elif choice == "5":
        print("Thank you for using Banking System.")
        break

    else:
        print("Invalid choice, try again.")

