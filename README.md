# scheduler-tool

This project is a Python script that generates a randomized schedule. The schedule is written to a .csv file, named based on the fiscal year and quarter provided by the user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x

### Installing

1. Clone the repository
```sh
git clone https://github.com/oni0nrings/scheduler-tool.git

2. Navigate to the project directory
```sh
cd schedule-generator```

3. Run the script
```sh
python main.py
```

## Usage

When you run the script, you will be prompted to enter the year and the quarter (1-4). The script will then generate a .csv file named FY{year}Q{quarter}.csv with the randomized names.

The names are read from a file named names.txt in the same directory, with one name per line.

Please note that if a file with the same name already exists, the script will not overwrite it and will exit instead.

## Dependencies

This script uses the built-in Python libraries csv, datetime, and os. It also uses a function randomize_names from the randomizer.py file in the same directory.
