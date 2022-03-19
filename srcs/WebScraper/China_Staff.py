# -*- coding = utf-8 -*-
# @Time: 2022/2/17 19:18
# @Author: Zhihang Zhu
# @File: China_Staff.py
# @Software: PyCharm

import requests
import sqlite3
import re
import urllib.request
from bs4 import BeautifulSoup

# Relative information to look through the URL
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}

urlNormalCollection = {"FOSE": "https://www.nottingham.edu.cn/en/science-engineering/people/academic.aspx",
                       "FHSS": "https://www.nottingham.edu.cn/en/humanities-and-social-sciences/people/listing.aspx",
                       "FOB": "https://www.nottingham.edu.cn/en/business/people/academic.aspx"}
urlSpecialCollection = {
    "CELE": "https://www.nottingham.edu.cn/en/cele/cele-and-cpso-staff/cele-staff-profile-listing.aspx?STFPageIndex=",
    "PGR": "https://www.nottingham.edu.cn/en/graduateschool/people/gs-staff-listing.aspx"}
facultyList = ["FOSE", "FHSS", "FOB", "CELE", "PGR"]
urlHead = "https://www.nottingham.edu.cn"


# Different faculty have different forms of teaching staffs' list
# According to the faculty name, using different mathods to collect staff's information
def get_staff():
    # If this program needs to run twice, ignore the operation of creating a new table in order to store staff's information
    # con = sqlite3.connect("UUIS_database_Testing.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    # cur.execute("CREATE TABLE UNNC_Staff('Name' TEXT NOT NULL,'Course' TEXT NOT NULL,'URL' TEXT NOT NULL);")
    # Cope with FOSE, FHSS, FOB Faculty
    for index in range(0, 3):
        fileName = str(facultyList[index])
        try:
            request = urllib.request.Request(url=urlNormalCollection[fileName], headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            analyse_link_staff_1(content, fileName)
        except BaseException as e:
            print(e)
    # Cope with CELE Department
    fileName = str(facultyList[3])
    for index in range(1, 12):
        try:
            request = urllib.request.Request(url=urlSpecialCollection[fileName] + str(index), headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            analyse_link_staff_2(content, fileName)
        except BaseException as e:
            print(e)

# Get staff information of FOSE, FHSS, FOB and insert them into database
def analyse_link_staff_1(content, fileName):
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.select("td > a")
    reg = r'<a.+?href="(.+?)".*>(.+)</a>'
    urlre = re.compile(reg)
    for item in links:
        listPart = urlre.findall(str(item))
        target = urlHead + str(listPart[0][0])
        staffName = str(listPart[0][1])
        cur.execute("INSERT INTO UNNC_Staff ('Name','Course','URL') VALUES (?,?,?);", (staffName, fileName, target))
        con.commit()
        request = urllib.request.Request(url=target, headers=headers)
        res = requests.get(target)
        # Testing Code
        print(staffName + " | Response status: " + str(res.status_code))
        response = urllib.request.urlopen(request)
        staffInfo = response.read().decode('utf-8')
        file = open(fileName + "_" + staffName + ".html", "w", encoding="utf-8")
        file.write(staffInfo)
        file.close()

# Get the staff information of CELE Department
def analyse_link_staff_2(content, fileName):
    con = sqlite3.connect("UUIS_database_Testing.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.select("h2 > a")
    reg = r'<a.+?href="(.+?)".*>(.+)</a>'
    urlre = re.compile(reg)
    for item in links:
        listPart = urlre.findall(str(item))
        target = urlHead + str(listPart[0][0])
        staffName = str(listPart[0][1])
        cur.execute("INSERT INTO UNNC_Staff ('Name','Course','URL') VALUES (?,?,?);", (staffName, fileName, target))
        con.commit()
        request = urllib.request.Request(url=target, headers=headers)
        res = requests.get(target)
        # Testing Code
        print(staffName + " | Response status: " + str(res.status_code))
        response = urllib.request.urlopen(request)
        staffInfo = response.read().decode('utf-8')
        file = open(fileName + "_" + staffName + ".html", "w", encoding="utf-8")
        file.write(staffInfo)
        file.close()


if __name__ == "__main__":
    get_staff()
