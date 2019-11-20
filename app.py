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

def question5():
    question = "True or False: Jupiter is the largest planet in our solar system"
    answer = "1"

    print(f"{question} - {true_or_false}")

    guess = input()

    if guess == answer:
        correct_answer()
    else:
        wrong_answer(5, answer)

def question6():
    question = "True of False: There are 1 trillion stars in the Andromeda "
    answer = "1"

    print(f"{question} - {true_or_false}")

    guess = input()

    if guess == answer:
        correct_answer()
    else:
        wrong_answer(6, answer)

def summary():
    print("Quiz Summary:")
    print(f"You got {total_score}/6 answers right")
    print(f"Questions you got wrong: {', '.join(questions_wrong)}")
    if total_score <= 2:
        print("Nice try, but you can do better")
    elif total_score < 4:
        print("You seem to know a bit about the universe")
    else:
        print("You know the universe pretty well")

def universe_quiz():
    print("Quiz time! Let's test your knowledge of the universe\n")
    question1()
    question2()
    question3()
    question4()
    question5()
    question6()
    summary()

if __name__ == "__main__":
    universe_quiz()