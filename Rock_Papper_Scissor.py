'''
1-input from user (rock, paper , scissor)
2-randomly generate computer input (rock, paper , scissor)
3-compare user input and computer input
4- print result (win, lose , draw)

cases :
rock - Rock = draw
rock - paper =  paper wins
rock - scissor = rock wins

paper - paper = draw
paper - rock = paper wins
paper - scissor = scissor wins

scissor - scissor = draw
scissor - rock = rock wins
scissor - paper = scissor wins

'''
import random
item_list = ['rock', 'paper','scissor']
user_input = input("Enter your choice (rock, paper, scissor): ").lower()
if user_input not in item_list:
   print("Invalid input ! please enter correct input")
else:
   computer_input = random.choice(item_list)
   print(f"Computer choice is : {computer_input}")
   if user_input == computer_input:
      print("its a draw ")
   elif (user_input == 'rock' and computer_input == 'scissor') or (user_input == 'paper' and computer_input == 'rock') or (user_input == 'scissor' and computer_input == 'paper'):
      print(" You win !")
   else:
      print("Computer wins !")

# when we play game continuously then we add while loop 

import random

item_list = ['rock', 'paper', 'scissor']

while True:
    user_input = input("Enter your choice (rock, paper, scissor) or 'exit' to quit: ").lower()
    
    if user_input == "exit":
        print("Game Over! Thanks for playing.")
        break
    
    if user_input not in item_list:
        print("Invalid input! Please enter correct input")
        continue
    
    computer_input = random.choice(item_list)
    print(f"Computer choice is: {computer_input}")

    if user_input == computer_input:
        print("It's a draw")
    elif (user_input == 'rock' and computer_input == 'scissor') \
         or (user_input == 'paper' and computer_input == 'rock') \
         or (user_input == 'scissor' and computer_input == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
