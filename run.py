def owner():
    """
    Will ask user for their name and pet name.
    Saves information into a dictionary.
    Information will be called at end of survey.
    """
    owner_data = ['Name', 'Pet Name']
    user_input = ''
    user = dict.fromkeys(owner_data, user_input)
    user['Name'] = input("Please tell us your name: \n")
    user['Pet Name'] = input("Please tell us your pet's name: \n")


def feedback():
    """
    Feedback input from user.
    User chooses an input 0-5, which must be integers.
    The loop will repeat if user enters an invalid input.
    """
    print("Please answer the below questions.")
    print("Your answer should be a figure between 0-5")
    print("0 = Thoroughly disagree; 5 = Very much agree.\n")

    questions = [
        "Would you recommend us to friends",
        "How happy are you with the service provided",
        "How professional is Pawsitively Perfect",
        "Are the staff caring and attentive",
        "Have the team replied in a timely manner"
    ]

    for q in questions:
        get_answer(0, 5, f"{q}? \n")

    # data_1 = input("1. Would you recommend us to friends? \n")
    # while not valid_answer(data_1):
    #     data_1 = input("1. Would you recommend us to friends? \n")

    # data_2 = input("2. How happy are you with the service provided? \n")
    # while not valid_answer(data_2):
    #     data_2 = input("2. How happy are you with the service provided? \n")

    # data_3 = input("3. How professional is Pawsitively Perfect? \n")
    # while not valid_answer(data_3):
    #     data_3 = input("3. How professional is Pawsitively Perfect? \n")

    # data_4 = input("4. Are the staff caring and attentive? \n")
    # while not valid_answer(data_4):
    #     data_4 = input("4. Are the staff caring and attentive? \n")

    # data_5 = input("5. Have the team replied in a timely manner? \n")
    # while not valid_answer(data_5):
    #     data_5 = input("5. Have the team replied in a timely manner? \n")


def collect_data():
    """
    Get all of user's input and put into a list.
    List will then be called at the end of survey.
    User will be required to input y/n if data is correct.
    """
    get_answer = []
    final_answers =
    print(f"Your answers are: {final_answers}")


def get_answer(min, max, prompt):
    """
    Will check if values are equal to or between 0-5.
    Raises ValueError if incorrect data has been input.
    """
    while True:
        answer = input(prompt)
        if answer.isnumeric():
            if min <= int(answer) <= max:
                return int(answer)
            else:
                print("Number not between 0-5")
        else:
            print("This is not a number, please try again.")


def main():
    """
    Run all program functions
    """
    owner()
    feedback()
    print(f"Thank you {user['Name']}!")
    collect_data()


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
