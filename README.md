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
'''
user (Text)
timestamp (Text)
hours (Float)
Project (Text) 
'''

This script extensively uses Pandas library for:
- file read/write
- data extraction/manipulation

The script uses sqlite to: 
- create db
- establish/end connection to database 
querying data 

The script generates/writes to a csv file the cleaned version of the ingested data. 

#### Web Service

DataLoader Web Service

This script connects to local "checkins" database created by data loader script.
This script requires that 'sqlite3', `flask's Flask, request and jsonify',  be installed within the Python
environment you are running this script in.

Script has two functions for querying data
1. Checkins : displays all data of all users from chekins db
  - Parameter: none
2. Checkins_single_user: Displays all data of a specific user from checkins db
  - Parameter: user (string)

Returns
On Success:
--200
On Failure:
--500


#### ETL Data Flow Process
1. Run dataloader.py 
2. Run webservices.py
- data can be visualized by sending requests via postman or via browser url 
