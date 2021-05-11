calc_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):

    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}")
    elif num_of_days == 0:
        return (f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}, but you probably already knew that! Please enter a valid positive number")
    else:
        return ("incorrect value, please enter value that is greater than zero")


def validate_input():
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You have entered 0, please enter a positive number")
        else:
            print(
                f"{user_input} is not a valid input, please enter a valid number")
    except ValueError:
        print("Your input is not a valid number, please don't ruin my program")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey user, enter a number of days as a comma (+space) seperated list and I will convert it to hours!\n"
    )
    list_of_days = user_input.split(", ")

    for num_of_days in set(list_of_days):
        validate_input()
