# -*- coding = utf-8 -*-
# @Time: 2022/3/7 20:37
# @Author: Zhihang Zhu
# @File: China_Course_Detail.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import sqlite3

# Cope with the brief introduction about the course
# Collect all the information and insert them into database
def get_course():
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    # Use course's name to collect the course information
    cur.execute("CREATE TABLE UNNC_Course_Info('Name' TEXT NOT NULL,'Degree' TEXT NOT NULL,'Type' TEXT NOT NULL,'Duration' TEXT NOT NULL,'StartDate' TEXT NOT NULL,'Faculty' TEXT NOT NULL,'Model' TEXT NOT NULL);")
    cur.execute("SELECT Name FROM UNNC_Faculty;")
    courses = cur.fetchall();
    for item in courses:
        # Use course's name to search for the back-end document
        try:
            fileName = "./UNNC Course Information/" + str(item[0]) + ".html"
            content = open(fileName, "r", encoding="utf-8")
            write_into(content, str(item[0]))
        except BaseException as e:
            print(e)
            break

# Write all the course introduction into database
def write_into(content, name):
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    soup = BeautifulSoup(content, "html.parser")
    information = soup.select(".key-information__details__row__cell")
    # The following part contains the brief introduction about the specified course
    degree = information[1].string.strip()
    types = information[3].string.strip()
    duration = information[5].string.strip()
    startDate = information[7].string.strip()
    faculty = information[9].string.strip()
    model = information[11].string.strip()
    cur.execute("INSERT INTO UNNC_Course_Info (Name,Degree,Type,Duration,StartDate,Faculty,Model) VALUES(?,?,?,?,?,?,?);", (name, degree, types, duration, startDate, faculty, model))
    con.commit()


if __name__ == "__main__":
    get_course()
