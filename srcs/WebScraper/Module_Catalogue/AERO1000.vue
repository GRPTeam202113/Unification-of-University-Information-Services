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
    return {moduleName: 'Aerospace Design and Materials',
year: 'Academic Year 2022',
credit: '20.00',
level: '1',
targetStudents: 'Students must be on one of the Aerospace Engineering Courses H402, H40A, H400, H40B. Not available to any other students including exchange students.',
offeringSchool: 'School of Aerospace',
taughtSemesters: 'Full year China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: '',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: rgb(0, 57, 101); font-family: "Arial",sans-serif; font-size: 13.5pt;">On successful completion of the module students will understand the key stages of the design process and be able to apply and integrate knowledge from other areas to support their designs. Students will acquire manufacturing know-how by doing and by demonstration. Students will acquire skills in both the generation of mechanical system design and the communication of those designs to a wider audience.</span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: rgb(0, 57, 101); font-family: "Arial",sans-serif; font-size: 13.5pt;">On successful completion of this module students will be able to:</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO1 – Demonstrate understanding of the process of aircraft design and testing</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO2 – Operate a computer aided engineering package to develop designs</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO3 – Design and analyse rudimentary aerospace systems, parts and assemblies</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO4 – Communicate design intent through 2D drawings and 3D models</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO5 – Describe basic mechanical elements and their function</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>LO6 – Use machine tools safely to manufacture mechanical systems</span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: rgb(0, 57, 101); font-family: "Arial",sans-serif; font-size: 13.5pt;"> </span></p><p style="margin: 0px 0px 13px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; color: rgb(0, 57, 101); font-family: "Arial",sans-serif; font-size: 13.5pt;">This year long module introduces students on the Aerospace Engineering courses to the basic concepts and practices of design and manufacture in an aerospace context and includes the following topics:</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>The process of concept generation through to detail design in an aerospace context</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>The use of computer aided engineering tools in the design processes</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Part and assembly design using CATIA</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Basic machine elements and their function</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Properties and mechanical behaviour of materials</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Materials selection as part of the design process</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>How materials, stress analysis and manufacturing disciplines fit within the framework of design</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Machining processes and metrology</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Lab-based demonstration of manufacturing processes</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>Machine shop practical training</span></p><p style="margin: 0px; line-height: normal;"><span lang="EN-GB" style="margin: 0px; font-family: Symbol; font-size: 12pt;">·</span><span lang="EN-GB" style="margin: 0px; font-family: "Times New Roman",serif; font-size: 12pt;"><span style="margin: 0px;">  </span>An appreciation of modern working practices - interaction with technical staff and conveying design intent</span></p><p> </p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '18 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '17 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '17 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Workshop',
numberOfWeeks: '1 week',
numberOfSessions: '5 week',
duration: '3 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '10.00',
requirements: 'Individual part design project'
}, {
type: 'Laboratory',
weight: '10.00',
requirements: ' '
}, {
type: 'Coursework 2',
weight: '10.00',
requirements: 'Individual assembly design project'
}, {
type: 'CAE in-class test',
weight: '10.00',
requirements: 'CAE in-class test'
}, {
type: 'EXAM',
weight: '60.00',
requirements: 'one 2h exam'
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
