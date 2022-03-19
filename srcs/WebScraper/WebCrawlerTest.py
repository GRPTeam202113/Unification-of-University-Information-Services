import unittest
from bs4 import BeautifulSoup


class WebCrawlerTest(unittest.TestCase):
    # Test whether the course information is collected correctly
    def test_course_information(self):
        file = open("./UNNC Course Information/Aerospace Engineering.html", "r", encoding="utf-8")
        content = file.read()
        soup = BeautifulSoup(content.replace('<br>', '\n').replace('<br/>', '\n'), 'html.parser')
        information = soup.select(".key-information__details__row__cell")
        # The following part contains the brief introduction about the specified course
        degree = information[1].string.strip()
        types = information[3].string.strip()
        duration = information[5].string.strip()
        startDate = information[7].string.strip()
        faculty = information[9].string.strip()
        model = information[11].string.strip()
        # Test the information for the course website collected by the web crawler
        self.assertEqual(degree, "BEng (Hons) Aerospace Engineering")
        self.assertEqual(types, "Full time")
        self.assertEqual(duration, "Three or four years depending on entry qualifications")
        self.assertEqual(startDate, "September 2022")
        self.assertEqual(faculty, "Aerospace / Faculty of Science and Engineering")
        self.assertEqual(model, "2+2, 4+0")

    # Test whether the module information is collected correctly
    def test_module_information(self):
        file = open("./UNNC Module Information/ABEE1021.html", "r", encoding="utf-8")
        content = file.read()
        soup = BeautifulSoup(content.replace('<br>', '\n').replace('<br/>', '\n'), 'html.parser')
        Academic_Year = soup.find(id='UN_PAM_EXTR_WRK_HTMLAREA5').string
        Total_Credits = soup.find(id='UN_PAM_CRSE_DTL_UNITS_MINIMUM$0').string
        Level = soup.find(id='UN_PAM_CRSE_DTL_UN_LEVELS$0').string
        Target_Students = soup.find(id='UN_PAM_CRSE_DTL_UN_TARGET_STDNTS$0').string
        Offering_School = soup.find(id='ACAD_ORG_TBL_DESCRFORMAL$0').string
        Taught_Semesters = soup.find(id='SSR_CRSE_TYPOFF_DESCR$0').string
        Requisites = soup.find(id='UN_PAM_CRSE_WRK_UN_PRE_CO_REQ_GRP$0').string
        Additional_Requirements = soup.find(id='UN_PAM_CRSE_WRK_UN_ADD_REQ_GRP$0').string
        # Test the information for the module catalogue collected by the web crawler
        self.assertEqual(Academic_Year, "\nAcademic Year 2022")
        self.assertEqual(Total_Credits, "20.00")
        self.assertEqual(Level, "1")
        self.assertEqual(Target_Students, "\nArchitecture")
        self.assertEqual(Offering_School, "Department of Architecture and Built Environment")
        self.assertEqual(Taught_Semesters, "Full year China")
        self.assertEqual(Requisites, "N/A")
        self.assertEqual(Additional_Requirements, "N/A")

    # Test whether the staff information is collected correctly
    def test_staff_information(self):
        file = open("./UNNC Staff Information/FOSE_Ruibin Bai.html", "r", encoding="utf-8")
        content = file.read()
        soup = BeautifulSoup(content.replace('<br>', '\n').replace('<br/>', '\n'), 'html.parser')
        staffInformation = soup.select(".key-information__details__row__cell")
        staffOffice = staffInformation[1].string.replace("\n", "").strip()
        staffCampus = staffInformation[3].string.replace("\n", "").strip()
        staffAddress = staffInformation[5].string.replace("\n", "").strip()
        # Test the information for the staff introduction website collected by the web crawler
        self.assertEqual(staffOffice, "PMB 425, Sir Peter Mansfield Building")
        self.assertEqual(staffCampus, "University of Nottingham Ningbo China")
        self.assertEqual(staffAddress, "199 Taikang East Road, Ningbo, 315100, China")


if __name__ == '__main__':
    unittest.main()
