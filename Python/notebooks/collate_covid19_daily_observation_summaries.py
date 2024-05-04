"""
Combines files containing daily summaries of COVID-19 data.
"""

import glob
from os import path
import re
from typing import List

DIR = "csse_covid_19_daily_reports"
DAILY_DATA = "daily_observations.csv"

def load_dates() -> List[str]:
    """Returns all the days for which we have data."""
    pattern = r"(\d{2}-\d{2}-\d{4}).csv"
    src = "{}/*.csv".format(DIR)
    dates = [re.findall(pattern, f)[0] for f in glob.glob(src) if re.search(pattern, f)]
    dates.sort()
    return dates

def source_path(date: str) -> str:
    """Constructs file path from date."""
    return "{}/{}.csv".format(DIR, date)

def create_collated_daily_data():
    """Creates single file containing all data from combined daily data files."""
    with open(DAILY_DATA, 'w') as writer:
        writer.write("Date,Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered\n")
        for date in load_dates():
            file = source_path(date)
            has_newline = True
            with open(file) as reader:
                next(reader) # Skip header
                for line in reader:
                    line = "{},{}".format(date, line) # Prepend to line
                    writer.write(line)
                    has_newline = line.endswith("\n")
            if not has_newline:
                writer.write("\n")

if not path.exists(DAILY_DATA):
    create_collated_daily_data()
    print("Created file: {}".format(DAILY_DATA))
else:
    print("File already exists: {}".format(DAILY_DATA))
