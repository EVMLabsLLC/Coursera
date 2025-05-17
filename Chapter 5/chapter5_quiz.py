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
    
    # Section 1: While Loops
    print_section("Section 1: While Loops")
    
    questions = [
        {
            "question": "What will be the output of this code?\nn = 5\nwhile n > 0:\n    print(n)\n    n = n - 1\nprint('Blastoff!')",
            "options": [
                "A) 5 4 3 2 1 Blastoff!",
                "B) 5 4 3 2 1 0 Blastoff!",
                "C) 4 3 2 1 0 Blastoff!",
                "D) 5 4 3 2 1"
            ],
            "correct": "A",
            "explanation": "The loop prints numbers from 5 down to 1, then prints 'Blastoff!' when n becomes 0."
        },
        {
            "question": "What is a sentinel value?",
            "options": [
                "A) A value that marks the end of a sequence",
                "B) A value that starts a sequence",
                "C) A value that is always zero",
                "D) A value that is always negative"
            ],
            "correct": "A",
            "explanation": "A sentinel value is a special value used to signal the end of a sequence or loop, like 'done' in the number input program."
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
    
    # Section 2: For Loops
    print_section("Section 2: For Loops")
    
    print("Given the code:\n")
    print("friends = ['Joseph', 'Glenn', 'Sally']")
    print("for friend in friends:")
    print("    print('Happy New Year:', friend)")
    print("print('Done!')")
    
    print("\nHow many times will the loop execute?")
    print("A) 2 times")
    print("B) 3 times")
    print("C) 4 times")
    print("D) 5 times")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "B", "The loop will execute once for each item in the friends list, which has 3 items"):
        score += 1
    total_questions += 1
    
    # Section 3: Loop Patterns
    print_section("Section 3: Loop Patterns")
    
    print("Given the code:\n")
    print("numbers = [3, 41, 12, 9, 74, 15]")
    print("count = 0")
    print("total = 0")
    print("for num in numbers:")
    print("    count = count + 1")
    print("    total = total + num")
    print("print('Count:', count)")
    print("print('Average:', total/count)")
    
    print("\nWhat will be the output?")
    print("A) Count: 6, Average: 25.67")
    print("B) Count: 5, Average: 27.8")
    print("C) Count: 6, Average: 27.8")
    print("D) Count: 5, Average: 25.67")
    
    answer = input("\nYour answer (A/B/C/D): ").upper()
    if check_answer(answer, "A", "The code counts 6 numbers and calculates their average (3+41+12+9+74+15)/6 = 25.67"):
        score += 1
    total_questions += 1
    
    # Final Score
    print_section("Quiz Complete!")
    print(f"Your score: {score}/{total_questions}")
    percentage = (score/total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("Excellent! You have a strong understanding of loops and iterations!")
    elif percentage >= 70:
        print("Good job! You understand the basics well.")
    else:
        print("Keep practicing! Loops are essential for processing data in Python.")

if __name__ == "__main__":
    print("Welcome to the Chapter 5 Loops and Iterations Quiz!")
    print("This quiz will test your understanding of while loops, for loops, and common loop patterns.")
    input("Press Enter to begin...")
    run_quiz() 