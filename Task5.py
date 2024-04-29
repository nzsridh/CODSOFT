import random

# Quiz questions and answers
quiz_data = [
    {"question": "'.MOV. extension refers usually to what kind of file?","choices": ["A) MS Office document", "B) Audio file", "C) Animation/movie file", "D) Image file"], "answer": "C"},
    {"question": "Who invented Jet Engine?", "choices": ["A)Roger Bacon", "b) Lewis E. Waterman", "C) Gottlieb Daimler", "D) Sir Frank Whittle"], "answer": "D"},
    {"question": "What is the largest ocean on Earth?", "choices": ["A) Atlantic", "B) Arctic", "C) Indian", "D) Pacific"], "answer": "D"},
    {"question": "In what year did the Titanic sink?", "choices": ["A) 1912", "B) 1921", "C) 1905", "D) 1918"], "answer": "A"},
    {"question": "Which country drinks the most amount of coffee per person? ", "choices": ["A) Colombia", "B) Finland", "C) Italy", "D) USA"], "answer": "B"},
    {"question": "What is the chemical symbol for gold?", "choices": ["A) Au", "B) Ag", "C) Fe", "D) O"], "answer": "A"},
    # Add more questions with the same structure
]

# Function to display the welcome message and rules
def display_welcome():
    input("Welcome to the Quiz Game! Press Enter to start playing.")
    print("You will be presented with multiple-choice questions. Choose the correct answer to gain points.")
    print("Let's get started!\n")

# Function to present questions
def present_questions():
    score = 0
    for i, question in enumerate(random.sample(quiz_data, len(quiz_data)), 1):
        print(f"Question {i}: {question['question']}")
        for choice in sorted(question["choices"]):
            print(choice)
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question['choices'][ord(question['answer']) - ord('A')]}.\n")
        if i < len(quiz_data):
            input("Are you ready for the next question? Press Enter to continue.")
        print()
    return score

# Function to display final results
def display_results(score):
    print(f"Your final score is: {score}/{len(quiz_data)}")
    if score == len(quiz_data):
        print("Perfect score! Well done!")
    elif score > len(quiz_data) // 2:
        print("Great job! You've passed the quiz.")
    else:
        print("Good effort! Try again to improve your score.")

# Function to ask the user if they want to play again
def play_again():
    return input("Do you want to play again? (yes/no): ").strip().lower() == "yes"

# Main game loop
def main():
    display_welcome()
    while True:
        score = present_questions()
        display_results(score)
        if not play_again():
            break
    print("Thank you for playing the quiz game!")

if __name__ == "__main__":
    main()
