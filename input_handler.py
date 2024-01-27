import datetime


def get_fiscal_year_and_quarter():
    # Ask for the current fiscal year and quarter
    # Keep asking for the year until a valid value is entered
    while True:
        try:
            year = int(input("Enter the year: "))
            current_year = datetime.datetime.now().year
            if current_year <= year <= current_year + 10:
                break
            else:
                print("Invalid year. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

    # Keep asking for the quarter until a valid value is entered
    while True:
        try:
            quarter = int(input("Enter the quarter (1-4): "))
            if quarter in [1, 2, 3, 4]:
                break
            else:
                print("Invalid quarter. Please enter a value between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid quarter.")

    return year, quarter
