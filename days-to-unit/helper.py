USER_INPUT_MESSAGE = "Hey !! Enter number of days as a comma separated list:unit of measurement (e.g 20, 30:hours) " \
                     "and I'll convert it for you.\n "


def days_to_hours(num_of_days, conversion_unit):
    calculation_factor = 0
    if conversion_unit == "hours":
        calculation_factor = 24
    elif conversion_unit == "minutes":
        calculation_factor = 24 * 60
    elif conversion_unit == "seconds":
        calculation_factor = 24 * 60 * 60
    else:
        return "Unsupported unit of measurement. Pls. pass either (hours/minutes/seconds)."
    return f"{num_of_days} days are {num_of_days * calculation_factor} {conversion_unit}"


def validate_and_execute(num_of_days, conversion_unit):
    try:
        user_input_number = int(num_of_days)
        if user_input_number > 0:
            calculated_value = days_to_hours(user_input_number, conversion_unit)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please provide a valid positive number.")
        else:
            print("You entered a negative number, no conversion for you.")
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program.")
