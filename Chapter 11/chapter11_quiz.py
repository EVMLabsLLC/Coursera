import re
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
    
    # Section 1: Basic Regex Patterns
    print_section("Section 1: Basic Regex Patterns")
    
    questions = [
        {
            "question": "What does the '^' character do in a regular expression?",
            "options": [
                "A) Matches any character",
                "B) Matches the start of a line",
                "C) Matches the end of a line",
                "D) Matches a literal '^' character"
            ],
            "correct": "B",
            "explanation": "The '^' character is an anchor that matches the start of a line or string."
        },
        {
            "question": "Which pattern would match a single digit?",
            "options": [
                "A) [0-9]",
                "B) [0-9]+",
                "C) [0-9]*",
                "D) [0-9]?"
            ],
            "correct": "A",
            "explanation": "[0-9] matches exactly one digit, while the others match one or more (+), zero or more (*), or zero or one (?) digits."
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
    
    # Section 2: Pattern Matching
    print_section("Section 2: Pattern Matching")
    
    # Test email pattern matching
    print("Given the pattern: r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'")
    print("Which of these is a valid email match?")
    test_emails = [
        "user@example.com",
        "invalid.email",
        "user@.com",
        "user@example"
    ]
    
    for i, email in enumerate(test_emails, 1):
        print(f"{i}) {email}")
    
    answer = input("\nEnter the number of the valid email: ")
    if check_answer(answer, "1", "The first option is a valid email format with proper domain structure."):
        score += 1
    total_questions += 1
    
    # Section 3: File Handling with Regex
    print_section("Section 3: File Handling with Regex")
    
    print("Given the code:\n")
    print("import re")
    print("file = open('data.txt')")
    print("for line in file:")
    print("    line = line.rstrip()")
    print("    if re.search('^From:', line):")
    print("        print(line)")
    
    print("\nWhat does this code do?")
    print("A) Prints all lines containing 'From:' anywhere in the line")
    print("B) Prints only lines that start with 'From:'")
    print("C) Prints all lines in the file")
    print("D) Prints only the first line containing 'From:'")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The '^' anchor ensures we only match lines that start with 'From:'"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of regular expressions!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! Regular expressions take time to master.")

if __name__ == "__main__":
    print("Welcome to the Chapter 11 Regular Expressions Quiz!")
    print("This quiz will test your understanding of regular expressions in Python.")
    input("Press Enter to begin...")
    run_quiz() 