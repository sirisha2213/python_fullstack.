def run_quiz():
    # 1. Database of 10 Questions
    questions = [
        {"q": "What is the capital of Japan?", "o": ["A) Seoul", "B) Tokyo", "C) Beijing", "D) Bangkok"], "a": "B"},
        {"q": "Which element has the chemical symbol 'O'?", "o": ["A) Gold", "B) Oxygen", "C) Osmium", "D) Helium"], "a": "B"},
        {"q": "How many continents are there on Earth?", "o": ["A) 5", "B) 6", "C) 7", "D) 8"], "a": "C"},
        {"q": "What is the largest mammal in the world?", "o": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Shark"], "a": "B"},
        {"q": "Who wrote 'Romeo and Juliet'?", "o": ["A) Mark Twain", "B) Jane Austen", "C) William Shakespeare", "D) Charles Dickens"], "a": "C"},
        {"q": "What is the square root of 64?", "o": ["A) 6", "B) 7", "C) 8", "D) 9"], "a": "C"},
        {"q": "Which planet is closest to the Sun?", "o": ["A) Venus", "B) Earth", "C) Mars", "D) Mercury"], "a": "D"},
        {"q": "What does CPU stand for?", "o": ["A) Central Process Unit", "B) Computer Personal Unit", "C) Central Processing Unit", "D) Central Processor Utility"], "a": "C"},
        {"q": "In which year did the Titanic sink?", "o": ["A) 1912", "B) 1905", "C) 1920", "D) 1898"], "a": "A"},
        {"q": "What is the hardest natural substance on Earth?", "o": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"], "a": "C"}
    ]

    score = 0
    total = len(questions)

    print("STARTING THE ULTIMATE 10-QUESTION QUIZ ")
    print("--------------------------------------------")

    for i, item in enumerate(questions):
        print(f"\nQuestion {i+1} of {total}:")
        print(item["q"])
        for option in item["o"]:
            print(option)
        
        
        guess = input("Your answer (A, B, C, or D): ").strip().upper()

        
        if guess == item["a"]:
            print(" CORRECT!")
            score += 1
        else:
            print(f" WRONG. The correct answer was {item['a']}.")


    
    
    print("       QUIZ COMPLETED!       ")
    print("="*30)
    print(f"Final Score: {score}/{total}")
    

    if score == len(questions):
        print("Rank:  perfect score")
    elif score > 6:
        print("Rank:  good keep going")
    else:
        print("Rank:  need to work hard !")

if __name__ == "__main__":
    run_quiz()
    

