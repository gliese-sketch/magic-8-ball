import random

name = "Bill Gates"
question = ""
answer = ""
    
questions_list = [
    "What is the meaning of life?",
    "Do you love me?",
    "Are you a robot?",
    "How do you feel about robots?",
    "What is AI?",
    "Who wrote the book 'The Hitchhiker's Guide to the Galaxy'?",
    "Who aims to be the first man on the moon?",
    "Who claims to be the most intelligent person in the world?",
    "Is Alexander the Great a woman?",
    "Is the moon made of cheese?",
]

answers_list = [
    "I don't know",
    "Yes",
    "Pretty sure",
    "No nada",
    "Go and ask Sam Harris",
]


question_index = random.randint(0, len(questions_list) - 1)
answer_index = random.randint(0, len(answers_list) - 1)

question = questions_list[question_index]
answer = answers_list[answer_index]

if name:
    print(f"{name} asks: {question}")
else:
    print(f"Question: {question}")

print(f"Answer: {answer}")