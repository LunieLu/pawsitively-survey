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
    final_answers = []

    questions = [
        "Would you recommend us to friends",
        "How happy are you with the service provided",
        "How professional is Pawsitively Perfect",
        "Are the staff caring and attentive",
        "Have the team replied in a timely manner"
    ]
    # loop over each question
    for q in questions:
        # get_answer(0, 5, f"{q}? \n")
        # create variable, give it a value
        answer = get_answer(0, 5, f"{q}? \n")
        # append answer to final_answers list
        final_answers.append(answer)
        # done

    return final_answers


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
    # print(f"Thank you {owner(user['Name'])}!")
    print(f"Here are your final answers: {answer_list}")


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
