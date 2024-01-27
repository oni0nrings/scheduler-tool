import random
from collections import deque
from datetime import timedelta


def create_schedule(start_date, num_weeks, names):
    # Convert the names list to a deque for efficient popping
    names = deque(names)

    # Initialize the schedule as an empty dictionary
    schedule = {}

    # Iterate over the range of weeks in the quarter
    for i in range(num_weeks):
        # Calculate the start and end dates for the current week
        start = start_date + timedelta(weeks=i)
        end = start + timedelta(days=11) # end date is 11 days after start date (2 business weeks)

        # Assign a random name to the current week
        random.shuffle(names)
        person = names.popleft()

        # Assign the person to the current 2-week period
        schedule[(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))] = person

    return schedule
