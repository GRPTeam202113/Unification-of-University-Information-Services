import pytest
import json
import requests

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'ok'


# This class is defined to test API '/faculty/course',
# which take a course name as input,
# and return the corresponding information of this course.
class TestCouseInfo:
    _data_Civil_Engineering = {
        'coursename': "Civil Engineering"
    }
    _data_Computer_Science = {
        'coursename': "Computer Science"
    }
    _data_Computer_Science_with_Artificial_Intelligence = {
        'coursename': "Computer Science with Artificial Intelligence"
    }
    _data_Economics = {
        'coursename': "Economics"
    }
    _data_Electrical_and_Electronic_Engineering = {
        'coursename': "Electrical and Electronic Engineering"
    }
    _data_Aerospace_Engineering = {
        'coursename': "Aerospace Engineering"
    }
    _data_Architectural_Environment_Engineering = {
        'coursename': "Architectural Environment Engineering"
    }
    _data_Architecture = {
        'coursename': "Architecture"
    }
    _data_Chemical_Engineering = {
        'coursename': "Chemical Engineering"
    }
    _data_Chemistry = {
        'coursename': "Chemistry"
    }
    _data_English_Language_and_Applied_Linguistics = {
        'coursename': "English Language and Applied Linguistics"
    }
    _data_English_Language_and_Literature = {
        'coursename': "English Language and Literature"
    }
    _data_English_with_International_Business = {
        'coursename': "English with International Business"
    }
    _data_Environmental_Engineering = {
        'coursename': "Environmental Engineering"
    }
    _data_Environmental_Sciences = {
        'coursename': "Environmental Sciences"
    }
    _data_Finance_Accounting_and_Management = {
        'coursename': "Finance, Accounting and Management"
    }
    _data_International_Business_Economics = {
        'coursename': "International Business Economics"
    }
    _data_International_Business_Management = {
        'coursename': "International Business Management"
    }
    _data_International_Business_with_Communication_Studies = {
        'coursename': "International Business with Communication Studies"
    }
    _data_International_Business_with_Language = {
        'coursename': "International Business with Language"
    }
    _data_International_Communications_Studies = {
        'coursename': "International Communications Studies"
    }
    _data_International_Communications_Studies_with_Chinese = {
        'coursename': "International Communications Studies with Chinese"
    }
    _data_International_Economics_and_Trade = {
        'coursename': "International Economics and Trade"
    }
    _data_International_Studies = {
        'coursename': "International Studies"
    }
    _data_International_Studies_with_Spanish_German_French_Japanese_Chinese = {
        'coursename': "International Studies with Spanish German French Japanese Chinese"
    }
    _data_Mathematics_with_Applied_Mathematics = {
        'coursename': "Mathematics with Applied Mathematics"
    }
    _data_Mechanical_Engineering = {
        'coursename': "Mechanical Engineering"
    }
    _data_Product_Design_and_Manufacture = {
        'coursename': "Product Design and Manufacture"
    }
    _data_Statistics = {
        'coursename': "Statistics"
    }


    #Wrong http method
    def test_course_info1(self, client):
        url = '/faculty/course'
        rv = client.get(url)
        assert rv.status_code == 405

    # Wrong url test
    # It will return a 404 bad request
    def test_course_info2(self, client):
        url = '/faculty'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Civil_Engineering))
        assert rv.status_code == 404

    # Wrong url test
    # It will return a 404 bad request
    def test_course_info3(self, client):
        url = '/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Civil_Engineering))
        assert rv.status_code == 404

    # Wrong input
    # It will raise a TypeError
    def test_course_info4(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "civil Engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info5(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "computer Science"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info6(self, client):
       with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "economics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info7(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "electrical and electronic engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info8(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "aerospace engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info9(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "architectural environment engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info10(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "architecture"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info11(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "chemical engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info12(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "computer science with artificial intelligence"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info13(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "chemistry"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info14(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "english language and applied linguistics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info15(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "english language and literature"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info16(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "english with international business"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info17(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "environmental engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info18(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "environmental sciences"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info19(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "finance, accounting and management"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info20(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international business economics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info21(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international business management"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info22(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international business with communication studies"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info23(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "iternational business with language"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info24(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international communications studies"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info25(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international communications studies with chinese"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info26(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international economics and trade"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info27(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international studies"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info28(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "international studies with spanish german french japanese chinese"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info29(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "mathematics with applied mathematics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info30(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "mechanical engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info31(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "product design and manufacture"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info32(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course'
            client.post(url, content_type='application/json', data='{"coursename": "statistics"}')

    # Right input and url
    # It will connect successfully
    def test_course_info33(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Civil_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info34(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Computer_Science))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info35(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Computer_Science_with_Artificial_Intelligence))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info36(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Economics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info37(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Electrical_and_Electronic_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info38(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Aerospace_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info39(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Architectural_Environment_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info40(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Architecture))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info41(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Chemical_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info42(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Chemistry))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info43(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_English_Language_and_Applied_Linguistics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info44(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_English_Language_and_Literature))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info45(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_English_with_International_Business))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info46(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Environmental_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info47(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Environmental_Sciences))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info48(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Finance_Accounting_and_Management))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info49(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Business_Economics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info50(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Business_Management))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info51(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Business_with_Communication_Studies))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info52(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Business_with_Language))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info53(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Communications_Studies))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info54(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Communications_Studies_with_Chinese))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info55(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Economics_and_Trade))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info56(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Studies))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info57(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Studies_with_Spanish_German_French_Japanese_Chinese))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info58(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Mathematics_with_Applied_Mathematics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info59(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Mechanical_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info50(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Product_Design_and_Manufacture))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info61(self, client):
        url = '/faculty/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Statistics))
        assert rv.status_code == 200

class TestErrorReport:
    _data = {
        "error_message": "This is test error message"
    }

    # Wrong http method
    def test_error_report1(self, client):
        url = '/ErrorReport'
        rv = client.get(url)
        rv.status_code == 405

    # Wrong url test
    def test_error_report2(self, client):
        url = '/errorreport'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data))
        rv.status_code == 404

    # Wrong url test
    def test_error_report2(self, client):
        url = '/errorr'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data))
        rv.status_code == 404

    # Right input and url
    # It will connect successfully
    def test_error_report3(self, client):
        url = '/ErrorReport'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data))
        rv.status_code == 200

class TestModuleInfo:
    _data_Civil_Engineering = {
        "facultyname": "FOSE",
        "coursename": "Civil Engineering"
    }
    _data_Computer_Science = {
        "facultyname": "FOSE",
        'coursename': "Computer Science"
    }
    _data_Computer_Science_with_Artificial_Intelligence = {
        "facultyname": "FOSE",
        'coursename': "Computer Science with Artificial Intelligence"
    }
    _data_Economics = {
        "facultyname": "FHSS",
        'coursename': "Economics"
    }
    _data_Electrical_and_Electronic_Engineering = {
        "facultyname": "FOSE",
        'coursename': "Electrical and Electronic Engineering"
    }
    _data_Aerospace_Engineering = {
        "facultyname": "FOSE",
        'coursename': "Aerospace Engineering"
    }
    _data_Architectural_Environment_Engineering = {
        "facultyname": "FOSE",
        'coursename': "Architectural Environment Engineering"
    }
    _data_Architecture = {
        "facultyname": "FOSE",
        'coursename': "Architecture"
    }
    _data_Chemical_Engineering = {
        "facultyname": "FOSE",
        'coursename': "Chemical Engineering"
    }
    _data_Chemistry = {
        "facultyname": "FOSE",
        'coursename': "Chemistry"
    }
    _data_English_Language_and_Applied_Linguistics = {
        "facultyname": "FHSS",
        'coursename': "English Language and Applied Linguistics"
    }
    _data_English_Language_and_Literature = {
        "facultyname": "FHSS",
        'coursename': "English Language and Literature"
    }
    _data_English_with_International_Business = {
        "facultyname": "FHSS",
        'coursename': "English with International Business"
    }
    _data_Environmental_Engineering = {
        "facultyname": "FOSE",
        'coursename': "Environmental Engineering"
    }
    _data_Environmental_Sciences = {
        "facultyname": "FOSE",
        'coursename': "Environmental Sciences"
    }
    _data_Finance_Accounting_and_Management = {
        "facultyname": "FOB",
        'coursename': "Finance, Accounting and Management"
    }
    _data_International_Business_Economics = {
        "facultyname": "FOB",
        'coursename': "International Business Economics"
    }
    _data_International_Business_Management = {
        "facultyname": "FOB",
        'coursename': "International Business Management"
    }
    _data_International_Business_with_Communication_Studies = {
        "facultyname": "FOB",
        'coursename': "International Business with Communication Studies"
    }
    _data_International_Business_with_Language = {
        "facultyname": "FOB",
        'coursename': "International Business with Language"
    }
    _data_International_Communications_Studies = {
        "facultyname": "FHSS",
        'coursename': "International Communications Studies"
    }
    _data_International_Communications_Studies_with_Chinese = {
        "facultyname": "FHSS",
        'coursename': "International Communications Studies with Chinese"
    }
    _data_International_Economics_and_Trade = {
        "facultyname": "FHSS",
        'coursename': "International Economics and Trade"
    }
    _data_International_Studies = {
        "facultyname": "FHSS",
        'coursename': "International Studies"
    }
    _data_International_Studies_with_Spanish_German_French_Japanese_Chinese = {
        "facultyname": "FHSS",
        'coursename': "International Studies with Spanish German French Japanese Chinese"
    }
    _data_Mathematics_with_Applied_Mathematics = {
        "facultyname": "FOSE",
        'coursename': "Mathematics with Applied Mathematics"
    }
    _data_Mechanical_Engineering = {
        "facultyname": "FOSE",
        'coursename': "Mechanical Engineering"
    }
    _data_Product_Design_and_Manufacture = {
        "facultyname": "FOSE",
        'coursename': "Product Design and Manufacture"
    }
    _data_Statistics = {
        "facultyname": "FOSE",
        'coursename': "Statistics"
    }
    headers = {"Content-Type": "application/json; charset=UTF-8"}

    # Wrong http method
    def test_course_info1(self, client):
        url = '/faculty/course/module'
        rv = client.get(url)
        assert rv.status_code == 405

    # Wrong url test
    # It will return a 404 bad request
    def test_course_info2(self, client):
        url = '/faculty'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Civil_Engineering))
        assert rv.status_code == 404

    # Wrong url test
    # It will return a 404 bad request
    def test_course_info3(self, client):
        url = '/course'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Civil_Engineering))
        assert rv.status_code == 404

    # Wrong input
    # It will raise a TypeError
    def test_course_info4(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "civil Engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info5(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "computer Science"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info6(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FHss", "coursename": "economics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info7(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOSe", "coursename": "electrical and electronic engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info8(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "aerospace engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info9(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOSe", "coursename": "architectural environment engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info10(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "architecture"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info11(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "chemical engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info12(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOSe", "coursename": "computer science with artificial intelligence"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info13(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "chemistry"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info14(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FHss", "coursename": "english language and applied linguistics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info15(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FHss", "coursename": "english language and literature"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info16(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FHss", "coursename": "english with international business"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info17(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "environmental engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info18(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "environmental sciences"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info19(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOb", "coursename": "finance, accounting and management"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info20(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOb", "coursename": "international business economics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info21(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOb", "coursename": "international business management"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info22(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOb", "coursename": "international business with communication studies"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info23(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOb", "coursename": "iternational business with language"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info24(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FHss", "coursename": "international communications studies"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info25(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FHss", "coursename": "international communications studies with chinese"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info26(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FHss", "coursename": "international economics and trade"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info27(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FHss", "coursename": "international studies"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info28(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FHss", "coursename": "international studies with spanish german french japanese chinese"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info29(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json',
                        data='{"facultyname": "FOSe", "coursename": "mathematics with applied mathematics"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info30(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "mechanical engineering"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info31(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "product design and manufacture"}')

    # Wrong input
    # It will raise a TypeError
    def test_course_info32(self, client):
        with pytest.raises(TypeError):
            url = '/faculty/course/module'
            client.post(url, content_type='application/json', data='{"facultyname": "FOSe", "coursename": "statistics"}')

    # Right input and url
    # It will connect successfully
    def test_course_info33(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Civil_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info34(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Computer_Science))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info35(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_Computer_Science_with_Artificial_Intelligence))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info36(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Economics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info37(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_Electrical_and_Electronic_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info38(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Aerospace_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info39(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_Architectural_Environment_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info40(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Architecture))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info41(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Chemical_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info42(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Chemistry))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info43(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_English_Language_and_Applied_Linguistics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info44(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_English_Language_and_Literature))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info45(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_English_with_International_Business))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info46(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Environmental_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info47(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Environmental_Sciences))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info48(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_Finance_Accounting_and_Management))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info49(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Business_Economics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info50(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Business_Management))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info51(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Business_with_Communication_Studies))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info52(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Business_with_Language))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info53(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Communications_Studies))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info54(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Communications_Studies_with_Chinese))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info55(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Economics_and_Trade))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info56(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_International_Studies))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info57(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_International_Studies_with_Spanish_German_French_Japanese_Chinese))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info58(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_Mathematics_with_Applied_Mathematics))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info59(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Mechanical_Engineering))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info50(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json',
                         data=json.dumps(self._data_Product_Design_and_Manufacture))
        assert rv.status_code == 200

    # Right input and url
    # It will connect successfully
    def test_course_info61(self, client):
        url = '/faculty/course/module'
        rv = client.post(url, content_type='application/json', data=json.dumps(self._data_Statistics))
        assert rv.status_code == 200


# class TestClass:
#         def test_one(self):
#             x = "this"
#             assert 'h' in x
#
#         def test_two(self):
#             x = "hello"
#             assert hasattr(x, 'check')
#
#         def test_three(self):
#             a = "hello"
#             b = "hello world"
#             assert a in b

if __name__ == "__main__":
    pytest.main('-q test_sample.py')
