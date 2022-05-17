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
    print("0 = Awful; 5 = Absolutely fantastic.\n")

    print("1. Would you recommend Pawsitively Perfect to friends?")
    data_1 = input("Enter answer here:\n")

feedback()

def main():
    """
    Run all program functions
    """
    owner_data()


print("Thank you for choosing Pawsitively Perfect Pet Care.")
print("We would love to hear your feedback about our services.")
main()
