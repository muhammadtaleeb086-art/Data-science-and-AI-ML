temp_value = float(input("enter a temperature  value  : "))
from_unit = input("enter unit Celcius(C), Fahrenheit(F) : ").upper()
to_unit = input("Convert to (C,F) : ").upper()

if from_unit == "C" and to_unit == "F":
  result = (temp_value * 9/5 ) + 32
  print(f"{temp_value}`C == {result}`F")


elif from_unit == "F" and to_unit == "C": 
  result = (temp_value - 32 ) * 5/9 
  print(f"{temp_value}F = {result}C")

elif from_unit == to_unit:
   print("Same unit selected. Temperature remains:", temp_value)

else:
    print("Invalid unit entered")