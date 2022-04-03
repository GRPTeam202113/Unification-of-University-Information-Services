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
    return {moduleName: 'BEng Group Design Project',
year: 'Academic Year 2022',
credit: '30.00',
level: '3',
targetStudents: 'Part II students in Civil Engineering',
offeringSchool: 'Department of Civil Engineering',
taughtSemesters: 'Spring China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Byung Kang',
generalFurtherActivityDetail: '<br>Design work in Groups outside the above times. The Lecture sessions will support the learning of the principles and the applications of BIM, and the design process for a building structure. The Practical sessions will be in a computer lab to introduce develop the students to the BIM software skills. Workshops are timetabled sessions for the group to develop their design together. Group presentations will be scheduled in the workshop sessions, and other available timetable slots during that week',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>To understand and implement Building Information Modelling when collaboratively planning and designing RC structures.</p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">On successful completion of this module students will be able to: </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">   Understand the scientific principles and the applications of Building Information Modelling, and its historical, current and potential future development.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  List the basic stages of BIM life cycle implementation and develop a BIM Execution Plan (BEP). </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Understand and evaluate a brief from a client and consider the wider engineering context, public perception, and aesthetics. Define the problem, and its constraints, and evaluate RC design solutions at feasibility stage to produce rigorous and creative solutions which meet all aspects of the brief.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;"> Select and use analytical methods and computational modelling techniques to support the design of an RC structure.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Apply BIM based project planning, management, and cost estimation techniques/tools for a building project. Understand risk management techniques.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Communicate a design in an effective manner both to a technical and a non-technical audience. </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Undertake a BIM based RC design including: conceptual design, loading, detailed design and analysis of key RC members; and understand the context in which engineering knowledge can be applied in practice. Understand the appropriate codes and industry standards to use.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Apply skills in problem solving, communication, working with others, and effective use of IT.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">   Work as a member of a design team – taking individual responsibility for certain aspects while still ensuring the group achieve their overall goal. Use BIM protocols to work collaboratively.</span></span></span></p><p style="line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">This will contribute to the following programme learning outcome: (see Programme Specification for details) </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Knowledge and understanding of : SM1 </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Intellectual skills to: EA2, EA3, DD1, DD2, DD4, DD5, DD6  </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Professional/Practical skills to : EE3, EE4, EE6, EP1, EP4, EP6, EP8 </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">  Transferable/Key Skills to : GS1, GS2, GS3, GS4</span></span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p style="line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">This module provides students with an opportunity to use digital design, planning, analysis and presentation tools to support the collaborative design and planning of a reinforced concrete building.</span></span></span></p><p style="line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">Students get introduced to fundamental concepts and applications of Building Information Modelling (BIM). By example, they get to learn specific BIM software. Following this, they work in groups on their design project that covers the following subject areas: </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">Feasibility studies and conceptual design </span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">• The benefits of using BIM on construction project</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">• Preparing a BIM Execution Plan (BEP)</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">• Detailed structural design and documentation.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">• Health and Safety residual risks.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;"> Project planning, risk management, and cost estimation.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"><span style="color:#003965;"><span style="font-family:symbol;"><span style="font-size:12.0pt;">·</span></span></span><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;"> Sustainability and Life Cycle Management.</span></span></span></p><p style="margin-bottom:0in;margin-bottom:.0001pt;line-height:normal;"> </p><p><span style="color:#003965;"><span style="font-family:arial,sans-serif;"><span style="font-size:12.0pt;">Under the umbrella of BIM this module brings together Construction Management and Structural Design and makes students aware of the potential of emerging digital design technologies</span></span></span></p></div>',
assessmentFurtherActivityDetail: '<br>Design work in Groups outside the above times. The Lecture sessions will support the learning of the principles and the applications of BIM, and the design process for a building structure. The Practical sessions will be in a computer lab to introduce develop the students to the BIM software skills. Workshops are timetabled sessions for the group to develop their design together. Group presentations will be scheduled in the workshop sessions, and other available timetable slots during that week',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Practicum',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}, {
activity: 'Workshop',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}],
assessmentTable: [{
type: 'Presentation 1',
weight: '15.00',
requirements: 'Group presentation of initial concept designs (assessment of presentation skills and technical content)'
}, {
type: 'Written Exam',
weight: '25.00',
requirements: '90 minutes written assessment on the fundamentals of BIM&nbsp;'
}, {
type: 'Coursework',
weight: '50.00',
requirements: 'Final group BIM, detailed design and construction management report'
}, {
type: 'Presentation 2',
weight: '10.00',
requirements: 'Final group presentation (assessment of presentation skills and technical content)&nbsp;'
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
