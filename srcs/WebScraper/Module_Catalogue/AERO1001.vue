<template>
  <div class="module">
    <h1 class="title">{{ moduleName }}</h1>
    <el-divider></el-divider>
    <div class="block">
      <div style="position: relative">
        <img class="square" src="../../assets/square.png" alt="" />
        <span
          class="squareTitle"
          style="position: absolute; bottom: 20px; left: 50px"
        >
          <div class="normalTitle">General Information</div>
        </span>
      </div>
    </div>
    <!-- here below are the content for general information part-->
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h4>Academic Year:</h4></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ year }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Total Credites:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ credit }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Level:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ level }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Target Students:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ targetStudents }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Offering School:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ offeringSchool }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Taught Semesters:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ taughtSemesters }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Requisites:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ requisites }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Additional Requirements:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ additionalRequirements }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Method and Frequency of Class:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <el-table
          :data="methodAndFrequency"
          border
          style="width: 70%; color: black"
        >
          <el-table-column prop="activity" label="Activity" width="180">
          </el-table-column>
          <el-table-column
            prop="numberOfWeeks"
            label="Number of Weeks"
            width="180"
          >
          </el-table-column>
          <el-table-column prop="numberOfSessions" label="Number of Sessions">
          </el-table-column>
          <el-table-column prop="duration" label="Duration of a session">
          </el-table-column>
        </el-table>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Further Activity Detail:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3 v-html="generalFurtherActivityDetail"></h3
        ></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <br /><br /><br /><br />
    <div class="block">
      <div style="position: relative">
        <img class="square" src="../../assets/square.png" alt="" />
        <span
          class="squareTitle"
          style="position: absolute; bottom: 20px; left: 50px"
        >
          <div class="normalTitle">Teaching Content</div>
        </span>
      </div>
    </div>
    <!-- here below are the content for content part-->
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Education Aims:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"><h3 v-html="educationAims"></h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Summary Of Content:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"><h3 v-html="summaryOfContent"></h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Learning Outcome:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"><h3 v-html="learningOutcome"></h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <br /><br /><br /><br />
    <div class="block">
      <div style="position: relative">
        <img class="square" src="../../assets/square.png" alt="" />
        <span
          class="squareTitle"
          style="position: absolute; bottom: 20px; left: 50px"
        >
          <div class="normalTitle">Teaching Staff</div>
        </span>
      </div>
    </div>
    <br /><br /><br />
    <el-row>
      <el-col :span="5"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="15">
        <el-card :body-style="{ padding: '0px' }">
          <el-row>
            <el-col :span="12">
              <div class="staffName">{{ staffName }}</div>
              <div class="staffDepartment">{{ staffDepartment }}</div>
              <div class="staffLink">
                <div @click="goPage">
                  <el-link type="primary">Link to UNNC staff page</el-link>
                </div>
              </div>
            </el-col>
          </el-row>
          <el-row>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="3">
              <span class="attribute"><h3>Office:</h3></span>
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="18">
              <span class="contactContent"
                ><h3>{{ staffOffice }}</h3></span
              >
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
          </el-row>
          <el-row>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="3">
              <span class="attribute"><h3>Campus:</h3></span>
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="18">
              <span class="contactContent"
                ><h3>{{ staffCampus }}</h3></span
              >
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
          </el-row>
          <el-row>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="3">
              <span class="attribute"><h3>Campus:</h3></span>
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="18">
              <span class="contactContent"
                ><h3>{{ staffCampus }}</h3></span
              >
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
          </el-row>
          <el-row>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="3">
              <span class="attribute"><h3>Address:</h3></span>
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="18">
              <span class="contactContent"
                ><h3>{{ staffAddress }}</h3></span
              >
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
          </el-row>
          <el-row>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="3">
              <span class="attribute"><h3>Contact:</h3></span>
            </el-col>
            <el-col :span="1"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
            <el-col :span="18">
              <span class="contactContent"
                ><h3>{{ staffTelephone }}</h3></span
              >
            </el-col>
            <el-col :span="4"
              ><div class="grid-content bg-purple-white"></div
            ></el-col>
          </el-row>
        </el-card>
      </el-col>
      <el-col :span="2"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <br /><br /><br /><br />
    <div class="block">
      <div style="position: relative">
        <img class="square" src="../../assets/square.png" alt="" />
        <span
          class="squareTitle"
          style="position: absolute; bottom: 20px; left: 50px"
        >
          <div class="normalTitle">Assessment</div>
        </span>
      </div>
    </div>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Method of Assessment:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <el-table
          :data="assessmentTable"
          border
          style="width: 70%; color: black"
        >
          <el-table-column prop="type" label="Assessment Type" width="180">
          </el-table-column>
          <el-table-column prop="weight" label="Weight" width="180">
          </el-table-column>
          <el-table-column prop="requirements" label="Requirements">
          </el-table-column>
        </el-table>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <el-row>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="3">
        <span class="attribute"><h3>Further Activity Detail:</h3></span>
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
      <el-col :span="18">
        <span class="content"
          ><h3>{{ assessmentFurtherActivityDetail }}</h3></span
        >
      </el-col>
      <el-col :span="1"
        ><div class="grid-content bg-purple-white"></div
      ></el-col>
    </el-row>
    <br /><br /><br /><br />
  </div>
</template>
<script>
export default {
  name: 'module',
  data() {
    return {moduleName: 'Aerospace Statics and Dynamics',
year: 'Academic Year 2022',
credit: '20.00',
level: '1',
targetStudents: 'Students must be on one of the Aerospace Engineering courses H402, H40A, H400, H40B.Not available to any other students including exchange students.',
offeringSchool: 'School of Aerospace',
taughtSemesters: 'Full year China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: '',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: "Arial",sans-serif; font-size: 12pt;">The aim of this module is to introduce students to the fundamental concepts and principles of dynamics and flight mechanics and their application to aerospace engineering systems.</span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin:0px 0px 13px;line-height:normal;"><span style="font-size:12pt;"><span style="font-family:arial,sans-serif;">By the end of the module students should be able to:</span></span></p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  LO1 – demonstrate comprehension of the fundamental concepts of solid mechanics. </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  LO2 – Comprehend the fundamental concepts of dynamics in an aerospace context and flight mechanics </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  LO3 – Apply these concepts to simplified engineering scenarios. </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  LO4 – recognise and construct an appropriate analysis technique to apply when presented with a simple aerospace engineering scenario in a solid mechanics context </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  LO5 – Analyse the manner in which aircraft move and are propelled by applying an understanding of basic dynamics. </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  LO6 – Record the salient details from an experimental investigation and conduct accurate and appropriate data analysis.</span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="margin:0px 0px 13px;line-height:normal;"><span style="font-size:13.5pt;"><span style="font-family:arial,sans-serif;"><span style="color:#003965;">This year-long module introduces students on the Aerospace Engineering courses to the fundamental concepts and principles of solid mechanics and dynamics. It covers their application to simple engineering scenarios in an aerospace context. <br>Topics include: </span></span></span><br><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Review of basic mechanics : vectors, units, forces and moments, Newton’s laws </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Static equilibrium: force and moment analysis in design; frictional forces </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Free body diagrams and Pin-jointed structures </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Stress, strain and elasticity </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Multi-axial stress-strain; thin walled vessels under pressure </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Shear stress and torsion of shafts </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Plane stress; Mohr circle analysis </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Beam bending: shear force &amp; bending moment diagrams </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  2nd moments of area of cross-sections </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Bending stresses in beams </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  The relationship between linear and angular motion </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Newton’s laws for linear and rotational motion </span></span><br> </p><p style="line-height:normal;"><span style="font-size:12pt;"><span style="font-family:symbol;">·</span></span><span style="font-size:12pt;"><span style="font-family:times new roman,serif;">  Linear and angular momentum include</span></span></p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '23 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '23 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '23 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '23 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Seminar',
numberOfWeeks: '23 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}],
assessmentTable: [{
type: 'Lab report for Statics Lab',
weight: '10.00',
requirements: '<span style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: DengXian; mso-fareast-theme-font: minor-fareast; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;"><strong>Lab report for Statics Lab</strong></span>'
}, {
type: 'In Class Test Semester 1',
weight: '10.00',
requirements: '<span style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: DengXian; mso-fareast-theme-font: minor-fareast; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;"><strong>In Class Test Semester 1 </strong></span>'
}, {
type: 'Dynamics lab',
weight: '10.00',
requirements: '<span style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: DengXian; mso-fareast-theme-font: minor-fareast; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;"><strong>Dynamics lab </strong></span>'
}, {
type: 'inclass test-dynamics',
weight: '10.00',
requirements: '<span style="color: black; font-family: &quot;Calibri&quot;,sans-serif; font-size: 11pt; mso-fareast-font-family: DengXian; mso-fareast-theme-font: minor-fareast; mso-ansi-language: EN-US; mso-fareast-language: ZH-CN; mso-bidi-language: AR-SA;"><strong>inclass test-dynamics&nbsp; </strong></span>'
}, {
type: 'Final Exam',
weight: '60.00',
requirements: 'Final Exam'
}],
staffOffice: '',
staffAddress: '',
staffCampus: '',
staffTelephone: '',
staffDepartment: '',
staffUrl: ''
};
  },
  methods: {
    goPage() {
      // window.location.href = this.staffUrl
      window.open(this.staffUrl, '_blank');
    }
  }
};
</script>

<style scoped>
.square {
  margin-left: 20px;
  width: 90px;
  height: 90px;
}
.squareTitle {
  position: absolute;
  color: rgb(0, 0, 0);
  background-color: #f7f7f8;
  width: 90%;
  padding-left: 5px;
  padding-top: 6px;
  padding-bottom: 6px;
  font-size: 25px;
  font-weight: bolder;
}
.normalTitle {
  color: rgb(0, 0, 0);
  font-size: 25px;
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
  color: #4f6791;
}
.content {
  font-size: 12px;
}
.staffName {
  font-size: 20px;
  font-weight: bolder;
  margin: 10%;
}
.staffIntro {
  font-size: 15px;
  font-weight: bold;
  margin: 10%;
}
.staffDepartment {
  font-size: 12px;
  margin: 10%;
}
.staffLink {
  margin: 10%;
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
  margin-top: 5%;
}
.contactContent {
  font-size: 12px;
  color: rgb(123, 123, 123);
}
</style>
