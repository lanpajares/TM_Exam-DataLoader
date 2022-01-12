# TM_Exam-DataLoader
Deliverables for Support Engineer Exam

### Scripts
- dataLoader
- webService

#### Data Loader 

This script accepts file in CSV format, cleans up data to be ingested  and loads it to sqlite database.
This script requires that 'sqlite3', `pandas` be installed within the Python
environment you are running this script in.


Script assumes that the csv file has 4 columns with the following data types:
user (Text)
'''timestamp (Text)
hours (Float)
Project (Text) 
'''

#### Web Service

DataLoader Web Service

This script connects to local "checkins" database created by data loader script.
This script requires that 'sqlite3', `flask's Flask, request and jsonify',  be installed within the Python
environment you are running this script in.

Script has two functions for querying data
1. Checkins : displays all data of all users from chekins db
---- parameter: none
2. Checkins_single_user: Displays all data of a specific user from checkins db
---- Parameter: user (string)

Returns
On Success : 200
On Failure: 500


