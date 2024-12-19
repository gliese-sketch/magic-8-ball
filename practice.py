import random

questions = [
    "What is the meaning of life?",
    "Do you love me?",
    "Are you a robot?",
    "How do you feel about robots?",
    "What is the meaning of life?",
    "Is this a test?",
    "Am I a robot?",
]

fixex_question = questions[1]
random_question = random.randint(0, len(questions) - 1)

print(fixex_question)