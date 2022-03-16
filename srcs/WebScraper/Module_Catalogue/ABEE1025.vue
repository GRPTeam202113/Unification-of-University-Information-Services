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
moduleName: 'Architectural Engineering Design 1',
year: 'Academic Year 2022',
credit: '30.00',
level: '1',
targetStudents: 'BEng (Hons) Architectural Environment Engineering Students',
offeringSchool: 'Department of Architecture and Built Environment',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Zhiang Zhang',
generalFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p style="line-height:normal;"><strong><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Aims:</span></span></span></strong></p><ul> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To provide an overview of the construction sector and the role of engineers within it.</span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To provide an introduction to how building performance can be assessed. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To introduce some of the basic design skills and techniques used by engineers. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To practice some of the communication and presentation techniques used by engineers</span></span></span></li></ul><p style="line-height:normal;"><strong><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Objectives:</span></span></span></strong></p><ul> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To develop a basic awareness of the building design process and relate this to practices observed on site visits. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To develop the ability to carry out simple assessments of the designed performance of buildings. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To develop a basic ability to use hand sketching and computer drafting tools.</span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To develop a basic ability to use programming for data analysis and modelling. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To develop a basic ability to present work through use of graphics, numerical data and text. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To practice oral presentation techniques</span></span></span></li></ul></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin-top:.75pt;margin-right:0in;margin-bottom:.75pt;margin-left:0in;line-height:normal;"><strong><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">KNOWLEDGE AND UNDERSTANDING</span></span></span></strong></p><ul> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Understanding of the construction sector and the role of engineers within this. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Understanding of how building performance can be assessed. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Understanding of computer drafting techniques and their application.</span></span></span></li></ul><p style="margin-top:.75pt;margin-right:0in;margin-bottom:.75pt;margin-left:0in;line-height:normal;"><strong><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">INTELLECTUAL SKILLS</span></span></span></strong></p><ul> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To identify key information from a large body of material. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">To make appropriate approximations to simplify real life problems to permit them to be analysed.</span></span></span></li></ul><p style="margin-top:.75pt;margin-right:0in;margin-bottom:.75pt;margin-left:0in;line-height:normal;"><strong><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">PROFESSIONAL/PRACTICAL SKILLS</span></span></span></strong></p><ul> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Experience of report writing. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Experience of hand sketching.</span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Use of drafting software. </span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Use of programming software.</span></span></span></li> <li><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Use of presentation tools and ability to practice presentation techniques.</span></span></span></li></ul><p style="margin-top:.75pt;margin-right:0in;margin-bottom:.75pt;margin-left:0in;line-height:normal;"><strong><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">TRANSFERABLE SKILLS</span></span></span></strong></p><p><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">This module provides students with the ability to evaluate problems and identify solutions using mathematical techniques.</span></span></span></p><p><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">Students will meet engineering council learning outcomes:<br>SM1    Knowledge and understanding of scientific principles and methodology necessary to underpin their education in their engineering discipline, to enable appreciation of its scientific and engineering context, and to support their understanding of relevant historical, current and future developments and technologies<br>SM3    Ability to apply and integrate knowledge and understanding of other engineering disciplines to support study of their own engineering discipline.<br>EA2    Ability to identify, classify and describe the performance of systems and components through the use of analytical methods and modelling techniques<br>EA3    Ability to apply quantitative and computational methods in order to solve engineering problems and to implement appropriate action<br>EA4    Understanding of, and the ability to apply, an integrated or systems approach to solving engineering problems<br>D1    Understand and evaluate business, customer and user needs, including considerations such as the wider engineering context, public perception and aesthetics<br>D2    Investigate and define the problem, identifying any constraints including environmental and sustainability limitations; ethical, health, safety, security and risk issues; intellectual property; codes of practice and standards<br>D3    Work with information that may be incomplete or uncertain and quantify the effect of this on the design<br>D6    Communicate their work to technical and non-technical audiences</span></span></span></p><p><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">ELS4    Understanding of the requirement for engineering activities to promote sustainable development and ability to apply quantitative techniques where appropriate<br>ELS5    Awareness of relevant legal requirements governing engineering activities, including personnel, health &amp; safety, contracts, intellectual property rights, product safety and liability issues<br>P2    Knowledge of characteristics of particular materials, equipment, processes, or products<br>P4    Understanding of the use of technical literature and other information sources<br>P8    Ability to work with technical uncertainty<br>G1    Apply their skills in problem solving, communication, working with others, information retrieval, and the effective use of general IT facilities<br>G2    Plan self-learning and improve performance, as the foundation for lifelong learning/CPD<br>G3    Plan and carry out a personal programme of work, adjusting where appropriate</span></span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="margin-bottom:12.0pt;line-height:normal;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">This module introduces:</span></span></span></p><ul> <li style="margin-bottom:12.0pt;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">an overview of the construction sector and the role of the engineers in design teams </span></span></span></li> <li style="margin-bottom:12.0pt;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">hand sketching and 2/3D computer drafting tools, and their role as an aid to the design process </span></span></span></li> <li style="margin-bottom:12.0pt;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">communication and IT skills, including programming, used by professionals involved in the design of buildings</span></span></span></li> <li style="margin-bottom:12.0pt;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:9.0pt;">the ability to carry out simple assessments of the designed performance of buildings.</span></span></span></li> <li style="margin-bottom:12.0pt;"><font color="#515151" face="arial, sans-serif"><span style="font-size: 12px;">feild trip</span></font></li></ul></div>',
assessmentFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
methodAndFrequency: [{
activity: 'Field',
numberOfWeeks: '1 week',
numberOfSessions: '1 week',
duration: '12 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '4 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Tutorial',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Workshop',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '25.00',
requirements: 'Drawing Portfolio'
}, {
type: 'Coursework 2',
weight: '25.00',
requirements: 'Poster and Presentation'
}, {
type: 'Coursework 3',
weight: '25.00',
requirements: 'Performance Report'
}, {
type: 'Coursework 4',
weight: '25.00',
requirements: 'Computing Portfolio'
}],
staffOffice: 'Room 401, Sir Peter Mansfield Building',
staffAddress: '199 Taikang East Road, Ningbo, 315100, China',
staffCampus: 'University of Nottingham Ningbo China',
staffTelephone: '+86 (0) 574 8818 0000 (ext. 8033)',
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
