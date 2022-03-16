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
moduleName: 'Hydraulic Design and Experiments',
year: 'Academic Year 2022',
credit: '20.00',
level: '3',
targetStudents: 'Part II Civil Engineering students',
offeringSchool: 'Department of Civil Engineering',
taughtSemesters: 'Spring China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Fangfang Zhu',
generalFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><table border="0" cellpadding="0" cellspacing="0" style="border: currentColor; border-image: none; border-collapse: collapse;"> <tbody> <tr> <td style="padding: 0in 5.4pt; border: rgb(0, 0, 0); border-image: none; width: 425px; vertical-align: top;"><p><span style="font-size: 9pt;"><span style="font-family: arial,sans-serif;"><span style="color: rgb(81, 81, 81);">1. To introduce principles of urban drainage systems, river flow and flooding as well as water supply.</span></span></span></p><p style="margin: 0in 0in 8pt; line-height: normal;"><span style="font-size: 9pt;"><span style="font-family: arial,sans-serif;"><span style="color: rgb(81, 81, 81);">2. To provide to students the tools for designing basic hydraulic systems including water supply and drainage systems, </span></span></span><span style="font-size: medium;"><span style="font-family: calibri;">or</span></span><span style="font-size: 9pt;"><span style="font-family: arial,sans-serif;"><span style="color: rgb(81, 81, 81);"> flows at sluice gates.</span></span></span></p><p style="margin: 0in 0in 8pt; line-height: normal;"><span style="font-size: 9pt;"><span style="font-family: arial,sans-serif;"><span style="color: rgb(81, 81, 81);">3. To illustrate the students how to apply important empirical concepts in  hydraulics to laboratory scale experiments.</span></span></span></p><p style="margin: 0in 0in 8pt; line-height: normal;"><span style="font-size: 9pt;"><span style="font-family: arial,sans-serif;"><span style="color: rgb(81, 81, 81);">4. To develop technical experimental skills, team-work and critical report writing skills in the students.</span></span></span></p><p style="margin: 0in 0in 0pt; line-height: normal;"><span style="color: rgb(81, 81, 81); font-family: "Arial",sans-serif; font-size: 9pt; mso-fareast-font-family: "Times New Roman";"> </span></p></td> </tr> </tbody></table></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">On successfully completing the module, students will be able to:</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Understand urban drainage systems, river flow and flooding as well as water supply.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Design drainage and water supply systems.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Quantify the flow structure at sluice gates, weirs and bridge piers.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Make experimental observation and compare them with empirical formula.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Work effectively in a team.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Develop data analysis skills through the assessment of errors associated with experiments.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">This module will contribute to the following programme learning outcome: (see Programme Specification for descriptions of learning outcomes)</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> •Knowledge and understanding of: </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">SM1, SM2, SM3</span></span></span><br><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> •Intellectual Skills to: </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">EA1, EA2, EA3,</span></span></span></p><p style="line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Design to: DD2, DD3, DD4, DD5, DD6</span></span></span><br><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> •Professional/Practical Skills</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;"> to</span></span></span>: <span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">EE1, EE2, EE6</span></span></span></p><p><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">Engineering practice to: EP1, EP2, EP3, EP4, EP6, EP8, EP11</span></span></span><br><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> •Transferable/Key Skills to: </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">GS1, GS4</span></span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">This module introduces students to real-world hydraulic applications and designs using the theory that they learnt in Hydraulics 1 and 2. The topics covered include:</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Urban drainage system: Hydrological cycle, rainfall, runoff, types of sewer systems, stormwater sewer design, foulwater sewer design, sustainable urban drainage system (SUDS).</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•River flow and flooding: Rainfall, runoff and hydrographs, river flows, flow measurement, flood prediction, flood effects and protection.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Water supply</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">: Hardy Cross method</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">.</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•The following </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">three</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> themes will be taught in detail in the lab, on an individual field trip and in coursework:</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Open channel flow (sluice gate with hydraulic jump, </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">broad crested </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">weir flow),</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•Pipe flow (</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">pipe flow</span></span></span> <span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">losses, </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">impact of a jet</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">) and</span></span></span></p><p style="line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">River flow</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> (</span></span></span>  <span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">V</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">enturi flume, </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> scour at</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> bridge pier</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">s</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">).</span></span></span></p><p><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">•The assessment will be via coursework only. Specifically, there will be group report</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">s with </span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">peer-assessment</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> in coursework 1</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">,</span></span></span> <span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">2 and 3. I</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">ndividual </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> design</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> reports</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> will be written</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> in semi-formal writing sessions in coursework </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">4</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">, </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">5</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> and </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">6</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">;  will contain in addition a</span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;"> lab </span></span></span><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">contribution-related grade.</span></span></span></p></div>',
assessmentFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}, {
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '4 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '20.00',
requirements: '<span class="PSLONGEDITBOX" id="UN_QA_CRSE_ASAI_SSR_DESCRLONG$0">Urban drainage and water supply (group work with peer assessment)</span>'
}, {
type: 'Coursework 2',
weight: '20.00',
requirements: '<span class="PSLONGEDITBOX" id="UN_QA_CRSE_ASAI_SSR_DESCRLONG$0">Urban drainage and water supply (group work with peer assessment)</span>'
}, {
type: 'Exam',
weight: '60.00',
requirements: '2.5 hours exam'
}],
staffOffice: 'Room 313, Sir Peter Mansfield Building',
staffAddress: '199 Taikang East Road, Ningbo, 315100, China',
staffCampus: 'University of Nottingham Ningbo China',
staffTelephone: '+86 (0) 574 8818 0000-9059',
staffDepartment: 'Faculty of Science and Engineering'
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
