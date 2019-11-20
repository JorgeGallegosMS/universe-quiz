mult_choice = "Please enter a-d as an answer"
num_response = "Please enter a whole number"
true_or_false = "Please enter 1 for true and 0 for false"

questions_wrong = []

total_score = 0

def correct_answer():
    global total_score
    total_score += 1
    print("Correct!\n")

def wrong_answer(question_number, answer):
    questions_wrong.append(str(question_number))
    print(f"Incorrect. Correct answer: {answer}\n")

def question1():
    question = "1. How many minutes do sun rays take to reach earth?"
    answer = 8

    print(f"{question} {num_response}")

    guess = int(input())

    if guess == answer:
        correct_answer()
    else:
        wrong_answer(1, answer)

def question2():
    question = "2. How many days does it take for the moon to orbit Earth?"
    answer = 27

    print(f"{question} {num_response}")

    guess = int(input())

    if guess == answer:
        correct_answer()
    else:
        wrong_answer(2, answer)

def question3():
    question = "3. Which planet has the most volcanoes?"
    answer = "b"
    letters = ["a", "b", "c", "d"]
    choices = ["Earth", "Venus", "Jupiter", "Saturn"]

    print(f"{question} {mult_choice}")

    for index in range(len(choices)):
        print(f"{letters[index]} - {choices[index]}")

    guess = input().lower()

    if guess in letters:
        if guess == answer:
            correct_answer()
        else:
            wrong_answer(3, answer)
    else:
        print(f"{guess} is not a valid option. Try again\n")
        question3()

def question4():
    question = "4. What is the diameter of Earth?"
    answer = "c"
    letters = ["a", "b", "c", "d"]
    choices = ["3,144 miles", "9,227 miles", "7,918 miles", "4,916 miles"]

    print(f"{question} {mult_choice}")

    for index in range(len(choices)):
        print(f"{letters[index]} - {choices[index]}")

    guess = input().lower()

    if guess in letters:
        if guess == answer:
            correct_answer()
        else:
            wrong_answer(4, answer)
    else:
        print(f"{guess} is not a valid option. Try again\n")
        question4()

def quiz():
    question1()
    question2()
    question3()
    question4()

if __name__ == "__main__":
    quiz()

print(questions_wrong)
print(total_score)