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
    return {moduleName: 'Hydraulics 2',
year: 'Academic Year 2022',
credit: '10.00',
level: '2',
targetStudents: 'BEng Part I Civil Engineering students',
offeringSchool: 'Department of Civil Engineering',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Fangfang Zhu',
generalFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><div><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:2.0pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o extend and build on fundamental concepts and principles introduced in Hydraulics 1</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:6.0pt;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:190.55pt;margin-bottom:0in;margin-left:2.0pt;margin-bottom:.0001pt;line-height:101%;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o familiarize students with the fundamental concepts and principles of fluid dynamics and the basic concepts of a moving fluid i.e. real/ideal flow</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:6.0pt;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:2.0pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o enable students to apply these concepts to problems of relevance to engineering, in particular pipe flow</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:6.0pt;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:2.0pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o introduce the concepts of open channel flow</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:6.0pt;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:2.0pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o introduce the concepts of boundary layers and flows with vorticity</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:6.0pt;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:179.55pt;margin-bottom:0in;margin-left:2.0pt;margin-bottom:.0001pt;line-height:101%;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o provide an active learning environment where students will be able to take responsibility for their own development skills, thereby enhancing their attractiveness to prospective employers</span></span></span></p></div><p> </p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:6.0pt;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:95.6pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•<span style="letter-spacing:-.65pt;">T</span>o acquaint students with the sources of literature available in the area of hydraulic engineering</span></span></span></p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:95.6pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"> </p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:95.6pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•To introduce students to the principles of fluid flow and the simplified physical models used to describe flow in pipes and open channels.</span></span></span></p><p style="margin-top:0in;margin-right:0in;margin-bottom:0in;margin-left:95.6pt;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"> </p><p><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">•</span></span></span> <span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">To enable students to apply these physical models to analyse problems of relevance in civil engineering</span></span></span></p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p>On successfully completing the module, students will be able to: </p><p>1) Apply physical principles and mathematical methods to solve civil-engineering themed problems involving fluid flows in pipes and open channels. <br>2) Apply module content within a wider civil engineering context. <br>This will contribute to the following programme learning outcomes (see Programme Specification for details):<br> Knowledge and understanding of: A1, A2, A4 <br> Intellectual skills to: B1, B2, B4 <br> Transferable/Key Skills to: D1, D4</p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><div><p style="margin-top:2.2pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">The module extends the relationships established in H21H<span style="letter-spacing:-.45pt;">1</span>1 to consider broader principles:</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:7.0pt;text-autospace:none;"> </p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">1) Conservation of mass (continuity), momentum and energy</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:7.0pt;text-autospace:none;"> </p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">2) Steady flow in pipes and pipe systems</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:7.0pt;text-autospace:none;"> </p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">3) Quasi-steady pipe flow (in the context of reservoir discharge/transfer)</span></span></span></p><p style="margin-top:.1pt;margin-right:0in;margin-bottom:0in;margin-left:0in;margin-bottom:.0001pt;line-height:7.0pt;text-autospace:none;"> </p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:6.75pt;text-autospace:none;"><span style="color:#515151;"><span style="font-family:arial,sans-serif;"><span style="font-size:6.0pt;">4) Open channel flow</span></span></span></p></div><p> </p></div>',
assessmentFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '11 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Exam 1',
weight: '100.00',
requirements: '<span style="color: rgb(81, 81, 81);"><span style="font-family: arial,sans-serif;"><span style="font-size: 6pt;">General exam &ndash; standard: 2 papers of 3 hours assessing CIVE2025, CIVE2051, CIVE2029 &amp; CIVE2054 . Particular questions will test module specific knowledge to 2:1/2:2 borderline level. The module specific marks returned will form 70% of each overall module mark.</span></span></span>'
}],
staffOffice: 'Room 313, Sir Peter Mansfield Building',
staffAddress: '199 Taikang East Road, Ningbo, 315100, China',
staffCampus: 'University of Nottingham Ningbo China',
staffTelephone: '+86 (0) 574 8818 0000-9059',
staffDepartment: 'Faculty of Science and Engineering',
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
