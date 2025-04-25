# Temperature Data Analysis for HIT137 Assignment 2 - Question 2
# This script processes CSV temperature files and produces three reports:
# 1. Seasonal average temperatures
# 2. Station with the largest temperature range
# 3. Warmest and coolest stations based on average temperature

import os
import pandas as pd

# Define the folder where CSV files are located
csv_folder = "temperature_data"  # Make sure this folder contains all the station_group_*.csv files

# Define the months of the year (used later for processing)
months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Group months into seasons according to the Australian classification
seasons = {
    'Summer': ['December', 'January', 'February'],
    'Autumn': ['March', 'April', 'May'],
    'Winter': ['June', 'July', 'August'],
    'Spring': ['September', 'October', 'November']
}

# Read all CSV files from the folder and combine them into one big DataFrame
all_dataframes = []
for filename in os.listdir(csv_folder):
    if filename.endswith(".csv"):
        path = os.path.join(csv_folder, filename)
        data = pd.read_csv(path)
        data['source_file'] = filename  # Keep track of source file
        all_dataframes.append(data)

# Combine all yearly data into a single DataFrame
df = pd.concat(all_dataframes, ignore_index=True)

# --- Task 1: Calculate average temperatures for each season ---

# Convert wide format (columns for each month) to long format
long_df = df.melt(
    id_vars=['STATION_NAME', 'STN_ID', 'LAT', 'LON'],
    value_vars=months,
    var_name='Month',
    value_name='Temperature'
)

# Calculate and save average temperatures by season
with open("average_temp.txt", "w") as f:
    f.write("Average Temperatures by Season (°C):\n")
    for season, season_months in seasons.items():
        season_data = long_df[long_df['Month'].isin(season_months)]
        season_avg = season_data['Temperature'].mean()
        f.write(f"{season}: {round(season_avg, 2)}\n")

# --- Task 2: Find station(s) with the largest temperature range ---

# Add max, min and range of temperatures for each station
df['Max_Temp'] = df[months].max(axis=1)
df['Min_Temp'] = df[months].min(axis=1)
df['Range_Temp'] = df['Max_Temp'] - df['Min_Temp']

# Find the maximum range
max_range_value = df['Range_Temp'].max()

# Filter all stations that have this max range
stations_with_max_range = df[df['Range_Temp'] == max_range_value]

# Save to file
with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"Station(s) with the Largest Temperature Range ({round(max_range_value, 2)}°C):\n\n")
    for _, row in stations_with_max_range.iterrows():
        f.write(f"{row['STATION_NAME']} (ID: {int(row['STN_ID'])})\n")

# --- Task 3: Find warmest and coolest stations ---

# Calculate average temperature for each station
df['Average_Temp'] = df[months].mean(axis=1)

# Identify the highest and lowest averages
max_avg = df['Average_Temp'].max()
min_avg = df['Average_Temp'].min()

warmest_stations = df[df['Average_Temp'] == max_avg]
coolest_stations = df[df['Average_Temp'] == min_avg]

# Write to file
with open("warmest_and_coolest_station.txt", "w") as f:
    f.write(f"Warmest Station(s) with Avg Temp {round(max_avg, 2)}°C:\n")
    for _, row in warmest_stations.iterrows():
        f.write(f"{row['STATION_NAME']} (ID: {int(row['STN_ID'])})\n")
    
    f.write(f"\nCoolest Station(s) with Avg Temp {round(min_avg, 2)}°C:\n")
    for _, row in coolest_stations.iterrows():
        f.write(f"{row['STATION_NAME']} (ID: {int(row['STN_ID'])})\n")
