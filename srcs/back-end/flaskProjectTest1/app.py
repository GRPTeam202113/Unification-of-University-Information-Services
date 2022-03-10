from flask import Flask, request, render_template, jsonify
import sqlite3
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/faculty/course', methods=["POST"])
def course():
    if request.method == "POST":
        coursename = request.json.get("coursename")

        con = sqlite3.connect("UUIS_database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""SELECT Degree, Type, Duration, StrateDate, Faculty, Model from UNNC_Course_Info where Name = ?"""(coursename,))
        rows = cur.fetchall()
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
                return print("Error Happened")

@app.route('/faculty/course/year/module', methods=["POST"])
def year():
    if request.method == "POST":
        facultyname = request.json.get("facultyname")
        coursename = request.json.get("coursename")
        year = request.get.json('year')
        if year == 2:
            level = "Level 1"
        if year == 3:
            level = "Level 2"
        if year == 4:
            level = "Level 3"

        if facultyname != "FHSS":
            con1 = sqlite3.connect("UUIS_database.db")
            con1.row_factory = sqlite3.Row
            cur1 = con1.cursor()
            cur1.execute("""SELECT * from UNNC_module_catalogue where Name IN (SELECT Name FROM UNNC_Course where Course = ? AND Level = ?)""",(coursename,level,))
            rows = cur1.fetchall()
            modulelevels = []
            modulecodes = []
            modulenames = []
            moduleperiods = []
            i = 0
            try:
                for row in rows:
                    i=i+1
                    modulelevels.append(row["Level"])
                    modulecodes.append(row["Code"])
                    modulenames.append(row["Name"])
                    moduleperiods.append(row["Period"])
                print(i)
                return jsonify({'modulelevels': modulelevels, 'modulecodes': modulecodes, 'modulenames': modulenames,
                                'moduleperiods': moduleperiods})
            except:
                return print("Error Happened")
        else:
            con2 = sqlite3.connect("UUIS_database.db")
            con2.row_factory = sqlite3.Row
            cur2 = con2.cursor()
            cur2.execute(
                """SELECT * from UNNC_module_catalogue where Code IN (SELECT Code FROM UNNC_Course_FHSS where Code NOT LIKE 'CELEN%' AND Course = ?)""",
                (coursename,))
            rows = cur2.fetchall()
            modulelevels = []
            modulecodes = []
            modulenames = []
            moduleperiods = []
            i = 0
            try:
                for row in rows:
                    i = i+1
                    modulelevels.append(row["Level"])
                    modulecodes.append(row["Code"])
                    modulenames.append(row["Name"])
                    moduleperiods.append(row["Period"])
                print(i)
                return jsonify({'modulelevels': modulelevels, 'modulecodes': modulecodes, 'modulenames': modulenames, 'moduleperiods': moduleperiods})
            except:
                return print("Error Happened")



@app.route('/faculty/course/module', methods=["POST","GET"])
def course():
    if request.method == "POST":
        facultyname = request.json.get('facultyname')
        coursename = request.json.get('coursename')


        if facultyname != "FHSS":
            con1 = sqlite3.connect("UUIS_database.db")
            con1.row_factory = sqlite3.Row
            cur1 = con1.cursor()
            cur1.execute("""SELECT * from UNNC_module_catalogue where Name IN (SELECT Name FROM UNNC_Course where Course = ?)""",(coursename,))
            rows = cur1.fetchall()
            modulelevels = []
            modulecodes = []
            modulenames = []
            moduleperiods = []
            module = []
            i = 0
            try:
                for row in rows:
                    i=i+1
                    modulelevels.append(row["Level"])
                    modulecodes.append(row["Code"])
                    modulenames.append(row["Name"])
                    moduleperiods.append(row["Period"])
                print(i)
                module.append(modulelevels)
                return jsonify({'modulelevels': modulelevels, 'modulecodes': modulecodes, 'modulenames': modulenames, 'moduleperiods': moduleperiods})
                # return render_template("module.html", level=modulelevels, code=modulecodes, name=modulenames, period=moduleperiods)
            except:
                return print("Error Happened")
        else:
            con2 = sqlite3.connect("UUIS_database.db")
            con2.row_factory = sqlite3.Row
            cur2 = con2.cursor()
            cur2.execute(
                """SELECT * from UNNC_module_catalogue where Code IN (SELECT Code FROM UNNC_Course_FHSS where Code NOT LIKE 'CELEN%' AND Course = ?)""",
                (coursename,))
            rows = cur2.fetchall()
            modulelevels = []
            modulecodes = []
            modulenames = []
            moduleperiods = []
            i = 0
            try:
                for row in rows:
                    i = i+1
                    modulelevels.append(row["Level"])
                    modulecodes.append(row["Code"])
                    modulenames.append(row["Name"])
                    moduleperiods.append(row["Period"])
                print(i)
                return jsonify({'modulelevels': modulelevels, 'modulecodes': modulecodes, 'modulenames': modulenames, 'moduleperiods': moduleperiods})
            except:
                return print("Error Happened")

if __name__ == '__main__':
    app.debug = True
    app.run()
