def owner_data():
    """
    Get owner's information input from user.
    """
    print("Please tell us your name.")
    owner_data.owner = input("Name: \n")
    print("Please tell us your pet name.")
    owner_data.pet = input("Pet name: \n")


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
        get_answer(0, 5, f"{q}?")
    

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


def get_answer(min, max, prompt):
    """
    Will check if values are equal to or between 0-5.
    Raises ValueError if incorrect data has been input.
    """
    while True:
        answer = input(prompt)
        print(answer)
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
    owner_data()
    feedback()
    print(f"Thank you {owner_data.owner}!")
    print("We appreciate you taking the time to complete our survey.")
    print(f"We hope you and {owner_data.pet} have a great day.")


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
