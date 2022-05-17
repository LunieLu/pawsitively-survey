def owner_data():
    """
    Get owner's information input from user.
    """
    print("Please tell us your name.")
    owner = input("Name: \n")
    print("Please tell us your pet name.")
    pet = input("Pet name: \n")


def feedback():
    """
    Feedback input from user.
    User chooses an input 0-5, which must be integers.
    The loop will repeat if user enters an invalid input.
    """
    print("Please answer the below questions.")
    print("Your answer should be a figure between 0-5")
    print("0 = Thoroughly disagree; 5 = Very much agree.\n")

    print("1. Would you recommend Pawsitively Perfect to friends?")
    data_1 = input("Enter answer here:\n")
    valid_answer(data_1)

    print("2. How happy are you with the service provided?")
    data_2 = input("Enter answer here: \n")
    valid_answer(data_2)

    print("3. How professional is Pawsitively Perfect Pet Care?")
    data_3 = input("Enter answer here: \n")
    valid_answer(data_3)

    print("4. Are the staff caring and attentive?")
    data_4 = input("Enter answer here: \n")
    valid_answer(data_4)

    print("5. Have the team replied in a timely manner?")
    data_5 = input("Enter answer here: \n")
    valid_answer(data_5)


def valid_answer(values):
    """
    Will check if values are equal to or between 0-5.
    Raises ValueError if incorrect data has been input.
    """
    try:
        if 0 <= int(values) <= 5:
            return values
        else:
            raise ValueError(
                f"Number not between 0-5"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

# def thank_you(owner_data):
#     print(f"Thank you {owner} for completing the survey.")
#     print(f"We hope you and {pet} have a great day!")


def main():
    """
    Run all program functions
    """
    owner_data()
    feedback()


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
