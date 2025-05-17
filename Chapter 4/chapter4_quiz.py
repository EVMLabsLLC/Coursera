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
    
    # Section 1: Function Basics
    print_section("Section 1: Function Basics")
    
    questions = [
        {
            "question": "What is the correct way to define a function in Python?",
            "options": [
                "A) function myFunction():",
                "B) def myFunction():",
                "C) define myFunction():",
                "D) func myFunction():"
            ],
            "correct": "B",
            "explanation": "In Python, functions are defined using the 'def' keyword followed by the function name and parentheses."
        },
        {
            "question": "What will be returned by this function?\ndef addtwo(a, b):\n    added = a + b\n    return a",
            "options": [
                "A) The sum of a and b",
                "B) The value of a",
                "C) The value of b",
                "D) None"
            ],
            "correct": "B",
            "explanation": "The function returns 'a' instead of 'added', which is a bug. It should return 'added' to get the sum."
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
    
    # Section 2: Function Parameters and Return Values
    print_section("Section 2: Function Parameters and Return Values")
    
    print("Given the function:\n")
    print("def greet(lang):")
    print("    if lang == 'es':")
    print("        return 'Hola'")
    print("    elif lang == 'fr':")
    print("        return 'Bonjour'")
    print("    else:")
    print("        return 'Hello'")
    
    print("\nWhat will greet('fr') return?")
    print("A) Hello")
    print("B) Hola")
    print("C) Bonjour")
    print("D) None")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "C", "When lang is 'fr', the function returns 'Bonjour'"):
        score += 1
    total_questions += 1
    
    # Section 3: Error Handling in Functions
    print_section("Section 3: Error Handling in Functions")
    
    print("Given the code:\n")
    print("def computepay(hours, rate):")
    print("    if hours <= 40:")
    print("        pay = hours * rate")
    print("    else:")
    print("        regular_pay = 40 * rate")
    print("        overtime_pay = (hours - 40) * (rate * 1.5)")
    print("        pay = regular_pay + overtime_pay")
    print("    return pay")
    
    print("\nWhat will computepay(45, 10) return?")
    print("A) 450")
    print("B) 475")
    print("C) 500")
    print("D) 525")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "Regular pay (40 * 10) = 400, Overtime pay (5 * 15) = 75, Total = 475"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of functions and error handling!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! Functions are essential building blocks in Python programming.")

if __name__ == "__main__":
    print("Welcome to the Chapter 4 Functions and Error Handling Quiz!")
    print("This quiz will test your understanding of function definition, parameters, return values, and error handling.")
    input("Press Enter to begin...")
    run_quiz() 