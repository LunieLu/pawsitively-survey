from datetime import date


def main_menu(start, instructions, about):
    """
    Will explain to user the purpose of the app.
    """
    print("Welcome to Short Surveys!")
    print("Please choose one of the following options:")
    input("Start, Instructions or About: \n")
    start = "Start"
    instructions = "Instructions"
    about = "About"
    if not instructions or about:
        if start:
            print("Thank you for choosing Pawsitively Perfect Pet Care.")
            print("We would love to hear your feedback about our services.")
        else:
            return
    elif not start or about:
        if instructions:
            print("Instructions:")
            print("You will be shown 5 questions about Pawsitively Perfect.")
            print("Please answer these questions by typing in a number from 0 to 5")
            print("Numbers above 5 will give you an error.")
            print("Words will give you an error also")
            print("At the end of the survey, your answers will appear.")
            print("You will need to confirm if you're happy with them.")
    elif not start or instructions:
        if about:
            print("Our survey has been put together to:")
            print("- Find out how happy our customers are.")
            print("- See what our customers think of us.")
            print("- To help us improve our service.")
    else:
        print("Incorrect choice, please try again.")


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
        answer = input(prompt)
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
    print("Are you happy with your answers?")
    user_confirm = input("Please enter y for yes or n for no: \n")
    lower_confirm = user_confirm.lower()
    if lower_confirm == "y":
        print("Thank you!")
        print(f"Hope you and {owner.user['Pet Name']} have a lovely day!")
    elif lower_confirm == "n":
        main_repeated()
    else:
        print("Please answer y or n.")
        confirm()


def main():
    """
    Run all program functions
    """
    main_menu("Start", "Instructions", "About")
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


main()
