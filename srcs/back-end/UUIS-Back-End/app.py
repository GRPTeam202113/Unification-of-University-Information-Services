from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# This API is designed to return the corresponding information of
# a specific course that user choose
@app.route('/faculty/course', methods=["POST"])
def course():
    # User choose a specific course and post to back-end
    if request.method == "POST":
        coursename = request.json.get("coursename")

        # Open database and search the information of the course
        con = sqlite3.connect("UUIS_database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""SELECT Degree, Type, Duration, StartDate, Faculty, Model from UNNC_Course_Info where Name = ?""",
                    (coursename,))
        rows = cur.fetchall()

        # Create six dics to store the returned inforamtion
        coursedegree = []
        coursetype = []
        courseduration = []
        coursestartdate = []
        coursefaculty = []
        coursemodel = []
        try:
            for row in rows:
                coursedegree.append(row["Degree"])
                coursetype.append(row["Type"])
                courseduration.append(row["Duration"])
                coursestartdate.append(row["StartDate"])
                coursefaculty.append(row["Faculty"])
                coursemodel.append(row["Model"])
                return jsonify({'coursedegree': coursedegree, 'coursetype': coursetype, 'courseduration': courseduration,
                        'coursestartdate': coursestartdate, 'coursefaculty': coursefaculty, 'coursemodel': coursemodel})
        except:
                # When error happens, return the error information
                return print("Error Happened")


# This API is designed to return the corresponding modules of
# a specific course that user choose
@app.route('/faculty/course/module', methods=["POST"])
def courseinfo():
    # User choose a specific course and its faculty and post to back-end
    if request.method == "POST":
        facultyname = request.json.get("facultyname")
        coursename = request.json.get("coursename")

        # In the database, different faculties are stored in different tables, in FOSE and FOB
        # the program search the modules of the course according to the course name
        if facultyname == "FOSE" or facultyname == "FOB":
            con1 = sqlite3.connect("UUIS_database.db")
            con1.row_factory = sqlite3.Row
            cur1 = con1.cursor()
            cur1.execute("""SELECT LEVEL, CODE, NAME, PERIOD from UNNC_module_catalogue where Name IN (SELECT Name FROM UNNC_Course where Course = ?)""",(coursename,))
            rows = cur1.fetchall()

            # Create four dics to store the returned inforamtion
            modulelevels = []
            modulecodes = []
            modulenames = []
            moduleperiods = []
            try:
                for row in rows:
                    modulelevels.append(row["Level"])
                    modulecodes.append(row["Code"])
                    modulenames.append(row["Name"])
                    moduleperiods.append(row["Period"])
                return jsonify({'modulelevels': modulelevels, 'modulecodes': modulecodes, 'modulenames': modulenames, 'moduleperiods': moduleperiods})
                # return render_template("module.html", level=modulelevels, code=modulecodes, name=modulenames, period=moduleperiods)
            except:
                # When error happens, return the error information
                return print("Error Happened")

        # In the database, different faculties are stored in different tables, in FHSS
        # the program search the modules of the course according to the course name
        elif facultyname == "FHSS":
            con2 = sqlite3.connect("UUIS_database.db")
            con2.row_factory = sqlite3.Row
            cur2 = con2.cursor()
            cur2.execute(
                """SELECT LEVEL, CODE, NAME, PERIOD from UNNC_module_catalogue where Code IN (SELECT Code FROM UNNC_Course_FHSS where Code NOT LIKE 'CELEN%' AND Course = ?)""",
                (coursename,))
            rows = cur2.fetchall()

            # Create four dics to store the returned inforamtion
            modulelevels = []
            modulecodes = []
            modulenames = []
            moduleperiods = []
            try:
                for row in rows:
                    modulelevels.append(row["Level"])
                    modulecodes.append(row["Code"])
                    modulenames.append(row["Name"])
                    moduleperiods.append(row["Period"])
                return jsonify({'modulelevels': modulelevels, 'modulecodes': modulecodes, 'modulenames': modulenames, 'moduleperiods': moduleperiods})
            except:
                # When error happens, return the error information
                return print("Error Happened")

# This API is designed to allow users to report error
# and store the reported information into a database
@app.route('/ErrorReport', methods=["POST"])
def report_error():
    # User post his/her error report to back-end
    if request.method == "POST":
        error_message = request.json.get("error_message")

        # The program insert the error message to the error database
        # and return a value to front-end to check if inserted successfully
        try:
            con1 = sqlite3.connect("error.db")
            cur1 = con1.cursor()
            cur1.execute("""INSERT INTO Error (error) VALUES ('%s')""" % error_message)
            con1.commit()
            con1.close()
            # if successful, return 1
            return jsonify(1)
        except:
            # if failed, return 0
            return jsonify(0)


if __name__ == '__main__':
    app.debug = True
    app.run()
