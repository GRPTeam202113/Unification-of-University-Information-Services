# -*- coding = utf-8 -*-
# @Time: 2022/3/3 10:06
# @Author: Zhihang Zhu
# @File: ImportVue.py
# @Software: PyCharm

import sqlite3
from bs4 import BeautifulSoup
import os


def open_db():
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT Code from UNNC_module_catalogue;")
    code = cur.fetchall()
    for item in code:
            try:
                file = open("./UNNC Module Information/" + str(item[0]) + ".html", "r", encoding="utf-8")
                content = file.read()
                write_vue(item[0], content)
            except FileNotFoundError:
                continue


def write_vue(code, content):
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT Name from UNNC_module_catalogue WHERE Code = ?;", (code,))
    moduleName = cur.fetchall()
    name = ""
    for item in moduleName:
        name = item[0]
    file = open("./Module_Catalogue/" + code + ".vue", "wb")
    template_part1 = open("template_Part1.txt", "r", encoding="utf-8")
    template_part2 = open("template_Part2.txt", "r", encoding="utf-8")

    soup = BeautifulSoup(content.replace('<br>', '\n').replace('<br/>', '\n'), 'html.parser')

    Academic_Year = soup.find(id='UN_PAM_EXTR_WRK_HTMLAREA5').string
    Total_Credits = soup.find(id='UN_PAM_CRSE_DTL_UNITS_MINIMUM$0').string
    Level = soup.find(id='UN_PAM_CRSE_DTL_UN_LEVELS$0').string
    Target_Students = soup.find(id='UN_PAM_CRSE_DTL_UN_TARGET_STDNTS$0').string
    Offering_School = soup.find(id='ACAD_ORG_TBL_DESCRFORMAL$0').string
    Taught_Semesters = soup.find(id='SSR_CRSE_TYPOFF_DESCR$0').string
    Requisites = soup.find(id='UN_PAM_CRSE_WRK_UN_PRE_CO_REQ_GRP$0').string
    Additional_Requirements = soup.find(id='UN_PAM_CRSE_WRK_UN_ADD_REQ_GRP$0').string
    generalFurtherActivityDetail = soup.find(id="UN_PAM_EXTR_WRK_UN_ACTIVITY_INFO$0").string
    educationAims = str(soup.find(id="UN_PAM_CRSE_DTL_UN_AIMS$0"))
    learningOutcome = str(soup.find(id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0"))
    summaryOfContent = str(soup.find(id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0"))
    assessmentFurtherActivityDetail = soup.find(id="UN_PAM_EXTR_WRK_UN_ACTIVITY_INFO$97$$0").string
    methodAndFrequency = ""

    for index in range(0, 5):
        try:
            s1 = "UN_PAM_CRSE_FRQ_SSR_COMPONENT$" + str(index)
            methodAndFrequency_Activity = soup.find(id=s1).string
            s1 = "UN_PAM_EXTR_WRK_UN_CRSE_DURATN_WKS$" + str(index)
            methodAndFrequency_Weeks = soup.find(id=s1).string
            s1 = "UN_PAM_EXTR_WRK_UN_CRSE_NUM_SESN$" + str(index)
            methodAndFrequency_Sessions = soup.find(id=s1).string
            s1 = "UN_PAM_EXTR_WRK_UN_CRSE_DURATN_SES$" + str(index)
            methodAndFrequency_Duration = soup.find(id=s1).string
            if index == 0:
                methodAndFrequency += "{\nactivity: '" + methodAndFrequency_Activity + "',\nnumberOfWeeks: '" + methodAndFrequency_Weeks + "',\nnumberOfSessions: '" + methodAndFrequency_Sessions + "',\nduration: '" + methodAndFrequency_Duration + "'\n}"
            else:
                methodAndFrequency += ", {\nactivity: '" + methodAndFrequency_Activity + "',\nnumberOfWeeks: '" + methodAndFrequency_Weeks + "',\nnumberOfSessions: '" + methodAndFrequency_Sessions + "',\nduration: '" + methodAndFrequency_Duration + "'\n}"
        except:
            continue

    methodOfAssessment = ""
    for index in range(0, 5):
        try:
            methodOfAssessment_Type = soup.find(id="UN_QA_CRSE_ASAI_DESCR50$" + str(index)).string
            methodOfAssessment_Weight = soup.find(id="UN_QA_CRSE_ASAI_SSR_CW_WEIGHT$" + str(index)).string
            methodOfAssessment_Requirements = soup.find(id="UN_QA_CRSE_ASAI_SSR_DESCRLONG$" + str(index)).string
            if index == 0:
                methodOfAssessment += "{\ntype: '" + methodOfAssessment_Type + "',\nweight: '" + methodOfAssessment_Weight + "',\nrequirements: '" + methodOfAssessment_Requirements.replace('\t', '') + "'\n}"
            else:
                methodOfAssessment += ", {\ntype: '" + methodOfAssessment_Type + "',\nweight: '" + methodOfAssessment_Weight + "',\nrequirements: '" + methodOfAssessment_Requirements.replace('\t', '') + "'\n}"
        except:
            continue

    try:
        Convenor = soup.find(id='UN_PAM_CRS_CONV_NAME52$0').string
    except BaseException as e:
        Convenor = ""

    if Convenor != "":
        for header in ["CELE_", "FOSE_", "FHSS_", "FOB_"]:
            if header == "CELE_":
                staffDepartment = "Center for English Language Education"
            elif header == "FOSE_":
                staffDepartment = "Faculty of Science and Engineering"
            elif header == "FHSS_":
                staffDepartment = "Faculty of Humanities and Social Sciences"
            elif header == "FOB_":
                staffDepartment = "Faculty of Business"
            fileName = header + Convenor + ".html"
            if os.path.exists("./UNNC Staff Information/" + fileName):
                try:
                    staffFile = open("./UNNC Staff Information/" + fileName, "r", encoding="utf-8")
                    soup2 = BeautifulSoup(staffFile, "html.parser")
                    staffInformation = soup2.select(".key-information__details__row__cell")
                    staffOffice = staffInformation[1].string.replace("\n", "").strip()
                    staffCampus = staffInformation[3].string.replace("\n", "").strip()
                    staffAddress = staffInformation[5].string.replace("\n", "").strip()
                    try:
                        staffEmail = staffInformation[7].string.replace("\n", "").strip()
                    except:
                        pass
                    break
                except:
                    print(name)
            elif os.path.exists("./UNNC Staff Information/" + header + Convenor.replace("Dr ", "").replace("Dr.", "").replace("Prof.", "") + ".html"):
                fileName = header + Convenor.replace("Dr ", "").replace("Dr.", "").replace("Prof.", "") + ".html"
                try:
                    staffFile = open("./UNNC Staff Information/" + fileName, "r", encoding="utf-8")
                    soup2 = BeautifulSoup(staffFile, "html.parser")
                    staffInformation = soup2.select(".key-information__details__row__cell")
                    staffOffice = staffInformation[1].string.replace("\n", "").strip()
                    staffCampus = staffInformation[3].string.replace("\n", "").strip()
                    staffAddress = staffInformation[5].string.replace("\n", "").strip()
                    try:
                        staffEmail = staffInformation[7].string.replace("\n", "").strip()
                    except:
                        pass
                    break
                except:
                    print(name)
            else:
                staffOffice = ""
                staffCampus = ""
                staffEmail = ""
                staffAddress = ""
                staffDepartment = ""
                continue
    else:
        staffOffice = ""
        staffCampus = ""
        staffEmail = ""
        staffAddress = ""
        staffDepartment = ""

    try:
        script = "moduleName: '" + name.replace("\n", "") + "',\nyear: '" + Academic_Year.replace("\n", "") + "',\ncredit: '" + Total_Credits + "',\nlevel: '" + Level + "',\ntargetStudents: '" + Target_Students.replace("\n", "") + "',\nofferingSchool: '" + Offering_School + "',\ntaughtSemesters: '" + Taught_Semesters + "',\nrequisites: '" + Requisites + "',\nadditionalRequirements: '" + Additional_Requirements + "',\nstaffName: '" + Convenor + "',\ngeneralFurtherActivityDetail: '" + generalFurtherActivityDetail.replace('\n', '<br>').replace("'s", "").replace('\t','') + "',\neducationAims: '" + educationAims.replace('\n', '<br>').replace("'s", "").replace("'", "\"").replace('\t', "") + "',\nlearningOutcome: '" + learningOutcome.replace('\n', '<br>').replace("'s", "").replace("'", "\"").replace('\t', "") + "',\nsummaryOfContent: '" + summaryOfContent.replace('\n', '<br>').replace("'s", "").replace("'", "\"").replace('\t', "").replace('', '').replace('', '').replace('', '').replace('', '').replace('', '').replace('', '') + "',\nassessmentFurtherActivityDetail: '" + assessmentFurtherActivityDetail.replace('\n', '<br>').replace("'s", "").replace("'", "\"").replace('\t', "") + "',\nmethodAndFrequency: [" + methodAndFrequency + "],\nassessmentTable: [" + methodOfAssessment + "],\nstaffOffice: '" + staffOffice + "',\nstaffAddress: '" + staffAddress + "',\nstaffCampus: '" + staffCampus + "',\nstaffTelephone: '" + staffEmail + "',\nstaffDepartment: '" + staffDepartment + "'\n"
        file.write((template_part1.read() + script + template_part2.read()).encode(encoding="utf-8"))
    except:
        print(code)
        print(staffCampus)
        pass
    file.close()


if __name__ == "__main__":
    open_db()