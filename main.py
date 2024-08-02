from menu import Menu
# from core_python import Weather
from weather_code import Weather

temperature_controller = Weather(directory="csv2")
display_message = Menu()
# temperature_controller =Weather()


def handle_choice(weather_data_type):
    print(display_message.menu_2nd())
    choice_2nd = input("Enter your choice (in the form of number): ")
    if choice_2nd == "1":
        print(temperature_controller.complete_data(weather_data_type))
    elif choice_2nd == "2":
        year = input("Enter year (1997 to 2011): ")
        month = input("Enter month name (e.g., Jan, Apr): ").title()
        print(temperature_controller.temp_specific_month(year, month))
    elif choice_2nd == "3":
        print(temperature_controller.max_min_total(weather_data_type))
    elif choice_2nd == "4":
        year = input("Enter year (1997 to 2011): ")
        month = input("Enter month name (e.g., Jan, Apr): ").title()
        print(temperature_controller.max_min_specific_month(year, month, weather_data_type))
    elif choice_2nd == "5":
        year = input("Enter year (1997 to 2011): ")
        month = input("Enter month name (e.g., Jan, Apr): ").title()
        month_num = input("Enter month number (e.g., 1 for January): ") # reason:
        day = input("Enter day (e.g., 1 for the first day of the month): ")
        print(temperature_controller.specific_date(year, month, month_num, day, weather_data_type))
        # TODO: will do this case
    else:
        print("Invalid input. Try again.")


while True:
    print(display_message.menu())
    choice = input("Enter your choice (in the form of number): ").title()
    if choice == "1":
        handle_choice("Max TemperatureC")
    elif choice == "2":
        handle_choice("Max Humidity")
    elif choice == "3":
        handle_choice("Dew PointC")
    elif choice == "Q":
        break
    else:
        print("Invalid input. Try again")
