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
moduleName: 'Oral Communication Skills A',
year: 'Academic Year 2022',
credit: '10.00',
level: '0',
targetStudents: 'UNNC Preliminary Year students only',
offeringSchool: 'Centre for English Language Education',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Mr David Anstey',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p><span lang="EN-GB" style="color: black; font-family: "Calibri",sans-serif; font-size: 11pt; mso-fareast-font-family: "Times New Roman"; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-themecolor: text1;">To equip students with the necessary language, strategies and skills for understanding academic lectures, taking notes and both participating in and delivering academic discussions and presentations </span><span lang="EN-GB" style="color: black; font-family: "Calibri",sans-serif; font-size: 11pt; mso-fareast-font-family: SimSun; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-themecolor: text1;">in undergraduate academic contexts</span><span lang="EN-GB" style="color: black; font-family: "Calibri",sans-serif; font-size: 11pt; mso-fareast-font-family: "Times New Roman"; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-themecolor: text1;">. </span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="-ms-layout-grid-mode: char;"><em><span style="color: black;"><span style="font-size: medium;"><span style="font-family: calibri;">a) Knowledge and Understanding</span></span></span></em></p><ul> <li style="line-height: normal; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><span style="line-height: 107%; font-family: "Verdana",sans-serif; font-size: 10pt; mso-fareast-font-family: DengXian; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-theme-font: minor-bidi; mso-bidi-font-size: 11.0pt;"><font color="#000000">effective listening and note-making strategies to assist them in their comprehension of academic lectures.</font></span><em><span style="color: black;">.</span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><span style="line-height: 107%; font-family: "Verdana",sans-serif; font-size: 10pt; mso-bidi-font-size: 11.0pt;"><font color="#000000">the ability to re-formulate lecture notes for use in other academic contexts. </font></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><span style="line-height: 107%; font-family: "Verdana",sans-serif; font-size: 10pt; mso-bidi-font-size: 11.0pt;"><font color="#000000">a greater awareness of English pronunciation, intonation and rhythmic variations. </font></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><p style="margin: 0in 0in 8pt;"><span style="line-height: 107%; font-family: "Verdana",sans-serif; font-size: 10pt; mso-bidi-font-size: 11.0pt;"><font color="#000000">the ability to cope with a variety of English accents and different speeds of speech. </font></span></p></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><span style="line-height: 107%; font-family: "Verdana",sans-serif; font-size: 10pt; mso-bidi-font-size: 11.0pt;"><font color="#000000">an awareness of how the verbal and non-verbal aspects of oral communication interact.</font></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><span style="line-height: 107%; font-family: "Verdana",sans-serif; font-size: 10pt; mso-fareast-font-family: DengXian; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA; mso-bidi-theme-font: minor-bidi; mso-bidi-font-size: 11.0pt;"><font color="#000000">understanding of interaction strategies and conventions for academic discussions</font></span></li></ul><p style="-ms-layout-grid-mode: char;"><em><span style="color: black;"><span style="font-size: medium;"><span style="font-family: calibri;">b) Intellectual Skills</span></span></span></em></p><ul> <li style="line-height: normal; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><em><span style="color: black;">critical thinking, analysis and synthesis. </span></em></li></ul><p style="-ms-layout-grid-mode: char;"><em><span style="color: black;"><span style="font-size: medium;"><span style="font-family: calibri;">c) Transferable/Key Skills</span></span></span></em></p><ul> <li style="line-height: normal; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><em><span style="color: black;">the ability to apply listening strategies in order to comprehend spoken academic discourse.</span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><em><span style="color: black;">the ability to process academic lectures into a set of organized notes.</span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><em><span style="color: black;">the ability to communicate ideas and arguments effectively in oral contexts and to evaluate and respond appropriately to those of others.</span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><em><span style="color: black;">skills for supportive and collaborative teamwork, </span></em><em><span style="color: black;">the capacity for effective group work and sharing responsibility within a team</span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><em><span style="color: black;">increased confidence in public speaking. </span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><em><span style="color: black;">the ability to present and communicate ideas in a structured and logical manner. </span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><em><span style="color: black;">the ability to formulate and develop rational arguments in order to persuade others.</span></em></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-style: normal; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-layout-grid-mode: char;"><em><span style="color: black;">the ability to evaluate the validity of others’ arguments and identify bias.</span></em></li></ul><p><em><span style="font-size: 11pt;"><span style="font-family: calibri,sans-serif;"><span style="color: black;">the ability to work independently and demonstrate time management skills.</span></span></span></em></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p><span lang="EN-GB" style="color: black; font-family: "Calibri",sans-serif; font-size: 11pt; mso-fareast-font-family: SimSun; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: "Times New Roman"; mso-themecolor: text1; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;">This module focuses on the development of appropriate language, strategies and skills for understanding academic lectures, taking effective notes and participating in seminar discussions at an undergraduate level.It covers the following areas: understanding the purpose, structure and organization of academic lectures / using discourse markers as an aid to listening comprehension / identifying and summarizing the main points of a lecture / recognizing salient features of pronunciation and intonation / different strategies for and approaches to note-taking / sub-skills of effective note-taking e.g. using symbols and abbreviations / re-formulating and making active use of notes / developing fluency, clear pronunciation, intonation and rhythm in spoken discourse / characteristics of successful participation in seminar discussions / developing ability to discuss content in academic discussion / presenting opinions in academic discussions / agreeing and disagreeing in academic discussions / participating in group discussions/presentations</span></p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Seminar',
numberOfWeeks: '12 weeks',
numberOfSessions: '2 week',
duration: '2 hours'
}, {
activity: 'Seminar',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}],
assessmentTable: [{
type: 'group discussion',
weight: '40.00',
requirements: '<span lang="EN-GB" style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: SimSun; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-themecolor: text1; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;">1x end-of-semester group discussion</span>'
}, {
type: 'Coursework1',
weight: '20.00',
requirements: '<span lang="EN-GB" style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: SimSun; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-themecolor: text1; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;">5x submitted lecture notes @ 2% each</span>'
}, {
type: 'Exam1',
weight: '40.00',
requirements: '<span lang="EN-GB" style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: SimSun; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-themecolor: text1; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;">1x end of semester listening exam</span>'
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
