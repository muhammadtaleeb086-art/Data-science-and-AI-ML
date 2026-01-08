Secert_number = 5

while True :
  number = int(input("Enter a number 1 to 10 :"))

  if number == Secert_number:
    print(f"great! you guess  correct number {Secert_number}")
    break
  elif number < Secert_number:
    print(f"number {number} is small! Try again ..")
  else:
    print(f"number {number} is big ! Try again..")
  
