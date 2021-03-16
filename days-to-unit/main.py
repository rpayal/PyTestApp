from helper import validate_and_execute, USER_INPUT_MESSAGE

print("Welcome to my Python app.")

user_input = ""
while user_input != "exit":
    user_input = input(USER_INPUT_MESSAGE)
    if user_input != "exit":
        days_and_unit = user_input.split(":")
        print(days_and_unit)
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        for num_of_days_element in set(days_and_unit_dictionary.get("days").split(", ")):
            validate_and_execute(num_of_days_element, days_and_unit_dictionary.get('unit'))

exit()
