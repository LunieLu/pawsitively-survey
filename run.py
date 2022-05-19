from datetime import date


def owner():
    """
    Will ask user for their name and pet name.
    Saves information into a dictionary.
    Information will be called at end of survey.
    """
    owner_data = ['Name', 'Pet Name']
    user_input = ''
    owner.user = dict.fromkeys(owner_data, user_input)
    owner.user['Name'] = input("Please tell us your name: \n")
    owner.user['Pet Name'] = input("Please tell us your pet's name: \n")


def feedback():
    """
    Feedback input from user.
    User chooses an input 0-5, which must be integers.
    The loop will repeat if user enters an invalid input.
    """
    feedback.final_answers = []

    questions = [
        "Would you recommend us to friends",
        "How happy are you with the service provided",
        "How professional is Pawsitively Perfect",
        "Are the staff caring and attentive",
        "Have the team replied in a timely manner"
    ]

    for question in questions:
        answer = get_answer(0, 5, f"{question}? \n")
        feedback.final_answers.append(answer)
    return feedback.final_answers


def get_answer(low, high, prompt):
    """
    Will check if values are equal to or between 0-5.
    Raises ValueError if incorrect data has been input.
    """
    while True:
        answer = input(prompt "\n")
        if answer.isnumeric():
            if low <= int(answer) <= high:
                return int(answer)
            else:
                print("Number not between 0-5")
        else:
            print("This is not a number, please try again.")


def confirm():
    """
    Checks if user is happy with input by confirming y/n.
    If y, survey ends.
    If n, loops back to questions.
    If neither, provides error and repeats y/n question.
    """
    user_confirm = input("Are you happy with your answers? y/n: \n")
    if user_confirm == "y":
        print("Thank you!")
        print(f"Hope you and {owner.user['Pet Name']} have a lovely day!")
    elif user_confirm == "n":
        main_repeated()
    else:
        print("Please answer y or n.")
        confirm()


def main():
    """
    Run all program functions
    """
    owner()
    now = date.today()
    today = now.strftime("%d/%m/%Y")
    print("Today's date is:", today)
    print("Please answer the below questions.")
    print("Your answer should be a figure between 0-5")
    print("0 = Thoroughly disagree; 5 = Very much agree.\n")
    feedback()
    print(f"Thank you {owner.user['Name']}!")
    print(f"Here are your final answers: {feedback.final_answers}")
    confirm()


def main_repeated():
    """
    Repeats all program functions
    """
    print("Please answer the below questions.")
    print("Your answer should be a figure between 0-5")
    print("0 = Thoroughly disagree; 5 = Very much agree.\n")
    feedback()
    print(f"Thank you {owner.user['Name']}!")
    print(f"Here are your final answers: {feedback.final_answers}")
    confirm()


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
