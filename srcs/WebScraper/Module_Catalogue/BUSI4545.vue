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
moduleName: 'Entrepreneurial Creativity',
year: 'Academic Year 2022',
credit: '20.00',
level: '4',
targetStudents: 'Core module for EB16 Entrepreneurship, Innovation and Management students',
offeringSchool: 'Nottingham University Business School China',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Vincent Ting-Kuei Kuo',
generalFurtherActivityDetail: '<br>Total Hours of Learning = 200 hours of student centred learning comprised of the following:<br>o44 hours class-based contact time.<br>o48 hours reading and self-directed study.<br>o48 hours individual essay preparation.<br>o20 hours individual reflection and blog preparation.<br>o40 hours team presentation preparation.',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>This module encourages students to develop an understanding of entrepreneurial creativity through:<br>◦Theoretical analysis and the use of creative problem solving techniques.<br>◦Enabling students to generate, evaluate, and apply new ideas and concepts within a business planning process.<br>◦Experiencing creative problem solving techniques, reflecting upon appropriate methods for different stages of problem solving, and exploring the relationship between creative problem solving and entrepreneurship.</p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 9pt 0in 0pt;"><strong><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Knowledge and understanding</span></span></span></span></strong>: <span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">This module develops a knowledge and understanding of:</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Markets - the development and operation of markets for resources, goods and services </span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Customers and stakeholders - customer expectations, service and orientation</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Finance - the sources, uses and management of finance</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">People – strategic  and operational HRM, meeting future organisational requirements, people development, HR systems</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The management of operations<br><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The management of projects</span></span></span></span></span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Business innovation – creativity, intrapreneurial – and entrepreneurial behaviour and enterprise development, and the management and exploitation of intellectual property  </span></span></span></span></span></span></span></span></span></span></span></span></p><p><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The importance of sustainability issues, including an understanding of the challenges </span></span></span></p><p><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Theories, models and frameworks of entrepreneurship and creativity</span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Intellectual Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Being able to think critically and be creative: manage the creative processes in self and others; organise thoughts, analyse, synthesise and critically appraise. This includes the capability to identify assumptions, evaluate statements in terms of evidence, detect false logic or reasoning, identify implicit values, define terms adequately and generalise appropriately</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Being able to solve complex problems and make decisions: establish criteria, using appropriate decision-making techniques including identifying, formulating and solving business problems; and the ability to create, identify and evaluate options; the ability to implement and review decisions</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Using information and knowledge effectively in order to abstract meaning from information and to share knowledge, including the use of quantitative skills</span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Professional Practical Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of qualitative data, synthesis and reporting</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of quantitative data, synthesis and reporting</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Effective performance within team environments and the ability to recognise and utilise individuals" contributions in group processes and to negotiate and persuade or influence others; team selection, delegation, development and management.  Leadership and performance management: selecting appropriate leadership style for different situations; setting objectives, motivating, monitoring performance, coaching and mentoring</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The ability to recognise and address ethical dilemmas, corporate social responsibility and sustainability issues, applying ethical and organisational values to situations and choices</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Leadership and performance management: Selecting appropriate leadership style for different situations; setting targets, motivating, monitoring performance, coaching and mentoring</span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Transferable (key) Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Effective communication: networking, listening, oral and written communication of complex ideas and arguments, using a range of media, including the preparation of business reports</span></span></span></span></p><p style="margin: 9.2pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">High personal effectiveness: critical self-awareness, self-reflection and self-management; time management; conflict  resolution, displaying commercial acumen, the ability to continue to learn through reflection on practice and experience</span></span></span></span></p><p style="margin: 2.35pt 0in 0pt;"><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Soft skills: understanding the needs of others and empathy towards them; sensitivity to diversity in people and in different situations</span></span></span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p>The course will introduce students to the latest thinking in the areas of creativity, the creative process, knowledge management practices and the nature of entrepreneurship. Having established the vital link between creativity, entrepreneurship, innovation and value creation, the course uses directed reading, case study exercises, reflective blog writing and group-based creative problem solving to illustrate entrepreneurial creativity in practice. Students will be introduced to a variety of creative problem solving techniques and learn how to apply these techniques in the context of the development, evaluation, and application of ideas and concepts with commercial potential. The course culminates in students pitching their identified entrepreneurial opportunity to peers and real world entrepreneurs.</p></div>',
assessmentFurtherActivityDetail: '<br>Total Hours of Learning = 200 hours of student centred learning comprised of the following:<br>o44 hours class-based contact time.<br>o48 hours reading and self-directed study.<br>o48 hours individual essay preparation.<br>o20 hours individual reflection and blog preparation.<br>o40 hours team presentation preparation.',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '10 weeks',
numberOfSessions: '2 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '50.00',
requirements: 'Individual essay (3,500 words)'
}, {
type: 'Coursework 2',
weight: '15.00',
requirements: '5x Individual reflective blogs published online (2,000 words split across 5x 400 words)'
}, {
type: 'Presentation',
weight: '35.00',
requirements: 'Group Presentation (5 mins + 10 mins Q&amp;A, with submission of PowerPoint slides &amp; 500 word business plan).'
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
