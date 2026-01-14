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

def get_total_years():
    """get the total files within the temperatures directory"""
    # list all files under the temperature directory
    files = os.listdir(TEMPERATURE_DIR)
    # get the length of list
    total = len(files)

    return total


def is_valid_temperature(val):
    """check if provided temperature  is valid."""
    if val == "" or val.lower() == "nan":
        return False
    try:
        float(val)
        return True
    except ValueError:
        return False


def compute_avg_season_temperature(all_data):
    """compute average seasonal temperature data"""

    # total temperature in each seasons
    seasons = dict()
    # total number of each seasons
    seasons_count = dict()

    # Add entry for each season
    for s in AUS_SEASONS:
        seasons[s] = 0
        seasons_count[s] = 0

    # process each entry in the data
    # process each entry - each location -> each month (map to corressponding season)
    for row in all_data:
        # go through each months in a row
        for month in YEAR_MONTHS:
            # get the season based on month
            season_value = MONTHS_TO_SEASON[month]

            # get temperature of the current month
            temperature = row[month]

            # increment the count of season
            seasons_count[season_value] += 1

            # check if temperature is valid
            if is_valid_temperature(temperature):
                seasons[season_value] += float(temperature)

    # now compute average for seasons
    for s in AUS_SEASONS:
        seasons[s] /= seasons_count[s]

    return seasons

def compute_largest_temp_range(all_data):
    """compute the station with largest temperature range"""

    max_range = 0
    max_range_stations = []
    ranges_station = []

    # Loop through each entry
    for station in all_data:
        temperatures = []

        # go through all months of a year
        for month in YEAR_MONTHS:
            if month in station:
                # get the temperature for the month
                tempe_value = station[month]
                if is_valid_temperature(tempe_value):
                    temperatures.append(float(tempe_value))

        if temperatures:
            # compute the max gap between largest and lowest temperature
            max_temp = max(temperatures)
            min_temp = min(temperatures)
            tempe_range = max_temp - min_temp
            ranges_station.append(
                (station["STATION_NAME"], tempe_range, max_temp, min_temp)
            )

            # Set the max range if found
            if tempe_range > max_range:
                max_range = tempe_range

    # Filter the stations with max range
    for station in ranges_station:
        if station[1] == max_range:
            max_range_stations.append(station)

    return max_range_stations


def compute_stable_temp_range(all_data):
    """compute the station with largest and lowest standard deviation in temperature range"""

    max_deviation = 0
    min_deviation = 0
    is_initial = True  # for initial deviation comparision

    # store stations with highest deviation (most variable)
    high_deviation_stations = []

    # store stations with lowest deviation (most stable)
    low_deviation_stations = []

    # each station with their individual deviation value
    ranges_station = []

    # Loop through each entry
    for station in all_data:
        temperatures = []
        tempe_sum = 0

        # go through all months of a year
        for month in YEAR_MONTHS:
            if month in station:
                # get the temperature for the month
                tempe_value = station[month]
                if is_valid_temperature(tempe_value):
                    val = float(tempe_value)
                    # append to temperatures list
                    temperatures.append(val)
                    # add to sum
                    tempe_sum += val

        if temperatures:
            # total number of temperatures
            total_size = len(temperatures)
            # Mean of all temperatures in list
            mean_val = tempe_sum / total_size

            total_squared_diff = 0

            # sum of  (Xi - Mean) ^ 2, where i = index
            for t in temperatures:
                total_squared_diff += (t - mean_val) ** 2

            # compute the standard deviation
            deviation = math.sqrt((1 / total_size) * total_squared_diff)

            ranges_station.append((station["STATION_NAME"], deviation))

            # Set the max deviation if needed
            if deviation > max_deviation:
                max_deviation = deviation

            # set the min deviation value if needed
            if is_initial:
                min_deviation = deviation
            else:
                if deviation < min_deviation:
                    min_deviation = deviation

    # Filter the stations with highest deviation (less stable)
    for station in ranges_station:
        if station[1] == max_deviation:
            high_deviation_stations.append(station)

    # Filter the stations with lowest deviation (most stable)
    for station in ranges_station:
        if station[1] == min_deviation:
            low_deviation_stations.append(station)

    return high_deviation_stations, low_deviation_stations


### Main Program


try:
    # read all temperature data
    data = read_temperature_files()

    # Get the average seasonal temperature values
    avg_season_temperature = compute_avg_season_temperature(data)

    # Get max range of temperatures
    max_range_stations = compute_largest_temp_range(data)

    # Write to largest_temp_range_station.txt file
    with open("largest_temp_range_station.txt", "w") as file:
        for station in max_range_stations:
            file.write(f"Station {station[0]}: Range {station[1]:.2f}°C (Max: {station[2]:.2f}°C, Min: {station[3]:.2f}°C)\n")


    # Get stable and variable stations
    low_stable_stations, most_stable_stations = compute_stable_temp_range(data)
    with open("temperature_stability_stations.txt", "w") as file:
        # for stable
        for station in most_stable_stations:
            file.write(f"Most Stable: Station {station[0]}: StdDev {station[1]:.2f}°C\n")
        # for variable stations
        for station in low_stable_stations:
            file.write(f"Most Variable: Station {station[0]}: StdDev {station[1]:.2f}°C\n")

except Exception as e:
    print("Something went wrong.", e)
