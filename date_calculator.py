from datetime import datetime, timedelta


def get_quarter_start_end_dates(year, quarter):
    # Fiscal year quarters start dates
    quarters_start_dates = [(11, 1), (2, 1), (5, 1), (8, 1)]

    # Calculate the start and end dates for the current quarter
    start_date = datetime(year if quarter > 1 else year - 1, *quarters_start_dates[quarter - 1])
    end_date = datetime(year if quarter < 4 else year + 1, *quarters_start_dates[quarter % 4]) - timedelta(days=1)

    return start_date, end_date


def adjust_start_date(start_date):
    # Calculate the number of days until the next Mon day
    days_until_monday = (7 - start_date.weekday()) % 7

    # Add the number of days until the next Monday to the start date
    start_date += timedelta(days=days_until_monday)

    return start_date


def calculate_num_weeks(start_date, end_date):
    # Calculate the number of business weeks (Monday through Friday) in the current quarter
    num_weeks = (end_date - start_date).days // 7 + 1

    return num_weeks
