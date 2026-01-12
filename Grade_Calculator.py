English = int(input("Enter your marks in English : "))
while English < 0 or English > 100:
  print("invalid input.Try again.. !")
  English = int(input("Enter your marks in English : "))

Hindi = int(input("Enter your marks in hindi : "))
while Hindi < 0 or Hindi >100:
  print("invalid input. Try again ..!")
  Hindi = int(input("Enter your marks in hindi : "))

Math = int(input("Enter your marks in math : "))
while Math < 0 or Math > 100 :
  print("invalid inpurt . Try again ..!")
  Math = int(input("Enter your math marks : "))

Science = int(input("Enter your marks in science : "))
while Science < 0 or Science > 100 :
  print("invalid inpurt . Try again ..!")
  Science = int(input("Enter your science marks : "))

Urdu = int(input("Enter your marks in Urdu : "))
while Urdu < 0 or Urdu > 100 :
  print("invalid inpurt . Try again ..!")
  Urdu = int(input("Enter your urdu marks : "))

total_marks =English + Hindi + Math + Science + Urdu
precentage = (total_marks / 500 ) * 100

print(f"total marks : {total_marks}")
print(f"total precetage : {precentage}")

if precentage >= 90:
  print(f"Grade : [A+] and your precentage is  {precentage}% ")
elif precentage >= 85:
  print(f"Grade : [A] and your precentage is  {precentage}% ")
elif precentage >= 75:
  print(f"Grade : [B] and your precentage is  {precentage}% ")
elif precentage >= 65:
  print(f"Grade : [C] and your precentage is  {precentage}% ")
elif precentage >= 36:
  print(f"Grade : [D] and your precentage is  {precentage}% ")
else : 
  print(f"You are fail . your precentage {precentage}%")
