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
    return {moduleName: 'Advanced Techniques for Supply Chain Management',
year: 'Academic Year 2022',
credit: '20.00',
level: '4',
targetStudents: 'Business School MSc students subject to compliance with module choice requirements, as listed in the degree programme specification. In addition, other MA/MSc students subject to the discretion of the Director of MSc Programmes',
offeringSchool: 'Nottingham University Business School China',
taughtSemesters: 'Spring China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: '',
generalFurtherActivityDetail: '<br>Total Contact Hours = 44 hours (33 hours of lectures = 3-hour lecture x 11 weeks) + 11 hours computer lab sessions (5x1 hour + 3x2 hours)',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>The module aims to provide an understanding of the methods and techniques of statistics, machine learning, information systems, and system dynamics with applications in business and industry, including Supply Chain Management and related areas.  Students will learn how to apply the advanced quantitative techniques for a range of problems and appreciate the importance of data-driven decision making.</p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p>Knowledge and understanding: This module develops a knowledge and understanding of:</p><p>The management of the supply chain</p><p>The dynamics of the global economy and international business &amp;/or an awareness <br>of cultural, legal/regulatory, political, and economic differences across countries &amp;/or <br>an appreciation of management issues from a global perspective.</p><p>Customers and stakeholders - customer expectations, service and orientation</p><p>The management of logistics</p><p>The management of projects</p><p>Information systems and business intelligence - the development, management, application and implementation of information systems and their impact upon organisations<br>  <br>Tools and techniques for transforming (big) data into useful information for business analysis and decision support</p><p>Communications – the comprehension and use of relevant communications for application in business and management, including the use of digital tools</p><p>The importance of sustainability issues, including an understanding of the challenges <br>and opportunities arising from the activities of people and organisations on the economic, social and environmental conditions of the future.</p><p>Intellectual Skills: This module develops:</p><p>Being able to think critically and be creative: manage the creative processes in self and others; organise thoughts, analyse, synthesise and critically appraise. This includes the capability to identify assumptions, evaluate statements in terms of evidence, detect false logic or reasoning, identify implicit values, define terms adequately and generalise appropriately</p><p>Being able to solve complex problems and make decisions: establish criteria, using appropriate decision-making techniques including identifying, formulating and solving business problems; and the ability to create, identify and evaluate options; the ability to implement and review decisions</p><p>Using information and knowledge effectively in order to abstract meaning from information and to share knowledge, including the use of quantitative skills</p><p>Professional Practical Skills: This module develops:<br>research design, the collection and analysis of qualitative data, synthesis and reporting</p><p>The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of quantitative data, synthesis and reporting</p><p>Effective performance within team environments and the ability to recognise and utilise individuals" contributions in group processes and to negotiate and persuade or influence others; team selection, delegation, development and management.  Leadership and performance management: selecting appropriate leadership style for different situations; setting objectives, motivating, monitoring performance, coaching and mentoring</p><p>The ability to recognise the need for and initiate change and to be able to manage change</p><p>The ability to recognise and address ethical dilemmas, corporate social responsibility and sustainability issues, applying ethical and organisational values to situations and choices</p><p><br>Transferable (key) Skills: This module develops:</p><p>Effective communication: networking, listening, oral and written communication of complex ideas and arguments, using a range of media, including the preparation of business reports</p><p>High personal effectiveness: critical self-awareness, self-reflection and self-management; time management; conflict resolution, displaying commercial acumen, the ability to continue to learn through reflection on practice and experience</p><p>Soft skills: understanding the needs of others and empathy towards them; sensitivity to diversity in people and in different situations<br>Other: The ability to apply management science techniques</p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p>The emphasis in this module is on formulating and solving models with statistical, machine learning, information systems, and system dynamics tools. The topics covered include: introduction to supervised and unsupervised machine learning, model quality dimensionality, principal component analysis, clustering, and classifications, comparing predictor accuracy, sensitivity and specificity, supply chain IT systems including manufacturing execution systems (MES), warehouse management systems (WMS), and transportation management systems (TMS), supply chain network design, causal loop diagrams, stock and flow charts, common structures and behaviour in system dynamics, the bullwhip effect and supply chain dynamics </p></div>',
assessmentFurtherActivityDetail: '<br>Total Contact Hours = 44 hours (33 hours of lectures = 3-hour lecture x 11 weeks) + 11 hours computer lab sessions (5x1 hour + 3x2 hours)',
methodAndFrequency: [{
activity: 'Computing',
numberOfWeeks: '5 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}, {
activity: 'Computing',
numberOfWeeks: '3 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Lecture',
numberOfWeeks: '11 weeks',
numberOfSessions: '1 week',
duration: '3 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '30.00',
requirements: 'Group Coursework (3,000 words) &nbsp;'
}, {
type: 'Exam 1',
weight: '70.00',
requirements: '2 Hour Examination'
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
