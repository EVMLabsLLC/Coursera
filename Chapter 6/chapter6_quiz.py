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
    
    # Section 1: String Basics
    print_section("Section 1: String Basics")
    
    questions = [
        {
            "question": "What is the output of len('banana')?",
            "options": [
                "A) 5",
                "B) 6",
                "C) 7",
                "D) Error"
            ],
            "correct": "B",
            "explanation": "The len() function returns the number of characters in the string, which is 6 for 'banana'."
        },
        {
            "question": "What is the result of 'a' in 'banana'?",
            "options": [
                "A) True",
                "B) False",
                "C) 1",
                "D) Error"
            ],
            "correct": "A",
            "explanation": "The 'in' operator checks if a substring exists in a string. 'a' appears in 'banana', so it returns True."
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
    
    # Section 2: String Slicing
    print_section("Section 2: String Slicing")
    
    print("Given the string s = 'Monty Python', what is s[0:4]?")
    print("A) 'Mont'")
    print("B) 'Monty'")
    print("C) 'M'")
    print("D) 'Python'")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "A", "String slicing [0:4] returns characters from index 0 up to (but not including) index 4"):
        score += 1
    total_questions += 1
    
    # Section 3: String Methods
    print_section("Section 3: String Methods")
    
    print("Given the code:\n")
    print("text = 'Hello World'")
    print("print(text.find('World'))")
    
    print("\nWhat will be the output?")
    print("A) 0")
    print("B) 5")
    print("C) 6")
    print("D) -1")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "C", "The find() method returns the index where the substring 'World' starts, which is 6"):
        score += 1
    total_questions += 1
    
    # Section 4: String Manipulation
    print_section("Section 4: String Manipulation")
    
    print("Given the code:\n")
    print("text = '  Hello World  '")
    print("print(text.strip())")
    
    print("\nWhat will be the output?")
    print("A) '  Hello World  '")
    print("B) 'Hello World'")
    print("C) 'Hello World  '")
    print("D) '  Hello World'")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The strip() method removes leading and trailing whitespace from the string"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of string manipulation!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! String manipulation is essential in Python programming.")

if __name__ == "__main__":
    print("Welcome to the Chapter 6 String Manipulation Quiz!")
    print("This quiz will test your understanding of string methods, slicing, and common string operations.")
    input("Press Enter to begin...")
    run_quiz() 