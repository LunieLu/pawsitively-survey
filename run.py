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

    data_1 = input("1. Would you recommend Pawsitively Perfect to friends? \n")
    while not valid_answer(data_1):
        data_1 = input("1. Would you recommend Pawsitively Perfect to friends? \n")

    data_2 = input("2. How happy are you with the service provided? \n")
    while not valid_answer(data_2):
        data_2 = input("2. How happy are you with the service provided? \n")        

    data_3 = input("3. How professional is Pawsitively Perfect Pet Care? \n")
    while not valid_answer(data_3):
        data_3 = input("3. How professional is Pawsitively Perfect Pet Care? \n")
    
    data_4 = input("4. Are the staff caring and attentive? \n")
    while not valid_answer(data_4):
        data_4 = input("4. Are the staff caring and attentive? \n")

    data_5 = input("5. Have the team replied in a timely manner? \n")
    while not valid_answer(data_5):
        data_5 = input("5. Have the team replied in a timely manner? \n")


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
        return False

    return True


def main():
    """
    Run all program functions
    """
    owner_data()
    feedback()
    print("Thank you for taking the time to complete the survey!")
    print("We hope you have a great day.")


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
