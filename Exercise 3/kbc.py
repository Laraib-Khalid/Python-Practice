data = [
        {
            "question":"What is the capital of Pakistan?",
            "options":{"A":"Islamabad", "B":"Karachi", "C":"Lahore", "D":"Peshawar"},
            "answer":"A"
        },
        {
            "question": "Which language is this quiz written in?",
            "options": {"A": "C++", "B": "Python", "C": "Java", "D": "C#"},
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
            "answer": "C"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": {"A": "H2O", "B": "CO2", "C": "O2", "D": "NaCl"},
            "answer": "A"
        },
        {
            "question": "What is the largest animal on Earth?",
            "options": {"A": "Elephant", "B": "Giraffe", "C": "Blue Whale", "D": "Hippopotamus"},
            "answer": "C"
        },
        {
            "question": "What is the smallest planet in our solar system?",
            "options": {"A": "Mercury", "B": "Venus", "C": "Earth", "D": "Mars"},
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": {"A": "Au", "B": "Ag", "C": "Cu", "D": "Fe"},
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for sodium?",
            "options": {"A": "Na", "B": "K", "C": "Ca", "D": "Mg"},
            "answer": "A"
        },
        {
            "question": "What is the largest desert in the world?",
            "options": {"A": "Sahara", "B": "Arctic", "C": "Gobi", "D": "Kalahari"},
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for chlorine?",
            "options": {"A": "Cl", "B": "Br", "C": "I", "D": "F"},
            "answer": "A"
        },
        {
            "question": "What is the largest mammal on Earth?",
            "options": {"A": "Elephant", "B": "Giraffe", "C": "Blue Whale", "D": "Hippopotamus"},
            "answer": "C"
        }
    ]

# Money awarded for each correct answer
money_per_question = 1000
total_money = 0

# Function to display the question and options
def display_question(question,index):
    print(f"Question {index}: {question["question"]}")
    for option, value in question["options"].items():
        print(f"{option}: {value}")

# Function to check the answer
def check_answer(user_answer, correct_answer):
    return user_answer.upper() == correct_answer.upper()

# Main game loop
# for question in data:
#     display_question(question)
for i, question in enumerate(data, start=1):
    display_question(question, i)
    user_answer = input("Enter your answer (A, B, C, or D): ")
    if check_answer(user_answer, question["answer"]):
        print("Correct!")
        total_money += money_per_question
        print(f"You have won: {total_money}")
    else:
        print("Wrong answer!")
        print("Correct answer is: ", question["answer"])
        break

print(f"Game Over! You have won: {total_money}")
