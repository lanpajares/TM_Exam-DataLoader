""" DataLoader Web Service

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

"""


from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def db_connection():
# function to establish connection to the local chekins database
    conn = None
    try:
        conn = sqlite3.connect('checkins.db')
    except sqlite3.error as e:
        print(e)
    return conn


@app.route("/", methods=['GET'])
def welcome():
    return "Thank you for using Data Loader Web Service"

@app.route("/checkins", methods=["GET"])
def checkins():
    # function to display all data pf users from the database
    # Parameters
    # ----------
    # None
    #
    # Returns
    # -------
    # list
    #     a list of checkins of all users

    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT DISTINCT * FROM checkins")
        checkins_records = [
            dict(id=row[0], user=row[1],  timestamp=row[2],  hours=row[3],  project=row[4],)
            for row in cursor.fetchall()
        ]

        if checkins_records is not None:
            return jsonify(checkins_records), 200
        else:
            return "Something went Wrong", 500


@app.route("/checkins/single_user/<user>", methods=["GET", "POST"])
def checkins_single_user(user):
#function to query specific user to from the database
# Parameters
# ----------
# user : str
#     The name of the user to be queried
# Returns
# -------
# list
#     a list of unique checkins of specified user

    conn = db_connection()
    cursor = conn.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT DISTINCT * FROM checkins WHERE user=?", (user,))
        checkins_records = [
            dict(id=row[0], user=row[1],  timestamp=row[2],  hours=row[3],  project=row[4],)
            for row in cursor.fetchall()
        ]
        if checkins_records is not None:
            return jsonify(checkins_records), 200
        else:
            return "Something went Wrong", 500


if __name__== "__main__":
    app.run()

