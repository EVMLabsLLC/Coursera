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
    
    # Section 1: Dictionary Basics
    print_section("Section 1: Dictionary Basics")
    
    questions = [
        {
            "question": "What is the correct way to create an empty dictionary?",
            "options": [
                "A) dict = []",
                "B) dict = {}",
                "C) dict = ()",
                "D) dict = ''"
            ],
            "correct": "B",
            "explanation": "Empty dictionaries are created using curly braces {} or the dict() constructor."
        },
        {
            "question": "What is the output of this code?\nd = {'a': 1, 'b': 2}\nd['c'] = 3\nprint(d['b'])",
            "options": [
                "A) 1",
                "B) 2",
                "C) 3",
                "D) Error"
            ],
            "correct": "B",
            "explanation": "The code prints the value associated with key 'b', which is 2."
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
    
    # Section 2: Dictionary Methods
    print_section("Section 2: Dictionary Methods")
    
    print("Given the code:\n")
    print("d = {'a': 1, 'b': 2, 'c': 3}")
    print("print(d.get('b', 0))")
    
    print("\nWhat will be the output?")
    print("A) 0")
    print("B) 1")
    print("C) 2")
    print("D) 3")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "C", "The get() method returns the value for key 'b' if it exists, otherwise returns the default value 0"):
        score += 1
    total_questions += 1
    
    # Section 3: Dictionary Iteration
    print_section("Section 3: Dictionary Iteration")
    
    print("Given the code:\n")
    print("d = {'a': 1, 'b': 2, 'c': 3}")
    print("for key in d:")
    print("    print(key, d[key])")
    
    print("\nWhat will be the output?")
    print("A) a 1 b 2 c 3")
    print("B) 1 2 3")
    print("C) a b c")
    print("D) Error")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "A", "The loop iterates through the keys and prints each key-value pair"):
        score += 1
    total_questions += 1
    
    # Section 4: Dictionary Counting
    print_section("Section 4: Dictionary Counting")
    
    print("Given the code:\n")
    print("counts = dict()")
    print("names = ['a', 'b', 'a', 'c', 'b']")
    print("for name in names:")
    print("    counts[name] = counts.get(name, 0) + 1")
    print("print(counts)")
    
    print("\nWhat will be the output?")
    print("A) {'a': 2, 'b': 2, 'c': 1}")
    print("B) {'a': 1, 'b': 1, 'c': 1}")
    print("C) {'a': 2, 'b': 1, 'c': 1}")
    print("D) Error")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "A", "The code counts occurrences of each name in the list using the get() method with a default value of 0"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of dictionaries and collections!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! Dictionaries are powerful data structures in Python.")

if __name__ == "__main__":
    print("Welcome to the Chapter 9 Dictionaries and Collections Quiz!")
    print("This quiz will test your understanding of dictionary creation, methods, and common patterns.")
    input("Press Enter to begin...")
    run_quiz() 