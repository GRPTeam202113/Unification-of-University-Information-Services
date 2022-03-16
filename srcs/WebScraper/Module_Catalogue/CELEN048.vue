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
moduleName: 'Undergraduate Reading and Writing in Academic Contexts',
year: 'Academic Year 2022',
credit: '20.00',
level: '0',
targetStudents: 'UNNC Preliminary Year students only',
offeringSchool: 'Centre for English Language Education',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Ms Holly Nelson',
generalFurtherActivityDetail: '<br>6 hours of classroom contact per week (3 x 2 hour seminars), supplemented by a further 140 hours of self-directed study.',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p><span lang="EN-GB" style="font-family: "Calibri",sans-serif; font-size: 11pt; mso-fareast-font-family: SimSun; mso-fareast-theme-font: minor-fareast; mso-bidi-font-family: Arial; mso-bidi-theme-font: minor-bidi; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;"><font color="#000000">To equip students with the requisite language, strategies and skills that will enable them to read and write within a range of undergraduate-level academic contexts.</font></span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">Knowledge and Understanding </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• the ability to apply a range of skills and sub-skills to improve their performance in academic reading. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• an understanding of what is typically expected in written examinations and coursework assignments at the undergraduate level and the study approaches needed to meet these requirements. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• a knowledge of 2 specific types of examination essay questions that are commonly encountered in British higher education and an understanding of how to approach them. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• an understanding of how to format and structure academic written work. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• an awareness of the grammatical structures and vocabulary appropriate to academic writing and the ability to use these in context. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• an understanding of the process of writing coursework assignments and the ability to manage this effectively. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• a knowledge of academic referencing conventions and the ability to apply these appropriately. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• the ability to read and write effectively under timed conditions.</font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3"> </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">Intellectual Skills </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• critical thinking, analysis and synthesis.</font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3"> </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">Transferable/Key Skills </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• the ability to apply appropriate reading strategies in order to comprehend written academic discourse. </font></span></p><p style="margin: 0in 0in 0pt;"><span lang="EN-GB"><font color="#000000" face="Calibri" size="3">• the ability to present and communicate ideas and arguments effectively in written contexts.</font></span></p><p> </p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="line-height: normal;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">This module focuses on developing the core strategies, skills and language that will enable students to read and write within a range of undergraduate-level academic contexts. It covers the following areas: </span></span></span></p><ul> <li style="line-height: normal; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">the development of intensive and extensive academic reading skills </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">the purpose and organisation of different academic texts </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">understanding academic texts </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">strategies for taking notes from written academic sources </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">systematic development of core academic vocabulary with reference to the AWL (Academic Wordlist) </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">sentence and paragraph structure in academic writing </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">developing descriptive academic writing with supporting evidence </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">dealing with two specific types of examination essay questions: define and compare/contrast </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">understanding and applying basic academic referencing conventions </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">a progress-based approach to academic summary writing </span></span></span></li> <li style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"><span style="font-size: 12pt;"><span style="font-family: times new roman,serif;"><span style="color: rgb(0, 57, 101);">using a variety of study aids (dictionaries; thesauri; corpora) </span></span></span><p style="color: rgb(0, 0, 0); line-height: normal; font-family: Calibri,sans-serif; font-size: 11pt; font-weight: normal; margin-top: 0cm; margin-bottom: 0pt;"> </p></li></ul><p> </p><p> </p><p> </p><p> </p></div>',
assessmentFurtherActivityDetail: '<br>6 hours of classroom contact per week (3 x 2 hour seminars), supplemented by a further 140 hours of self-directed study.',
methodAndFrequency: [{
activity: 'Seminar',
numberOfWeeks: '12 weeks',
numberOfSessions: '3 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Assignment 1',
weight: '60.00',
requirements: '1 x 1,000-word coursework individual essay [sources provided]'
}, {
type: 'Exam 1',
weight: '40.00',
requirements: '<span lang="EN-GB" style="color: rgb(0, 57, 101); line-height: 115%; font-family: &quot;Times New Roman&quot;,serif; font-size: 12pt; mso-fareast-font-family: &quot;Times New Roman&quot;; mso-ansi-language: EN-GB; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;">90 minute reading and writing exam held at the end of semester.</span>'
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
