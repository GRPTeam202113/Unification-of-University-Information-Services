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
moduleName: 'Introduction to Academic Skills',
year: 'Academic Year 2022',
credit: '10.00',
level: '0',
targetStudents: 'Only available to students in the preliminary year on the International Student Pathways programme',
offeringSchool: 'Centre for English Language Education',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Epi Juarez',
generalFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>To introduce international students to the academic literacy skills necessary for the successful processing and production of academic discourse within a range of undergraduate-level academic contexts.</p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-family: calibri;"><em><span style="font-size: 12pt;">Knowledge and Understanding</span></em></span><span style="font-size: 12pt;"> -</span></p><ul> <li style="text-align: justify; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">Students will have developed </span></span><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">the ability to apply a range of skills and sub-skills to improve performance in academic reading;</span></span></li> <li style="text-align: justify; color: rgb(0, 0, 0); font-family: Times New Roman,serif; font-size: 10pt; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">an understanding of what is typically expected in written coursework assignments at the undergraduate level and the study approaches needed to meet these requirements;</span></span></li> <li style="text-align: justify; color: rgb(0, 0, 0); font-family: Times New Roman,serif; font-size: 10pt; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">an awareness of the grammatical structures and vocabulary appropriate to academic writing and the ability to use these in context;</span></span></li> <li style="text-align: justify; color: rgb(0, 0, 0); font-family: Times New Roman,serif; font-size: 10pt; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">an understanding of the process of writing coursework assignments and the ability to manage this effectively;</span></span></li> <li style="text-align: justify; color: rgb(0, 0, 0); font-family: Times New Roman,serif; font-size: 10pt; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">a knowledge of academic referencing conventions and the ability to apply these appropriately</span></span></li> <li style="text-align: justify; color: rgb(0, 0, 0); font-family: Times New Roman,serif; font-size: 10pt; font-weight: normal; margin-top: 0in; margin-bottom: 0pt; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">the ability to engage in academic seminar discussions.</span></span></li></ul><p style="margin: 0in 0in 0pt; text-align: justify; -ms-text-justify: inter-ideograph;"><span lang="EN-GB" style="font-size: 12pt; mso-fareast-font-family: "Times New Roman"; mso-bidi-font-style: italic;"><font color="#000000" face="Calibri"> </font></span></p><p style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-family: calibri;"><em><span style="font-size: 12pt;">Intellectual Skills -</span></em></span><span style="font-size: 12pt;"> Students will have developed a range of English language competencies within the specific skill sets of academic reading and writing, listening and note-taking, presenting and seminar discussions.   </span></p><p style="text-align: justify; -ms-text-justify: inter-ideograph;"> </p><p style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-family: calibri;"><em><span style="font-size: 12pt;">Transferable/Key Skills -</span></em></span><span style="font-size: 12pt;"> Students will have a heightened awareness of the different elements that constitute effective oral communication in the context of seminars. Through their seminar and workshop activities and their group self study they will have developed their ability to work productively as part of a team and demonstrate good interpersonal skills. Students will develop the ability to adopt a critical approach in investigation<em>.</em></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">This module develops the academic literacy skills necessary for the successful processing and production of academic discourse. It covers the following areas:</span></span></p><ul> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">the development of intensive and extensive academic reading skills </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">the purpose and organization of different academic texts </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">strategies for taking notes from written academic sources </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">systematic development of core academic vocabulary with reference to the AWL (Academic Wordlist) </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">a process-based approach to academic writing </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">sentence and paragraph structure in academic writing </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">developing academic arguments with supporting evidence </span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">understanding and applying academic referencing conventions</span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-family: calibri,sans-serif;"><span style="font-size: 14px;"><span style="font-family: arial,helvetica,sans-serif;">an awareness of how the verbal and non-verbal aspects of oral communication interact; </span></span></span></li> <li style="text-align: justify; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">The ability to engage in academic discussion using appropriate listening and speaking skills, such as turn-taking, interrupting, persuading </span></span></li> <li style="color: rgb(0, 0, 0); font-family: Times New Roman,serif; font-size: 10pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;"><span style="color: black;">building teamwork and collaboration in academic seminars</span></span></span></li> <li style="text-align: justify; font-style: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt; -ms-layout-grid-mode: char; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;"><span style="color: black;">presenting arguments/opinions effectively in oral and written contexts</span></span></span></li> <li style="font-style: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt; -ms-layout-grid-mode: char; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">the structure of lectures: identifying main and sub points</span></span></li> <li style="font-style: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt; -ms-layout-grid-mode: char; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">recognizing supporting information and topic change</span></span></li> <li style="font-style: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt; -ms-layout-grid-mode: char; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">following discourse markers and signpost language</span></span></li> <li style="text-align: justify; font-style: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt; -ms-layout-grid-mode: char; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">distinguishing key points from examples</span></span></li> <li style="text-align: justify; font-style: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt; -ms-layout-grid-mode: char; -ms-text-justify: inter-ideograph;"><span style="font-size: 12pt;"><span style="font-family: calibri,sans-serif;">making and organizing notes</span></span></li></ul></div>',
assessmentFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
methodAndFrequency: [{
activity: 'Seminar',
numberOfWeeks: '11 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Tutorial',
numberOfWeeks: '1 week',
numberOfSessions: '1 week',
duration: '30 minutes'
}, {
activity: 'Workshop',
numberOfWeeks: '11 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}],
assessmentTable: [{
type: 'Coursework',
weight: '70.00',
requirements: '<span style="font-family: &quot;Calibri&quot;,sans-serif; font-size: 12pt; mso-ascii-theme-font: minor-latin; mso-fareast-font-family: SimSun; mso-hansi-theme-font: minor-latin; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-fareast-theme-font: minor-fareast; mso-fareast-language: ZH-CN; mso-ansi-language: EN-GB; mso-bidi-language: AR-SA;"><font color="#000000">1000 word individual written assignment, based on an assigned reading list.</font></span>'
}, {
type: 'group discussion',
weight: '30.00',
requirements: '<span style="font-family: &quot;Calibri&quot;,sans-serif; font-size: 12pt; mso-ascii-theme-font: minor-latin; mso-fareast-font-family: SimSun; mso-hansi-theme-font: minor-latin; mso-bidi-font-family: &quot;Times New Roman&quot;; mso-fareast-theme-font: minor-fareast; mso-fareast-language: EN-GB; mso-ansi-language: EN-GB; mso-bidi-language: AR-SA;"><font color="#000000">10 minute group discussion task, based on reading list themes</font></span>'
}],
staffOffice: 'Trent Building 334',
staffAddress: '199 Taikang East Road, Ningbo, 315100, China',
staffCampus: 'University of Nottingham Ningbo China',
staffTelephone: '+86 0574 88180000 - 8609',
staffDepartment: 'Center for English Language Education'
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
