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
    
    # Section 1: File Basics
    print_section("Section 1: File Basics")
    
    questions = [
        {
            "question": "What is the correct way to open a file in Python?",
            "options": [
                "A) file = open('filename.txt', 'r')",
                "B) file = open('filename.txt')",
                "C) file = read('filename.txt')",
                "D) file = file('filename.txt')"
            ],
            "correct": "B",
            "explanation": "The basic way to open a file is using open('filename.txt'). The 'r' mode is the default for reading."
        },
        {
            "question": "What does the newline character '\\n' do?",
            "options": [
                "A) Creates a space",
                "B) Creates a new line",
                "C) Creates a tab",
                "D) Creates a backslash"
            ],
            "correct": "B",
            "explanation": "The \\n character is a special character that creates a new line when printed."
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
    
    # Section 2: File Reading
    print_section("Section 2: File Reading")
    
    print("Given the code:\n")
    print("fhand = open('mbox-short.txt')")
    print("for line in fhand:")
    print("    line = line.rstrip()")
    print("    if line.startswith('From:'):")
    print("        print(line)")
    
    print("\nWhat does this code do?")
    print("A) Prints all lines in the file")
    print("B) Prints only lines that start with 'From:'")
    print("C) Prints only the first line")
    print("D) Prints only the last line")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The code reads the file line by line and prints only lines that start with 'From:'"):
        score += 1
    total_questions += 1
    
    # Section 3: Error Handling
    print_section("Section 3: Error Handling")
    
    print("Given the code:\n")
    print("try:")
    print("    fhand = open('nonexistent.txt')")
    print("except:")
    print("    print('File cannot be opened')")
    print("    exit()")
    
    print("\nWhat happens if the file doesn't exist?")
    print("A) The program crashes")
    print("B) The program prints 'File cannot be opened' and exits")
    print("C) The program creates a new file")
    print("D) The program waits for user input")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The try-except block catches the FileNotFoundError and handles it gracefully"):
        score += 1
    total_questions += 1
    
    # Section 4: File Processing
    print_section("Section 4: File Processing")
    
    print("Given the code:\n")
    print("fhand = open('mbox-short.txt')")
    print("count = 0")
    print("for line in fhand:")
    print("    if line.startswith('From:'):")
    print("        count = count + 1")
    print("print('Count:', count)")
    
    print("\nWhat does this code do?")
    print("A) Counts all lines in the file")
    print("B) Counts lines starting with 'From:'")
    print("C) Counts words in the file")
    print("D) Counts characters in the file")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The code counts how many lines in the file start with 'From:'"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of file handling!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! File handling is essential for working with data in Python.")

if __name__ == "__main__":
    print("Welcome to the Chapter 7 File Handling Quiz!")
    print("This quiz will test your understanding of file operations, reading, and error handling.")
    input("Press Enter to begin...")
    run_quiz() 