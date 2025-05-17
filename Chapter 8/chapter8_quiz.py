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
    
    # Section 1: List Basics
    print_section("Section 1: List Basics")
    
    questions = [
        {
            "question": "What is the output of this code?\nnumbers = [2, 14, 26, 41, 63]\nnumbers[2] = 28\nprint(numbers)",
            "options": [
                "A) [2, 14, 26, 41, 63]",
                "B) [2, 14, 28, 41, 63]",
                "C) [2, 14, 26, 28, 63]",
                "D) Error"
            ],
            "correct": "B",
            "explanation": "The code changes the third element (index 2) from 26 to 28, demonstrating list mutability."
        },
        {
            "question": "What is the result of len(['red', ['1', '2'], '24'])?",
            "options": [
                "A) 3",
                "B) 4",
                "C) 5",
                "D) 6"
            ],
            "correct": "A",
            "explanation": "The len() function counts the number of elements in the list, including the nested list as one element."
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
    
    # Section 2: List Operations
    print_section("Section 2: List Operations")
    
    print("Given the code:\n")
    print("numbers = [9, 41, 12, 3, 74, 15]")
    print("print(numbers[1:3])")
    
    print("\nWhat will be the output?")
    print("A) [9, 41]")
    print("B) [41, 12]")
    print("C) [41, 12, 3]")
    print("D) [9, 41, 12]")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The slice [1:3] returns elements at indices 1 and 2, which are 41 and 12"):
        score += 1
    total_questions += 1
    
    # Section 3: List Methods
    print_section("Section 3: List Methods")
    
    print("Given the code:\n")
    print("numbers = [3, 1, 4, 2]")
    print("numbers.sort()")
    print("print(numbers)")
    
    print("\nWhat will be the output?")
    print("A) [3, 1, 4, 2]")
    print("B) [1, 2, 3, 4]")
    print("C) [4, 3, 2, 1]")
    print("D) [2, 4, 1, 3]")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The sort() method sorts the list in ascending order in place"):
        score += 1
    total_questions += 1
    
    # Section 4: String to List Conversion
    print_section("Section 4: String to List Conversion")
    
    print("Given the code:\n")
    print("text = 'first;second;third'")
    print("words = text.split(';')")
    print("print(words)")
    
    print("\nWhat will be the output?")
    print("A) ['first', 'second', 'third']")
    print("B) ['first;second;third']")
    print("C) ['first', ';', 'second', ';', 'third']")
    print("D) Error")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "A", "The split(';') method splits the string at each semicolon and returns a list of the parts"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of lists and list operations!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! Lists are fundamental data structures in Python.")

if __name__ == "__main__":
    print("Welcome to the Chapter 8 Lists and List Operations Quiz!")
    print("This quiz will test your understanding of list creation, manipulation, and common list operations.")
    input("Press Enter to begin...")
    run_quiz() 