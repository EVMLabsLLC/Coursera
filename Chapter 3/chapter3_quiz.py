import random

def print_section(title):
    print("\n" + "="*50)
    print(title)
    print("="*50 + "\n")

def check_answer(user_answer, correct_answer, explanation):
    if user_answer.lower() == correct_answer.lower():
        print("✓ Correct! " + explanation)
        return True
    else:
        print("✗ Incorrect. The correct answer is: " + correct_answer)
        print("Explanation: " + explanation)
        return False

def run_quiz():
    score = 0
    total_questions = 0
    
    # Section 1: Conditional Statements
    print_section("Section 1: Conditional Statements")
    
    questions = [
        {
            "question": "What is the correct syntax for an if-elif-else statement in Python?",
            "options": [
                "A) if condition: elif condition: else:",
                "B) if (condition) { } else if (condition) { } else { }",
                "C) if condition: elif condition: else:",
                "D) if condition then elif condition then else"
            ],
            "correct": "C",
            "explanation": "Python uses colons (:) after conditions and indentation for blocks. The correct syntax is 'if condition: elif condition: else:'"
        },
        {
            "question": "In the pay calculator program, what happens when hours > 40?",
            "options": [
                "A) Regular pay is calculated for all hours",
                "B) Overtime pay is calculated for all hours",
                "C) Regular pay for first 40 hours, then overtime for remaining hours",
                "D) The program returns an error"
            ],
            "correct": "C",
            "explanation": "When hours exceed 40, the program calculates regular pay for the first 40 hours and overtime pay (1.5x rate) for the remaining hours."
        }
    ]
    
    for q in questions:
        total_questions += 1
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("\nYour answer (A/B/C/D): ").upper()
        if check_answer(answer, q["correct"], q["explanation"]):
            score += 1
    
    # Section 2: Error Handling
    print_section("Section 2: Error Handling")
    
    print("Given the code:\n")
    print("try:")
    print("    hours = float(input('Enter Hours: '))")
    print("    rate = float(input('Enter Rate: '))")
    print("    pay = hours * rate")
    print("    print('Pay:', pay)")
    print("except:")
    print("    print('Error, please enter numeric input')")
    
    print("\nWhat happens if the user enters 'ten' for hours?")
    print("A) The program crashes")
    print("B) The program prints 'Pay: ten'")
    print("C) The program prints 'Error, please enter numeric input'")
    print("D) The program converts 'ten' to 10")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "C", "The try-except block catches the ValueError when converting 'ten' to float and executes the except block"):
        score += 1
    total_questions += 1
    
    # Section 3: Grade Calculator
    print_section("Section 3: Grade Calculator")
    
    print("Given a score of 0.85, what grade would be assigned?")
    print("A) A")
    print("B) B")
    print("C) C")
    print("D) D")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "A score of 0.85 falls in the B range (0.8 to 0.9)"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of conditional execution and error handling!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! These concepts are fundamental to Python programming.")

if __name__ == "__main__":
    print("Welcome to the Chapter 3 Conditional Execution and Error Handling Quiz!")
    print("This quiz will test your understanding of if-else statements, try-except blocks, and input validation.")
    input("Press Enter to begin...")
    run_quiz() 