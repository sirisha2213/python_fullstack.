def run_quiz():
    # 1. Define your questions, options, and the correct answer
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"
        },
        {
            "question": "Which programming language is known as the 'snake' language?",
            "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
            "answer": "C"
        }
    ]

    score = 0

    print("--- Welcome to the Mini Quiz! ---\n")

    # 2. Loop through the questions
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # 3. Get user input and validate
        guess = input("Your answer (A, B, C, or D): ").strip().upper()

        if guess == q['answer']:
            print("Correct! ✨\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # 4. Show the final result
    print("--- Quiz Finished ---")
    print(f"Your final score is: {score}/{len(questions)}")
    
    if score == len(questions):
        print("Perfect score! You're a genius.")
    elif score > 0:
        print("Good job! You passed.")
    else:
        print("Better luck next time!")

