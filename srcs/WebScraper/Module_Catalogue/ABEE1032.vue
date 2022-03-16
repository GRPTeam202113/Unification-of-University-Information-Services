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
moduleName: 'People Buildings Landscape',
year: 'Academic Year 2022',
credit: '10.00',
level: '1',
targetStudents: 'Students studying BEng Hons Architecture',
offeringSchool: 'Department of Architecture and Built Environment',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Wu Deng',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p style="margin-top:0in;margin-right:0in;margin-bottom:6.0pt;margin-left:.5in;background:white"><span lang="EN-GB" style="margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">The primary aim of this module is simple: to give students a thorough understanding of the impact that the built environment has on those who inhabit its spaces / places. In so doing, it affords students with the opportunity to analyse the qualities of existing built environments in some detail, as well as considering the bigger social, environmental sustainability implications of built environments. More specifically, the core aims of the module seek to:</span></p><p style="background: white; margin: 0px 0px 8px 72px; line-height: normal; text-indent: -0.25in;"><span lang="EN-GB" style="margin: 0px; color: black; font-family: Symbol; font-size: 10pt;"><span style="margin: 0px;">·<span style="font: 7pt "Times New Roman"; margin: 0px; font-size-adjust: none; font-stretch: normal;">         </span></span></span><span lang="EN-GB" style="margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">broaden students’ awareness of built environment design issues to incorporate perspectives from architecture, landscape design and the broader sustainability agenda;</span></p><p style="background: white; margin: 0px 0px 8px 72px; line-height: normal; text-indent: -0.25in;"><span lang="EN-GB" style="margin: 0px; color: black; font-family: Symbol; font-size: 10pt;"><span style="margin: 0px;">·<span style="font: 7pt "Times New Roman"; margin: 0px; font-size-adjust: none; font-stretch: normal;">         </span></span></span><span lang="EN-GB" style="margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">sensitize students to the various needs of people and to explore how built and natural environments may (or may not) meet those needs over time;</span></p><p style="background: white; margin: 0px 0px 8px 72px; line-height: normal; text-indent: -0.25in;"><span lang="EN-GB" style="margin: 0px; color: black; font-family: Symbol; font-size: 10pt;"><span style="margin: 0px;">·<span style="font: 7pt "Times New Roman"; margin: 0px; font-size-adjust: none; font-stretch: normal;">         </span></span></span><span lang="EN-GB" style="margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">introduce students to theories of environmental / behavioural psychology and their influence on built environment design;</span></p><p style="background: white; margin: 0px 0px 8px 72px; line-height: normal; text-indent: -0.25in;"><span lang="EN-GB" style="margin: 0px; color: black; font-family: Symbol; font-size: 10pt;"><span style="margin: 0px;">·<span style="font: 7pt "Times New Roman"; margin: 0px; font-size-adjust: none; font-stretch: normal;">         </span></span></span><span lang="EN-GB" style="margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">illustrate how design decisions impact more broadly on environmental, social and experiential issues (prompting sustainable thinking).</span></p><p><span lang="EN-GB" style="margin: 0px; color: black; line-height: 115%; font-family: "Arial",sans-serif; font-size: 10.5pt;">develop skills in critical thinking, communication, observation and analysis.</span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 3px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">On successful completion of the module the student will demonstrate:</span></p><ul style="margin-top:0in" type="disc"> <li style="margin: 0px 0px 3px; color: black; line-height: normal; font-family: "Arial",sans-serif; font-size: 10.5pt; font-style: normal; font-weight: normal;"><span lang="EN-GB" style="margin: 0px; font-family: "Arial",sans-serif; font-size: 10.5pt;">1. An appreciation of architecture and building engineering as professions which seek to design places for people (GC1.3; GC2.1; GC2.3, GC5.1; GC5.2; GC5.3);</span></li> <li style="margin: 0px 0px 3px; color: black; line-height: normal; font-family: "Arial",sans-serif; font-size: 10.5pt; font-style: normal; font-weight: normal;"><span lang="EN-GB" style="margin: 0px; font-family: "Arial",sans-serif; font-size: 10.5pt;">2. An awareness of the influence of the design of individual buildings and landscapes upon wider global issues and human behaviour.</span></li> <li style="margin: 0px 0px 3px; color: black; line-height: normal; font-family: "Arial",sans-serif; font-size: 10.5pt; font-style: normal; font-weight: normal;"><span lang="EN-GB" style="margin: 0px; font-family: "Arial",sans-serif; font-size: 10.5pt;">3. Knowledge of a number of theories, concepts and debates which underpin sustainable urban design, architectural practice and decision making (GC2.1; GC2.2; GC5.2, GC5.3, GC9.2);</span></li> <li style="margin: 0px 0px 3px; color: black; line-height: normal; font-family: "Arial",sans-serif; font-size: 10.5pt; font-style: normal; font-weight: normal;"><span lang="EN-GB" style="margin: 0px; font-family: "Arial",sans-serif; font-size: 10.5pt;">4. An ability to critically appraise and form considered judgements about the spatial, aesthetic, environmental and social qualities of built environment (GC 2.3)</span></li> <li style="margin: 0px 0px 3px; color: black; line-height: normal; font-family: "Arial",sans-serif; font-size: 10.5pt; font-style: normal; font-weight: normal;"><span lang="EN-GB" style="margin: 0px; font-family: "Arial",sans-serif; font-size: 10.5pt;">5. Communicate ideas in a range of formats (verbally, visually and in writing) with creativity and clarity.</span></li></ul></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 8px 48px; line-height: normal;"><span lang="EN-GB" style="background: white; margin: 0px; color: black; font-family: "Arial",sans-serif; font-size: 10.5pt;">What characterises healthy &amp; welcoming places? In this module, lectures, readings and student exercises will explore how environments can be designed to respond to a range of physical &amp; psychological needs, from the most fundamental (shelter, safety, orientation, physical health, ongoing availability of resources) through to the most sophisticated (community, identity, well-being, sense of place). Students will consider how different types of indoor &amp; outdoor spaces work. These spaces range in scale, from the qualities of individual rooms &amp; buildings through to the structure, experience and performance of public open spaces. Theories will be introduced which address the breadth and complexity of built environmental design, encompassing architecture, landscape architecture, sociology &amp; environmental psychology. This holistic way of thinking about built environments is essential as part of a sustainable design approach.</span></p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '11 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '100.00',
requirements: '&nbsp;Multiple Assessment of Place and Space&nbsp;'
}],
staffOffice: 'Room 443, Sir Peter Mansfield Building',
staffAddress: '199 Taikang East Road, Ningbo, 315100, China',
staffCampus: 'University of Nottingham Ningbo China',
staffTelephone: '+86 (0) 574 8818 0000 (ext 8543)',
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
