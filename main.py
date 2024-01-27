import csv
import os
import sys

from date_calculator import (
    adjust_start_date,
    calculate_num_weeks,
    get_quarter_start_end_dates,
)
from input_handler import get_fiscal_year_and_quarter
from scheduler import create_schedule

directory = os.path.dirname(os.path.realpath(sys.argv[0]))

# Prompt user for the year and quarter
year, quarter = get_fiscal_year_and_quarter()

# Calculate the start and end dates for the current quarter
start_date, end_date = get_quarter_start_end_dates(year, quarter)

# Adjust the start date to the next Monday if it's not already Monday
start_date = adjust_start_date(start_date)

# Calculate the number of business weeks (Monday through Friday) in the current quarter
num_weeks = calculate_num_weeks(start_date, end_date)

# Read names from a file, assuming one name per line
try:
    with open("names.txt", "r") as f:
        names = [line.strip() for line in f.readlines()]
    # Check if names is None or empty
    if not names:
        raise ValueError("The names list is empty. Please provide a list of names.")
except FileNotFoundError:
    print(
        "The file names.txt file was not found. Check the path variable and filename."
    )
    exit(1)
except IOError:
    print("There was an error reading the names.txt file.")
    exit(1)

# Create the schedule
schedule = create_schedule(start_date, num_weeks, names)

# Write the schedule to a .csv file
# Construct the filename
filename = os.path.join(directory, f"FY{year}Q{quarter}.csv")

# Save the schedule to the file and print it to the console
with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Start", "End", "Name"])  # write the header
    for (start, end), person in schedule.items():
        line = f"{start},{end},{person}"
        f.write(line + "\n")
        print(line)
    # Calculate the set of names that didn't make it onto the schedule
    not_assigned = set(names) - set(person for (start, end), person in schedule.items())
    if not_assigned:
        print(
            f"The following names didn't make it onto the schedule: {', '.join(not_assigned)}"
        )
    else:
        print("Everyone made it onto the schedule this round!")
