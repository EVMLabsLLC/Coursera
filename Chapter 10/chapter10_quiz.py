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
    
    # Section 1: Tuple Basics
    print_section("Section 1: Tuple Basics")
    
    questions = [
        {
            "question": "What is the correct way to create a tuple?",
            "options": [
                "A) t = []",
                "B) t = {}",
                "C) t = ()",
                "D) t = ''"
            ],
            "correct": "C",
            "explanation": "Tuples are created using parentheses () or the tuple() constructor."
        },
        {
            "question": "What is the output of this code?\nt = (1, 2, 3)\nprint(t[1])",
            "options": [
                "A) 1",
                "B) 2",
                "C) 3",
                "D) Error"
            ],
            "correct": "B",
            "explanation": "Tuple indexing starts at 0, so t[1] returns the second element, which is 2."
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
    
    # Section 2: Tuple Operations
    print_section("Section 2: Tuple Operations")
    
    print("Given the code:\n")
    print("t1 = (1, 2)")
    print("t2 = (3, 4)")
    print("print(t1 + t2)")
    
    print("\nWhat will be the output?")
    print("A) (1, 2, 3, 4)")
    print("B) (4, 6)")
    print("C) (1, 2)(3, 4)")
    print("D) Error")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "A", "The + operator concatenates tuples, creating a new tuple with all elements"):
        score += 1
    total_questions += 1
    
    # Section 3: Tuple Immutability
    print_section("Section 3: Tuple Immutability")
    
    print("Given the code:\n")
    print("t = (1, 2, 3)")
    print("t[0] = 4")
    
    print("\nWhat happens?")
    print("A) t becomes (4, 2, 3)")
    print("B) t becomes (1, 4, 3)")
    print("C) t remains (1, 2, 3)")
    print("D) TypeError is raised")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "D", "Tuples are immutable, so attempting to modify an element raises a TypeError"):
        score += 1
    total_questions += 1
    
    # Section 4: Tuple Unpacking
    print_section("Section 4: Tuple Unpacking")
    
    print("Given the code:\n")
    print("t = (1, 2, 3)")
    print("x, y, z = t")
    print("print(y)")
    
    print("\nWhat will be the output?")
    print("A) 1")
    print("B) 2")
    print("C) 3")
    print("D) Error")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "Tuple unpacking assigns each element to a variable in order, so y gets the second element (2)"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of tuples and their applications!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! Tuples are important immutable data structures in Python.")

if __name__ == "__main__":
    print("Welcome to the Chapter 10 Tuples Quiz!")
    print("This quiz will test your understanding of tuple creation, operations, and common patterns.")
    input("Press Enter to begin...")
    run_quiz() 