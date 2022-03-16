# -*- coding = utf-8 -*-
# @Time: 2022/2/2 11:26
# @Author: Zhihang Zhu
# @File: China.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from bs4 import BeautifulSoup
import sqlite3


def get_html():
    driver = webdriver.Chrome()
    time.sleep(1)
    driver.get(
        "https://campus.nottingham.ac.uk/psc/csprd_pub/EMPLOYEE/SA/c/UN_PROG_AND_MOD_EXTRACT.UN_PAM_CRSE_EXTRCT.GBL?&")
    driver.get(
        "https://campus.nottingham.ac.uk/psc/csprd_pub/EMPLOYEE/SA/c/UN_PROG_AND_MOD_EXTRACT.UN_PAM_CRSE_EXTRCT.GBL?&")
    time.sleep(1)
    # Enter the module catalogue
    driver.find_element_by_name('UN_PAM_EXTR_WRK_UN_MODULE_PB').click()
    driver.implicitly_wait(5)
    # Choose the campus
    sel2 = driver.find_element_by_name('UN_PAM_EXTR_WRK_CAMPUS')
    Select(sel2).select_by_index(1)
    time.sleep(1)
    sel1 = driver.find_element_by_name('UN_PAM_EXTR_WRK_STRM')
    Select(sel1).select_by_index(0)
    time.sleep(1)
    # Choose the faculty, this is one solution towards the situation
    for index2 in range(1, 25):
        if index2 != 2:
            try:
                sel3 = driver.find_element_by_name('UN_PAM_EXTR_WRK_UN_PAM_CRSE1_SRCH$0')
                Select(sel3).select_by_index(index2)
                driver.find_element_by_name('UN_PAM_EXTR_WRK_UN_SEARCH_PB$0').click()
                # Get into the modules page and get the page source
                time.sleep(2)
                # Get the web page's code and send it to analysis part
                text = driver.page_source
                add_db(text, "UNNC_module_catalogue")
                time.sleep(1)
            except:
                break
        driver.get(
            "https://campus.nottingham.ac.uk/psc/csprd_pub/EMPLOYEE/SA/c/UN_PROG_AND_MOD_EXTRACT.UN_PAM_CRSE_EXTRCT.GBL?&")
        driver.find_element_by_name('UN_PAM_EXTR_WRK_UN_MODULE_PB').click()
        sel1 = driver.find_element_by_name('UN_PAM_EXTR_WRK_CAMPUS')
        Select(sel1).select_by_index(1)
        time.sleep(2)
        sel2 = driver.find_element_by_name('UN_PAM_EXTR_WRK_STRM')
        Select(sel2).select_by_index(0)
        time.sleep(1)
    driver.quit()


def add_db(text, tableName):
    soup = BeautifulSoup(text, 'html.parser')
    # Connect the database
    con = sqlite3.connect("UUIS_database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    # Create specific table with specified name and term
    try:
        command1 = 'CREATE TABLE "' + tableName + '" ("Level"	TEXT NOT NULL,"Code"    TEXT NOT NULL,"Name"	TEXT NOT NULL,"Period"	TEXT NOT NULL);'
        cur.execute(command1)
    except:
        pass
    # Store the detailed information in order
    moduleCode = []
    moduleName = []
    moduleLevel = []
    modulePeriod = []
    for num in range(0, 1000):
        try:
            moduleCode += soup.find_all("a", id="CRSE_CODE$" + str(num))
            moduleName += soup.find_all("span", id="UN_PAM_CRSE_VW_COURSE_TITLE_LONG$" + str(num))
            moduleLevel += soup.find_all("span", id="UN_PAM_CRSE_VW_UN_LEVEL1_DESCR$" + str(num))
            modulePeriod += soup.find_all("span", id="SSR_CRSE_TYPOFF_DESCR$" + str(num))
            cur.execute("INSERT INTO " + tableName + " (Level,Code,Name,Period) VALUES (?,?,?,?)", (
                str(moduleLevel[num].string), str(moduleCode[num].string), str(moduleName[num].string),
                str(modulePeriod[num].string)))
            con.commit()
        # If there is no more modules
        except:
            break


if __name__ == "__main__":
    get_html()
