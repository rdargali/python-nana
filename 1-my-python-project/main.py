calc_to_units = 24
name_of_unit = "hours"

print(f"30 days are {30 * calc_to_units} {name_of_unit}")
print(f"35 days are {35 * calc_to_units} {name_of_unit}")
print(f"80 days are {80 * calc_to_units} {name_of_unit}")
print(f"120 days are {120 * calc_to_units} {name_of_unit}")


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calc_to_units} {name_of_unit}")
    print(custom_message)
    print("----------------------")


days_to_units(30, "that's awesome")

days_to_units(50, "no way")

days_to_units(80, "kowabunga")


def scope_check(parameter_internal_var):
    my_var = "my variable"
    print(name_of_unit)  # global variable
    print(parameter_internal_var)  # local variable as parameter
    print(my_var)  # local variable created inside function


scope_check("hello")
