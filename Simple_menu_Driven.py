while True:
 print("---Menu---")
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiply")
 print("4.Division")
 print("5.Exit")

 choice = int(input("enter number which option you choose : "))
 if choice == 5:
    print("thank you...")
    break


 num1 = float(input("Enter a number :"))
 num2 = float(input("Enter a number :"))

 if choice == 1:
    print(f"addtion : {num1 + num2}")

 elif choice == 2:
    print(f"Subtraction : {num1-num2}")
    
 elif choice == 3:
    print(f"multiply : {num1*num2}")
    
 elif choice == 4:
    if num2 == 0:
      print("Cannot divide by zero .")
    else :
      print(f"division : {num1 / num2}")
      
else :
    print("Invalid number choose. Try again...")