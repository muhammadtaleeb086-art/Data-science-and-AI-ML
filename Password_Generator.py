# Password Generator


import random 
import string 

length = int(input("enter the length of password : "))

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_Char = letters + numbers + symbols


password = ""

for i  in range(length) :
  random_char = random.choice(all_Char)
  password += random_char

print("Generated Password :",password)
