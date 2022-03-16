# -*- coding = utf-8 -*-
# @Time: 2022/2/3 17:04
# @Author: Zhihang Zhu
# @File: China_Detail.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import sqlite3


def get_code():
    # con = sqlite3.connect("UUIS_database.db")
    # con.row_factory = sqlite3.Row
    # cur = con.cursor()
    codes = ["CELEN083", "EDEN4002", "INCM4034"]
    try:
        # count = 0
        # cur.execute("SELECT Code FROM UNNC_module_catalogue;")
        # codes = cur.fetchall()
        for code in codes:
            try:
                # count += 1
                # if count < 557:
                #     continue
                filename = code + ".html"
                get_html(filename, code)
            except:
                continue
    except:
        pass


def get_html(fileName, code):
    file = open(fileName, mode="w", encoding="utf-8")
    driver = webdriver.Chrome()
    driver.get(
        "https://campus.nottingham.ac.uk/psc/csprd_pub/EMPLOYEE/SA/c/UN_PROG_AND_MOD_EXTRACT.UN_PAM_CRSE_EXTRCT.GBL?&")
    driver.get(
        "https://campus.nottingham.ac.uk/psc/csprd_pub/EMPLOYEE/SA/c/UN_PROG_AND_MOD_EXTRACT.UN_PAM_CRSE_EXTRCT.GBL?&")
    time.sleep(1)
    # Enter the module catalogue
    driver.find_element_by_name('UN_PAM_EXTR_WRK_UN_MODULE_PB').click()
    time.sleep(2)
    # Choose the campus location: China
    sel1 = driver.find_element_by_name('UN_PAM_EXTR_WRK_CAMPUS')
    Select(sel1).select_by_index(1)
    time.sleep(2)
    # Choose the term
    sel2 = driver.find_element_by_name('UN_PAM_EXTR_WRK_STRM')
    Select(sel2).select_by_index(0)
    # Enter the module code of the specified year
    driver.find_element_by_id("UN_PAM_EXTR_WRK_UN_PAM_CRSE2_SRCH$3").send_keys(code)
    time.sleep(1)
    driver.find_element_by_name("UN_PAM_EXTR_WRK_UN_SEARCH_PB$3").click()
    time.sleep(1)
    driver.find_element_by_name("CRSE_CODE$0").click()
    time.sleep(2)
    text = driver.page_source
    time.sleep(1)
    file.write(text)
    file.close()
    driver.quit()


if __name__ == "__main__":
    get_code()
