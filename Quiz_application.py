questions = (
    ("What is the capital of India?",
     "1. Mumbai", "2. Delhi", "3. Kolkata", "4. Chennai", 2),

    ("Which language is used for Data Science?",
     "1. Java", "2. C", "3. Python", "4. HTML", 3),

    ("Which data type is immutable?",
     "1. List", "2. Tuple", "3. Set", "4. Dictionary", 2),

    ("Which keyword is used for loop in Python?",
     "1. if", "2. while", "3. def", "4. return", 2)
)

total_score = 0
total_questions = len(questions)

print("---Welcome to Quiz Game---")

for q in questions:
  print("\n" + q[0])
  print(q[1])
  print(q[2])
  print(q[3])
  print(q[4])
  
  user_answer = int(input("Enter your answer(1-4):"))

  if user_answer == q[5]:
    print("Correct Answer")
    total_score += 1
  else :
    print("your answer is wrong..")
    print("correct option is ", q[5])
  
percentage = (total_score / total_questions) * 100

print("\n---- Quiz Result ----")
print("Total Questions:", total_questions)
print("Correct Answers:", total_score)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Result: Excellent ")
elif percentage >= 50:
    print("Result: Good ")
else:
    print("Result: Needs Improvement ")

print("Thank you for playing!")
  

