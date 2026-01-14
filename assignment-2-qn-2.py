"""
Group Name: SYDNEY-35 (SYD-35)
Authors: Roshan Lamichhane (S399178),Shrijan Neupane (S398335)

Group Members:
Roshan Lamichhane - S399178
Ekraj Ghimire - S398831
Sudip Sunar - S398629
Shrijan Neupane - S398335

#######################
Question 2

Create a program that analyses temperature data collected from multiple weather stations in Australia.
The data is stored in multiple CSV files under a "temperatures" folder, with each file representing data from one year.
Process ALL .csv files in the temperatures folder. Ignore missing temperature values (NaN) in calculations.

Main Functions to Implement:
Seasonal Average: Calculate the average temperature for each season across ALL stations and ALL years. Save the results to "average_temp.txt".
- Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (Jun- Aug), Spring (Sep-Nov)
- Output format example: "Summer: 28.5°C"

Temperature Range: Find the station(s) with the largest temperature range (difference between the highest and lowest temperature ever recorded at that station). Save the
results to "largest_temp_range_station.txt".
- Output format example: "Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)"
- If multiple stations tie, list all of them

Temperature Stability: Find which station(s) have the most stable temperatures (smallest standard deviation) and which have the most variable temperatures (largest
standard deviation). Save the results to "temperature_stability_stations.txt".
Output format example:
- "Most Stable: Station XYZ: StdDev 2.3°C"
- "Most Variable: Station DEF: StdDev 12.8°C"
- If multiple stations tie, list all of them


#######################
References:
- https://docs.python.org/3/library/os.html#os.listdir
"""

import os
import math

# Australian seasons and their respective months
AUS_SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"],
}

# Map month to its season
MONTHS_TO_SEASON = {
    "December": "Summer",
    "January": "Summer",
    "February": "Summer",
    "March": "Autumn",
    "April": "Autumn",
    "May": "Autumn",
    "June": "Winter",
    "July": "Winter",
    "August": "Winter",
    "September": "Spring",
    "October": "Spring",
    "November": "Spring",
}

# months of a year
YEAR_MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Directory where the temperature csv files are stored
TEMPERATURE_DIR = "temperatures"


def read_temperature_files():
    """read csv files containing temperature data and return as list of map/dict"""

    all_data = []
    # list all files under the temperature directory
    files = os.listdir(TEMPERATURE_DIR)

    # same headers in all csv files
    headers_csv = ["STATION_NAME", "STN_ID", "LAT", "LON", *YEAR_MONTHS]

    # read each file in the temperature directory
    for file in files:
        with open(f"{TEMPERATURE_DIR}/{file}", "r") as f:
            # skip the first line, that is, header

            for row in f.readlines()[1:]:
                # split by commas as csv = comma separated values
                row = row.strip().split(",")

                # append a dict containing zip of each header key with its value in all_data list
                all_data.append(dict(zip(headers_csv, row)))

    return all_data


### Main Program
