balance = 958500
correct_pin = 1886
attempt = 3

print("Welcome ATM")
while attempt > 0:
  pin = int(input("Please enter your ATM pin number :"))

  if pin == correct_pin :
    print("Loign succesfully.")
    break
  else :
    attempt -= 1
    print("Wrong pin number. try again...")

if attempt == 0 :
  print("Card blocked. Too many wrong attempts.")
else :

  while True :

    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")

    choice = int(input("enter your choice : "))

    if choice == 1:
     print(f"Your acount balance : {balance}")

    elif choice == 2:
     amount = int(input("enter the amount you want to withdraw : "))
     if amount > 0 and amount <= balance:
      balance -= amount 
      print(f"{amount} is withdraw successfully...")
      print(f"{balance} remaining balance.")
     else :
      print("Invalid amount or insufficient balance .")

    elif choice == 3:
     amount = int(input("enter the amount you want deposit : "))
     if amount > 0:
      balance += amount
      print(f"{amount} is successfully deposite in your account.")
      print(f"{balance}  Now total balance in account.")
     else :
      print("Invalid amount.")

    elif choice == 4:
     print("Thank you for using ATM.")
     break
    
    else :
     print("Invalid option. Try again ...")
      