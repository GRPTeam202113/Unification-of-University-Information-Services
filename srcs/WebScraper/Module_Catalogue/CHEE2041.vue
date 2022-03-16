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
moduleName: 'Environmental Assessment',
year: 'Academic Year 2022',
credit: '20.00',
level: '2',
targetStudents: 'Students registered in the Department of Chemical and Environmental Engineering only.',
offeringSchool: 'Department of Chemical and Environmental Engineeri',
taughtSemesters: 'Full year China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Yong Sun',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p style="margin: 0in 0in 0pt; text-align: justify; line-height: 150%;"><span style="color: black; line-height: 150%; font-family: "Verdana",sans-serif; font-size: 9pt; mso-fareast-font-family: "Arial Unicode MS"; mso-bidi-font-family: Arial;">This module will enable students to undertake Environmental Assessment in the form of Site Investigation and Environmental Impact Assessment.</span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">A1.2.4 Have a basic understanding of relevant elements from engineering disciplines commonly associated with chemical engineering</span></span></p><ul> <li style="text-align: justify; font-style: italic; font-weight: normal;"><em><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Integration of knowledge and understanding to complete a phase 1 site investigation</span></span></em></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="letter-spacing: -0.45pt;"><span style="font-family: verdana,sans-serif;"><span style="color: rgb(6, 5, 5);"><span style="font-size: medium;">A2.5.2 -</span></span></span></span><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Understand the inter-dependence of elements of a complex system and be able to synthesise such systems by integrating process steps into a sequence and applying analysis techniques.</span></span></span></p><p style="text-align: justify;"> </p><ul> <li style="text-align: justify; font-weight: normal;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Plan, undertake and report on inherently complex environmental impact and risk assessment tasks (phase 2 site investigation and an EIA)</span></span></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">A2.6.0.3 Understand methods of identifying process hazards (e.g. HAZOP), and of assessing environmental impact.</span></span></span></p><p style="text-align: justify;"> </p><ul> <li style="text-align: justify; font-weight: normal;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Undertake an Environmental Impact Assessment</span></span></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">A2.6.0.5 Have knowledge of the local legislative framework and how it is applied to the management of safety, health and environment in practice and in the workplace, from the perspectives of all involved, including operators, designers, contractors, researchers, visitors and the public.</span></span></span></p><p style="text-align: justify;"> </p><ul> <li style="text-align: justify; font-style: italic; font-weight: normal;"><em><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Generation of a conceptual site model of source-pathway-receptor and risk assessment</span></span></em></li> <li style="text-align: justify; font-weight: normal;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Consider local legislative frameworks in the context of an Environmental Impact Assessment</span></span></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">A2.7.0.1 Understand the principles of sustainability (environmental, social and economic) and be able to apply techniques for analysing, throughout the lifecycle, the interaction of process, product and plant with the environment.</span></span></span></p><p style="text-align: justify;"> </p><ul> <li style="text-align: justify; font-weight: normal;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Consider environmental, social and economic impact within the context Environmental Impact Assessment and Site Investigation.</span></span></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">A2.7.0.2 Understand and be able to apply the main methods of minimizing the environmental impact on air, water, land, and integrated eco-systems, including waste minimization at source and ‘end-of-pipe’ methods.</span></span></span></p><p style="text-align: justify;"> </p><ul> <li style="text-align: justify; font-weight: normal; margin-top: 0in; margin-bottom: 0pt;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Design mitigation measures as part of an Environmental Impact Assessment.</span></span></span></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">A3.2.4 Be aware of the importance of codes of practice and industry standards and have some experience of applying them</span></span></p><ul> <li style="text-align: justify; font-style: italic; font-weight: normal;"><em><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Application of the BS5930-2015 for site investigation</span></span></em><span style="margin: 63px auto auto 87px; left: 0px; width: 620px; height: 2px; position: absolute; z-index: 251658240;"><img height="2" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAACCAYAAADl9IAmAAAAAXNSR0ICQMB9xQAAAAlwSFlzAAAOxAAADsQBlSsOGwAAABl0RVh0U29mdHdhcmUATWljcm9zb2Z0IE9mZmljZX/tNXEAAAAsSURBVFjD7dY5EQBADMSwpR5kgXbPhEQKFTIGp6oCAMBek6SfAwDAKv1f7QJrjBO7jyOacgAAAABJRU5ErkJggg==" width="620"/></span></li></ul><p style="text-align: justify;"> </p><p style="text-align: justify;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">A4.3.2 Be able to work with information that may be incomplete or uncertain, quantify the effect of this on the design and, where appropriate, use theory or experimental research to mitigate deficiencies</span></span></span><span style="font-size: 9pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">.</span></span></span></p><p style="text-align: justify;"> </p><ul> <li style="text-align: justify; font-style: italic; font-weight: normal;"><em><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;">Use of technical literature to complete a phase 1 site investigation</span></span></em></li> <li style="text-align: justify; font-style: italic; font-weight: normal;"><span style="font-size: 10pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Evaluate risk using inherently uncertain or incomplete data and modify design decision on this basis within the context of an Environmental Impact Assessment</span></span></span></li></ul></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="text-align: justify; line-height: 115%;"><span style="font-size: 9pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The course develops through practical application an understanding of the principles and methods of Environmental Assessment. In semester 1 the course provides a structured approach to site investigation, methods of assessing risk on a site and how to interpret and presenting findings.  It will include: the basis of site investigations, safety, technique selection, data interpretation and reporting; sampling methods for soils, rocks and water, interpretation and reporting. Semester 2 prepares the students for a practical field experience in environmental impact assessment, site investigation, safety in practice, and inherently safe design. On the field course groups of students plan, manage and undertake field tasks in site investigation and environmental impact assessment. The tasks are open ended challenges some of which involve budgeting and technique selection.</span></span></span></p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '21 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Report 1',
weight: '8.00',
requirements: 'Map collation and annotation report.'
}, {
type: 'Report 2',
weight: '8.00',
requirements: 'Field observation report.'
}, {
type: 'Report 3',
weight: '24.00',
requirements: 'Part 1 Site Investigation Report.'
}, {
type: 'Assignment 1',
weight: '60.00',
requirements: 'Field course.'
}],
staffOffice: 'Room 315, Sir Peter Mansfield Building',
staffAddress: '199 Taikang East Road, Ningbo, 315100, China',
staffCampus: 'University of Nottingham Ningbo China',
staffTelephone: '+86 (0) 574 88180000 (ext 8766)',
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
