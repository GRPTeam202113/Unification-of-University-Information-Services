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
moduleName: 'Professional Engineering and Project 1',
year: 'Academic Year 2022',
credit: '20.00',
level: '1',
targetStudents: 'Students must be on one of the Aerospace Engineering courses H402, H40A, H400, H40B. Not available to any other students including exchange students.',
offeringSchool: 'School of Aerospace',
taughtSemesters: 'Full year China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: '',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: rgb(0, 57, 101); font-family: "Arial",sans-serif; font-size: 13.5pt;">This module aims to provide students with sufficient competence in a range of professional engineering elements and skills such that they can conduct the technical, research and project elements of the first year of the aerospace engineering course and present the outcomes appropriately.</span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: rgb(0, 57, 101); font-family: "Arial",sans-serif; font-size: 13.5pt;">By the end of the module students should be able to:</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO1 – Understand complex numbers and their use and manipulation in an aerospace engineering context</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO2 – Apply matrix algebra techniques to analyse efficiently and solve systems of equations and algebraic eigenvalue problems.</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO3 – Use extended techniques of differential and integral calculus, typically used in solving engineering problems.</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO4 - Manipulate vectors to solve geometric problems in aerospace engineering</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO5 - Understand the concepts of computation using variables and appreciate the ideas of data- types and limited precision</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO6 - Demonstrate an appreciation of the fact that computer programmes run instructions in a sequence and that the internal data within a programme can affect that sequence</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO7 - Decompose a programming problem into manageable pieces</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO8 – Plan, conduct and manage the progress of an engineering design, make and test project</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO9 – Demonstrate the capability to write a professional standard engineering report on an experiment including appropriate application of data analysis techniques</span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="margin:0px 0px 13px;line-height:normal;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">This year-long module comprises a number of elements and these are:</span></span></span></p><p style="margin:0px 0px 0px 48px;line-height:normal;text-indent:-0.25in;"><span style="font-size:13.5pt;"><span style="font-family:symbol;"><span style="color:#003965;">·        </span></span></span><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Essential professional engineering elements:, report writing, information searching, data analysis</span></span></span></p><p style="margin:0px 0px 0px 48px;line-height:normal;text-indent:-0.25in;"><span style="font-size:13.5pt;"><span style="font-family:symbol;"><span style="color:#003965;">·        </span></span></span><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Essential engineering study support elements: Maths, MATLAB, Using MS Excel, Word, Powerpoint</span></span></span></p><p style="margin:0px 0px 13px 48px;line-height:normal;text-indent:-0.25in;"><span style="font-size:13.5pt;"><span style="font-family:symbol;"><span style="color:#003965;">·        </span></span></span><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Essential project skills: team working, project management, MS Project</span></span></span></p><p style="margin:0px 0px 13px;line-height:normal;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">These skills will be covered to a level appropriate to first year aerospace engineering students.</span></span></span></p><p style="margin:0px 0px 13px;line-height:normal;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">In addition the module includes a year-long integrating group project element that draws in technical elements from the other 5 modules running in the first year of the course. An output from the project is a model scale aircraft designed to meet the specification set.</span></span></span></p><p style="margin:16px 0px;"><strong><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Method of re-assessment:</span></span></span></strong></p><p style="margin:16px 0px 8px;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Students who have not achieved a mark of 40% or above for one or more of the three in-class maths tests following the in-class re-assessment opportunity will be re-assessed by a single examination covering the entire maths syllabus. A mark of 40% or above is required on this re-assessment to pass the module.</span></span></span></p><p style="margin:16px 0px 8px;"> </p><p style="margin:16px 0px 8px;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Students who fail this module overall and are required to complete a re-assessment will be re-assessed in all failed assessment components. These failed component re-assessments will be undertaken as follows: </span></span></span></p><p style="margin:16px 0px;"> </p><p style="margin:16px 0px;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Where a student has failed one or both of the Matlab coursework components, they will complete a coursework re-assessment (20%);</span></span></span></p><p style="margin:16px 0px 16px 48px;text-align:justify;text-indent:-0.25in;text-justify:inter-ideograph;"><span style="font-size:13.5pt;"><span style="font-family:symbol;"><span style="color:#003965;">·        </span></span></span><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Where a student has failed one or more of the three in-class maths tests they will be reassessed via a single examination covering the entire maths syllabus.  (40%); </span></span></span></p><p style="margin:16px 0px 16px 48px;text-align:justify;text-indent:-0.25in;text-justify:inter-ideograph;"><span style="font-size:13.5pt;"><span style="font-family:symbol;"><span style="color:#003965;">·        </span></span></span><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Where a student has failed any number of the project coursework components (Coursework 3, Coursework 4, Coursework 5), they will complete a coursework re-assessment covering the failed learning outcomes (35%);</span></span></span></p><p style="margin:16px 0px 16px 48px;text-align:justify;text-indent:-0.25in;text-justify:inter-ideograph;"><span style="font-size:13.5pt;"><span style="font-family:symbol;"><span style="color:#003965;">·        </span></span></span><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">Where a student has failed the Lab book assessment, they will complete a coursework re-assessment (resubmission of the lab book) (5%)</span></span></span></p><p style="margin:16px 0px 16px 48px;"> </p><p style="margin:16px 0px;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">The re-assessment mark for the module will be a combination of the marks from components passed first time and the components which have been re-assessed.</span></span></span></p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Computing',
numberOfWeeks: '2 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '19 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '2 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '1 week',
numberOfSessions: '1 week',
duration: '4 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '1 week',
numberOfSessions: '1 week',
duration: '3 hours'
}],
assessmentTable: [{
type: 'MATLAB coursework 1',
weight: '10.00',
requirements: '<span lang="EN-AU" style="margin: 0px; line-height: 115%; font-family: &quot;Times New Roman&quot;,serif; font-size: 12pt;"><font color="#000000">MATLAB coursework 1</font></span>'
}, {
type: 'Coursework 6',
weight: '5.00',
requirements: '<span lang="EN-AU" style="margin: 0px; line-height: 115%; font-family: &quot;Times New Roman&quot;,serif; font-size: 12pt;"><font color="#000000">Lab books assessed</font></span>'
}, {
type: 'Matlab Coursework 2',
weight: '10.00',
requirements: '<span lang="EN-AU" style="margin: 0px; line-height: 115%; font-family: &quot;Times New Roman&quot;,serif; font-size: 12pt;"><font color="#000000">Matlab Coursework 2</font></span>'
}, {
type: 'In-class  assessment 1',
weight: '10.00',
requirements: '<span lang="EN-AU" style="margin: 0px; line-height: 115%; font-family: &quot;Times New Roman&quot;,serif; font-size: 12pt;"><font color="#000000">Maths progress test 1 (40 mins) Students must achieve a mark of 40% or above on each in-class maths progress test to pass the module. Students will be offered one in-class re-sit opportunity for each test if they do not achieve a mark of 40% or above at first attempt.</font></span>'
}, {
type: 'In-class  assessment 2',
weight: '10.00',
requirements: '<span lang="EN-AU" style="margin: 0px; line-height: 115%; font-family: &quot;Times New Roman&quot;,serif; font-size: 12pt;"><font color="#000000">Maths progress test 2 (40 mins) Students must achieve a mark of 40% or above on each in-class maths progress test to pass the module. Students will be offered one in-class re-sit opportunity for each test if they do not achieve a mark of 40% or above at first attempt.</font></span>'
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
