questions = [
    {
        "prompt":"What is the capital of France?",
        "options":["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer":"A"
    },
    {
        "prompt":"Which language is primarily spoken in Brazil?",
        "options":["A. Spanish", "B. Portugese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt":"What is th smallest prime number?",
        "options":["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer":"B"
    },
    {
        "prompt":"Who wrote 'To Kill a Mockingbird'?",
        "options":["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. O2", "D. H2SO4"],
        "answer": "A"
    },
    {
        "prompt": "Which is the smallest continent by land area?",
        "options": ["A. Europe", "B. Australia", "C. South America", "D. Antarctica"],
        "answer": "B"
    },
    {
        "prompt": "What year did World War II end?",
        "options": ["A. 1945", "B. 1939", "C. 1942", "D. 1950"],
        "answer": "A"
    },
    {
        "prompt": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Seoul", "C. Tokyo", "D. Bangkok"],
        "answer": "C"
    },
    {
        "prompt": "What is the square root of 81?",
        "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "C"
    },
    {
        "prompt": "Who discovered penicillin?",
        "options": ["A. Marie Curie", "B. Alexander Fleming", "C. Isaac Newton", "D. Louis Pasteur"],
        "answer": "B"
    },
    {
        "prompt": "What is the largest mammal in the world?",
        "options": ["A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Orca"],
        "answer": "B"
    }
]

def run_quiz(questions):
    score = 0
    life = 3
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C OR D): ").upper()
        if answer == question["answer"]:
            print("Correct answer, Hoorraayyyy!!!\n")
            score += 1
            print("score", score)
            print("life", life)
        else:
            print(f"Wrong answer, BAD LUCK!!!, The correct answer was {question["answer"]}", "\n")
            life -= 1
            print("score", score)
            print("life", life)
            if life == 0:
                break
    
    print(f"You got {score} out of {len(questions)} questions correct.")


run_quiz(questions)