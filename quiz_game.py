from questions import list_quiz


def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if list_quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in list_quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


def intro_message():
    """
    Introduces user to the list_quiz and rules, and takes an input from customer to start the quiz.
    Returns true when enter key is pressed.
    """
    print("Welcome to this Capital Cities of the Countries quiz!")
    print("Are you ready to test your knowledge about Capital Cities?")
    print("There are a total of 10 questions, you can skip a question anytime by typing 'skip'")
    input("Press enter to start the fun!")
    return True


intro = intro_message()
while True:
    score = 0
    for question in list_quiz:
        attempts = 3
        while attempts > 0:
            print(list_quiz[question]['question'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1


    break

if score == 10:
    print(f"You've got a perfect score of {score}!")
else:
    print(f"Your final score is {score}/10!\n\n")
print("Want to know the correct answers? Please see them below! ;)\n")
print_dictionary()
print("Thank you for participating!")
