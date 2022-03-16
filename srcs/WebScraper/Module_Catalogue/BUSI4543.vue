<template>
    <div class ="module">
        <h1 class="title">{{ moduleName }}</h1>
        <el-divider></el-divider>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">General Information</div>
                </span>
            </div>
        </div>
        <!-- here below are the content for general information part-->
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h4>Academic Year:</h4></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ year }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Total Credites:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ credit }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Level:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ level }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Target Students:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ targetStudents }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Offering School:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ offeringSchool }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Taught Semesters:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ taughtSemesters }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Requisites:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ requisites }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Additional Requirements:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ additionalRequirements }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Method and Frequency of Class:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <el-table
                    :data="methodAndFrequency"
                    border
                    style="width: 70%; color: black">
                    <el-table-column
                    prop="activity"
                    label="Activity"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    prop="numberOfWeeks"
                    label="Number of Weeks"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    prop="numberOfSessions"
                    label="Number of Sessions">
                    </el-table-column>
                    <el-table-column
                    prop="duration"
                    label="Duration of a session">
                    </el-table-column>
                </el-table>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Further Activity Detail:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3 v-html="generalFurtherActivityDetail"></h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <br><br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">Teaching Content</div>
                </span>
            </div>
        </div>
        <!-- here below are the content for content part-->
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Education Aims:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3 v-html="educationAims"></h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Summary Of Content:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3 v-html="summaryOfContent"></h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Learning Outcome:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3 v-html="learningOutcome"></h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <br><br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">Teaching Staff</div>
                </span>
            </div>
        </div>
        <br><br><br>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="10">
                <el-card :body-style="{ padding: '0px' }">
                    <el-row>
                        <el-col :span="12">
                            <div class="staffName">{{ staffName }}</div>
                            <div class="staffDepartment">{{ staffDepartment }}</div>
                            <div class="staffLink">
                                <el-link href="https://element.eleme.io" type="primary" target="_blank">Link to UNNC staff page</el-link>
                                <el-link href="https://element.eleme.io" type="primary" target="_blank">Link to hoogle scholar</el-link>
                            </div>
                        </el-col>
                    </el-row>
                </el-card>
            </el-col>
            <el-col :span="2"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="10">
                <el-card :body-style="{ padding: '0px' }">
                    <div class="contactTitle">Contact</div>
                    <el-row>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="3">
                            <span class="attribute"><h3>Office:</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="18">
                            <span class="contactContent"><h3>{{ staffOffice }}</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="3">
                            <span class="attribute"><h3>Campus:</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="18">
                            <span class="contactContent"><h3>{{ staffCampus }}</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="3">
                            <span class="attribute"><h3>Address:</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="18">
                            <span class="contactContent"><h3>{{ staffAddress }}</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="3">
                            <span class="attribute"><h3>Contact:</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                        <el-col :span="18">
                            <span class="contactContent"><h3>{{ staffTelephone }}</h3></span>
                        </el-col>
                        <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
                    </el-row>
                </el-card>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <br><br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">Assessment</div>
                </span>
            </div>
        </div>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Method of Assessment:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <el-table
                    :data="assessmentTable"
                    border
                    style="width: 70%; color: black">
                    <el-table-column
                    prop="type"
                    label="Assessment Type"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    prop="weight"
                    label="Weight"
                    width="180">
                    </el-table-column>
                    <el-table-column
                    prop="requirements"
                    label="Requirements">
                    </el-table-column>
                </el-table>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="3">
                <span class="attribute"><h3>Further Activity Detail:</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <el-col :span="18">
                <span class="content"><h3>{{ assessmentFurtherActivityDetail }}</h3></span>
            </el-col>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <br><br><br><br>
    </div>
</template>
<script>
    export default {
        name: 'module',
        data () {
            return {
moduleName: 'Corporate Finance',
year: 'Academic Year 2022',
credit: '20.00',
level: '4',
targetStudents: 'Core Module MSc Finance and Investment',
offeringSchool: 'Nottingham University Business School China',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Cherry Zhang',
generalFurtherActivityDetail: '<br>Lecture Hours: 11 x 3-hour <br>Recitations: 11 x 1-hour <br> <br>Total Contact Hours: 44 hours',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p><span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 10pt; mso-fareast-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-GB; mso-bidi-language: AR-SA; mso-bidi-font-family: Arial; mso-bidi-font-size: 7.0pt;">To highlight the key aspects of corporate finance and to identify current research issues and approaches</span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p><strong><span style="-ms-layout-grid-mode: line;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"><span style="font-size: small;">Learning Objectives &amp; Outcomes </span></span></span></span></strong><em><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Please tick all that apply - including at least one under each heading</span></span></span></span></em></p><p style="margin: 9pt 0in 0pt;"><strong><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Knowledge and understanding</span></span></span></span></strong>: <span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">This module develops a knowledge and understanding of:</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Finance - the sources, uses and management of finance</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> The use of accounting and other information systems for managerial applications</span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Intellectual Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p> </p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> Being able to think critically and be creative: manage the creative processes in self and others; organise thoughts, analyse, synthesise and critically appraise. This includes the capability to identify assumptions, evaluate statements in terms of evidence, detect false logic or reasoning, identify implicit values, define terms adequately and generalise appropriately</span></span></span></span></p><p> </p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> Being able to solve complex problems and make decisions: establish criteria, using appropriate decision-making techniques including identifying, formulating and solving business problems; and the ability to create, identify and evaluate options; the ability to implement and review decisions</span></span></span></span></p><p> </p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> Using information and knowledge effectively in order to abstract meaning from information and to share knowledge, including the use of quantitative skills</span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Professional Practical Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p> </p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of qualitative data, synthesis and reporting</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"> </p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of quantitative data, synthesis and reporting</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> Effective performance within team environments and the ability to recognise and utilise individuals" contributions in group processes and to negotiate and persuade or influence others; team selection, delegation, development and management.  Leadership and performance management: selecting appropriate leadership style for different situations; setting objectives, motivating, monitoring performance, coaching and mentoring</span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Transferable (key) Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p> </p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> Effective communication: networking, listening, oral and written communication of complex ideas and arguments, using a range of media, including the preparation of business reports</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"> High personal effectiveness: critical self-awareness, self-reflection and self-management; time management; conflict  resolution, displaying commercial acumen, the ability to continue to learn through reflection on practice and experience</span></span></span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p><span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 10pt; mso-fareast-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-GB; mso-bidi-language: AR-SA; mso-bidi-font-family: Arial; mso-bidi-font-size: 7.0pt;">The module covers the traditional content of a Corporate Finance course: Investment, Capital structure, and Dividend Decisions from a Shareholder Value Perspective; Capital Market Behaviour (background); Mergers; Real Options.</span></p></div>',
assessmentFurtherActivityDetail: '<br>Lecture Hours: 11 x 3-hour <br>Recitations: 11 x 1-hour <br> <br>Total Contact Hours: 44 hours',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '10 weeks',
numberOfSessions: '2 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Assignment',
weight: '30.00',
requirements: 'Group Coursework (2500 words)'
}, {
type: 'Exam 1',
weight: '70.00',
requirements: 'Two hour exam'
}],
staffOffice: '',
staffAddress: '',
staffCampus: '',
staffTelephone: '',
staffDepartment: ''
            }
        }
    }
</script>

<style scoped>
.square{
    margin-left: 20px;
    width: 90px;
    height: 90px;
}
.squareTitle{
    position: absolute;
    color:rgb(0, 0, 0);
    background-color: #F7F7F8;
    width:90%;
    padding-left:5px;
    padding-top:6px;
    padding-bottom: 6px;
    font-size:25px;
    font-weight: bolder;
}
.normalTitle {
    color:rgb(0, 0, 0);
    font-size:25px;
    font-weight: bolder;
}
.title {
    margin-top: 0;
    margin-left: 30px;
    font-size: 50px;
    font-weight: bold;
    color: rgb(0, 0, 0);
  }
.grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
.bg-purple-white {
    background: #ffffff;
}
.el-col {
    text-align: left;
}
.attribute {
    font-size: 12px;
    color:#4F6791
}
.content{
    font-size: 12px;
}
.staffName {
    font-size: 20px;
    font-weight: bolder;
    margin:10%;
}
.staffIntro {
    font-size: 15px;
    font-weight: bold;
    margin:10%;
}
.staffDepartment {
    font-size: 12px;
    margin:10%;
}
.staffLink {
    margin:10%;
}
.staffPicture {
    margin: 15%;
    width: 50%;
}
.contactTitle {
    font-size: 20px;
    font-weight: bolder;
    margin-left: 10%;
    margin-right: 10%;
    margin-top:5%;
}
.contactContent {
    font-size: 12px;
    color:rgb(123, 123, 123)
}
</style>
