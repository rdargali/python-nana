calc_to_seconds = 24*60*60
name_of_unit = "seconds"

print(f"30 days are {30 * calc_to_seconds} {name_of_unit}")
# print(f"35 days are {35 * calc_to_seconds} {name_of_unit}")
# print(f"80 days are {80 * calc_to_seconds} {name_of_unit}")
# print(f"120 days are {120 * calc_to_seconds} {name_of_unit}")


def days_to_units(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calc_to_seconds} {name_of_unit}")


days_to_units(30)
