# Quiz questions stored in tuples
questions = (
    ("What is the capital of India?", "a", ["a. New Delhi", "b. Mumbai", "c. Kolkata", "d. Chennai"]),
    ("Which language is used for Data Science?", "b", ["a. Java", "b. Python", "c. C++", "d. HTML"]),
    ("2 + 2 * 2 = ?", "c", ["a. 6", "b. 8", "c. 6", "d. 4"]),
)

score = 0  # initialize score

# Loop through each question
for q in questions:
    print("\n" + q[0])  # print question
    for option in q[2]:  # print options
        print(option)
    
    answer = input("Enter your answer (a/b/c/d): ").lower()  # take input and convert to lowercase
    
    # Check if answer is correct
    if answer == q[1]:
        print("Correct!")
        score += 1  # increase score
    else:
        print("Wrong! Correct answer is:", q[1])

# Show final result
print("\nQuiz Completed!")
print("Your Score:", score, "out of", len(questions))
if score == len(questions):
    print("Excellent! You got all correct.")
elif score >= len(questions)//2:
    print("Good! But you can do better.")
else:
    print("You need to practice more.")
