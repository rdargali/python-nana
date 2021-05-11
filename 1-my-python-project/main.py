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
        user_input_number = int(user_input)
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
        "Hey user, enter a number of days and I will convert it to hours!\n"
    )
    validate_input()

# ---SCOPE---
# def scope_check(parameter_internal_var):
#     my_var = "my variable"
#     print(name_of_unit)  # global variable
#     print(parameter_internal_var)  # local variable as parameter
#     print(my_var)  # local variable created inside function

# scope_check("hello")
