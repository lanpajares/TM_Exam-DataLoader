""" Data Loader 

This script accepts file in CSV format, cleans up data to be ingested  and loads it to sqlite database.
This script requires that 'sqlite3', `pandas` be installed within the Python
environment you are running this script in.


Script assumes that the csv file has 4 columns with the following data types:
user (Text)
timestamp (Text)
hours (Float)
Project (Text) 

"""

import pandas as pd
import sqlite3


def remove_non_ascii(text):
    # function to remove non-ASCII (ranged)
    # takes data_frame[column] (ex: timestamp) and apply below logic to each element
    # in the data_frame[column]
    return ''.join(i for i in text if ord(i) < 122)


# read csv file from file repository
check_in_file_path = 'files/dailycheckins_short.csv'
data_frame = pd.read_csv(check_in_file_path)

# Data Frame Cleanup
# remove duplicates, drop columns with null values
data_frame.dropna(inplace = True)
data_frame.drop_duplicates(inplace=True)

# Cleanup User: replace all non-alpha numeric characters using \W regex
# Capitalize user names
data_frame['user'] = data_frame['user'].replace(r'\W', "", regex=True)
data_frame['user'] = data_frame['user'].str.capitalize()

# Cleanup Timestamp : remove non ascii characters
# Convert string Date time into Python Date time object.
data_frame['timestamp'] = data_frame['timestamp'].apply(remove_non_ascii)
data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'], utc=True, errors='coerce')

# Cleanup Hours:
#data_frame['hours'] = data_frame['hours'].apply(remove_non_ascii)
data_frame['hours'] = data_frame['hours'].replace(r'\W', "", regex=True)

# Cleanup Project
data_frame['project'] = data_frame['project'].str.capitalize()
data_frame['project'] = data_frame['project'].apply(remove_non_ascii)

# Write to separate cleaned csv
dataTypeSeries = data_frame.dtypes
print(dataTypeSeries)
data_frame.to_csv('files/dailycheckins_short_cleaned.csv')

# establish connection to the previously created database
conn = sqlite3.connect('checkins.db')

# create a cursor
c = conn.cursor()

# Initialize table
c.execute("""CREATE TABLE IF NOT EXISTS checkins (
    user text,
    timestamp text,
    hours integer,
    project text
)""")

data_frame.to_sql("checkins", conn, if_exists="append")
c.execute("SELECT * FROM checkins")
#print(c.fetchall())

print("command executed successfully...")

# commit our command
conn.commit()

# close our connection
conn.close()