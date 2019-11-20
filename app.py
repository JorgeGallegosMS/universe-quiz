mult_choice = "Please enter a-e as an answer"
num_response = "Please enter a number"
true_or_false = "Please enter 1 for true and 0 for false"

questions_wrong = []

total_score = 0

def correct_answer():
    global total_score
    total_score += 1
    print("Correct!")

def wrong_answer(question_number, answer):
    questions_wrong.append(str(question_number))
    print(f"Incorrect. Correct answer: {answer}")

def question1():
    question = "How many minutes do sun rays take to reach earth?"
    answer = 8

    print(f"{question} {num_response}")

    guess = int(input())

    if guess == answer:
        correct_answer()
    else:
        wrong_answer(1, answer)

def question2():
    question = "How many days does it take for the moon to orbit Earth?"
    answer = 27

    print(f"{question} {num_response}")

    guess = int(input())

    if guess == answer:
        correct_answer()
    else:
        wrong_answer(2, answer)

question1()
question2()

print(questions_wrong)
print(total_score)