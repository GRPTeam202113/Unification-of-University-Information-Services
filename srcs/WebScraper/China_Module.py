# -*- coding = utf-8 -*-
# @Time: 2022/2/16 9:52
# @Author: Zhihang Zhu
# @File: China_Module.py
# @Software: PyCharm
import requests
import os
import re
import sqlite3
import urllib.request
import urllib
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}

urlHead1 = "https://www.nottingham.edu.cn/en/study-with-us/undergraduate/courses/atoz.aspx?PageIndex="
urlHead2 = "https://www.nottingham.edu.cn"

courseCount = 0
courseNameList = {}


# This program is used to collect the modules' information in a faculty
# According to the specified faculty, using different method to cope with the webpages
def get_faculty():
    for index in range(1, 7):
        # according to the url, search the faculty's course name and get the result
        try:
            url = urlHead1 + str(index)
            request = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(request)
            content = response.read().decode('utf-8')
            analyse_link_faculty(content)
        except BaseException as e:
            print(e)
            break

# Analyse the information about faculty and its modules
def analyse_link_faculty(content):
    global courseCount
    global courseNameList
    soup1 = BeautifulSoup(content, 'html.parser')
    links = soup1.select("h2 > a")
    reg = r'<a.+?href="(.+?)".*>(.+)</a>'
    urlre = re.compile(reg)
    for item in links:
        listPart = urlre.findall(str(item))
        target = urlHead2 + str(listPart[0][0])
        res = requests.get(target)
        courseName = str(listPart[0][1])
        # Testing Code
        print(courseName + " | Response status: " + str(res.status_code))
        if courseName == "International Studies with Spanish/German/French/Japanese/Chinese":
            courseName = "International Studies with Spanish German French Japanese Chinese"
        courseNameList[courseCount] = courseName
        courseCount += 1
        request = urllib.request.Request(url=target, headers=headers)
        response = urllib.request.urlopen(request)
        course = response.read().decode('utf-8')
        # soup2 = BeautifulSoup(course, "html.parser")
        # courseModuleList = str(soup2.find_all("div", id="faq-content-1")) + str(
        #     soup2.find_all("div", id="faq-content-2")) + str(soup2.find_all("div", id="faq-content-3")) + str(
        #     soup2.find_all("div", id="faq-content-4"))
        file = open(str(courseCount) + ".html", "w", encoding="utf-8")
        file.write(course)
        file.close()


def analyse_table():
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE UNNC_Course("Name" TEXT NOT NULL,"Course" TEXT NOT NULL);')
    except:
        pass
    # Cope with the FoSE modules
    for index in [0, 1, 2, 3, 4, 5, 6, 7, 9, 13, 14, 25, 26, 27, 28]:
        file = open('./UNNC Course Information/' + str(index + 1) + ".html", "r", encoding="utf-8")
        soup = BeautifulSoup(file, "html.parser")
        moduleList = soup.select('td') + soup.select('td > p')
        for module in moduleList:
            if str(module.string) == "None" or str(module.string) == " ":
                continue
            else:
                cur.execute("INSERT INTO UNNC_Course (Name, Course) VALUES (?,?);",
                            (str(module.string), courseNameList[index]))
                con.commit()
    # Cope with the FoB modules
    for index1 in [15, 16, 17, 18, 19]:
        file = open('./UNNC Course Information/' + str(index1 + 1) + ".html", "r", encoding="utf-8")
        soup = BeautifulSoup(file, "html.parser")
        moduleList = soup.select("td")
        moduleListDetails = []
        for module in moduleList:
            moduleListDetails.append(str(module.string))
        for index2 in range(1, 2001, 4):
            try:
                moduleName = moduleListDetails[index2]
                if moduleName == "Title":
                    continue
                cur.execute("INSERT INTO UNNC_COURSE (Name, Course) VALUES (?,?);", (moduleName, courseNameList[index1]))
                con.commit()
            except:
                break
    # Get the PDF download links and apply downloading operation to the links
    for index2 in [8, 10, 11, 12, 20, 21, 22, 23, 24]:
        file = open('./UNNC Course Information/' + str(index2 + 1) + ".html", "r", encoding="utf-8")
        soup = BeautifulSoup(file, "html.parser")
        modulePDF = soup.select("a[title='Download a PDF document of the course module structure']")
        reg = r'<a.+?href="(.+?)".+?title="(.+?)">\n(.+)\n</a>'
        urlre = re.compile(reg)
        if not os.path.exists('./auto_download'):
            os.makedirs('auto_download')
        item = modulePDF[0]
        listPart = urlre.findall(str(item))
        target = urlHead2 + listPart[0][0]
        urllib.request.urlretrieve(target, os.path.join('./auto_download', courseNameList[index2] + ".pdf"))

# For FHSS faculty, PDF analysis is essential
# Before running this part of code, some PDF Processing operations are needed or exceptions may occur.
def analyse_pdf():
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE UNNC_Course_FHSS ("Code" TEXT NOT NULL,"Course" TEXT NOT NULL);')
    except:
        pass
    for index in [8, 10, 11, 12, 20, 21, 22, 23, 24]:
        file = open("./auto_download/" + courseNameList[index] + ".html", "r", encoding="gb2312")
        soup = BeautifulSoup(file, "html.parser")
        moduleList = soup.select('td > p > b > span')
        moduleDetail = []
        for module in moduleList:
            moduleDetail.append(str(module.string))
        for index2 in range(1, 1001):
            # get all the modules
            try:
                if moduleDetail[index2] != "Title " and moduleDetail[index2] != "Credits " and moduleDetail[index2] != "Taught " and moduleDetail[index2] != "None" and moduleDetail[index2] != "Code " and moduleDetail[index2] != " " and moduleDetail[index2] != "Title" and moduleDetail[index2] != "Credits" and moduleDetail[index2] != "Taught" and moduleDetail[index2] != "Code" and moduleDetail[index2] is not None and moduleDetail[index2] != ", " and moduleDetail[index2] != "\n":
                    if moduleDetail[index2].isalnum() is not True:
                        moduleDetail[index2] = moduleDetail[index2][0:8]
                    print(moduleDetail[index2])
                    cur.execute("INSERT INTO UNNC_COURSE_FHSS (Code, Course) VALUES (?,?);", (moduleDetail[index2], courseNameList[index]))
                    con.commit()
            except:
                break


if __name__ == "__main__":
    get_faculty()
    analyse_table()
    # Before running this part, the downloaded PDF files needs to be handled.
    analyse_pdf()
