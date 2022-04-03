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
    return {moduleName: 'Corpus Linguistics (BA)',
year: 'Academic Year 2022',
credit: '20.00',
level: '3',
targetStudents: 'Strongly recommended for BA English Language and Applied Linguistics students.Optional for BA English and International Business.Other students by agreement with the convenor.',
offeringSchool: 'School of Education and English',
taughtSemesters: 'Spring China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: '',
generalFurtherActivityDetail: '<br>',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>After completing this module, students will -<br>•    develop a solid understanding of the concerns and methods of corpus linguistics with a focus on the application of corpus analytic methods in linguistic studies, literary analysis, English language teaching, and research on professional communication<br>•    develop the ability to apply corpus analytic methods in literary criticism, linguistic inquiry, and business communication studies<br>•    become familiar with quantitative analysis of corpus</p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p>Knowledge and understanding of<br>•    Key concepts, terms and concerns of corpus linguistics;<br>•    Theories underlying corpus linguistics;<br>•    Distinctions between corpus linguistics and cognitive linguistics;<br>•    Types of corpora and their applications in language-based studies;<br>•    Methods of building corpora and ways of conducting corpus-based research.<br>Intellectual skills:<br>•    The ability to view a given discipline in perspective;<br>•    The competence in examining stretches of discourse in different genres through computer-aided and data-based analysis;<br>•    The ability to interpret research findings and their implications in a broad context;<br>•    The capability to theorize the distinctions between different approaches to linguistic studies;<br>•    The ability to understand relevant published research, locate the strengths as well as drawbacks of students" own work and make plans for improvement.<br>Professional skills:<br>•    The ability to analyse and interpret corpus-based work in the domains of linguistic enquiry, literary analysis, English education, and business communication studies;<br>•    The capability to design, construct and use corpora for data-based or quantitatively oriented research;<br>•    The competence in evaluating corpus-based studies within a terminological framework of corpus linguistics in a professional setting;<br>•    The ability to disseminate findings of corpus research via clear and effective presentation.<br>Transferable skills:<br>•    The ability to perform date-based linguistic analysis of various texts;<br>•    The competence in gathering, sorting out and processing data by means of information technology for empirical research;<br>•    The capability to present findings of computer-aided investigation and engage in discussion of them from two or more perspectives.</p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p>The module looks at the use of corpus methodology to study a wide range of areas and issues in applied linguistics. These will include, amongst others, the analysis of everyday discourse and of institutional discourse, the analysis of language and register/genre, English Language Teaching, creativity in language use, the study of vocabulary and lexico-grammar. The aim of the module is to provide students with an introduction to some of the tools and resources used for corpus analysis, and to help them develop a range of skills needed to analyse computerised samples of natural language. The emphasis of the module is on the application of corpus analysis to specific research questions, and students will have the opportunity to explore the use of corpus methodologies in relation to their own research interests and to formulate new lines of inquiry that they will investigate with a corpus approach.<br>Please note: This module is assessed at the end of Spring semester. First sit/ Re-sit exams are scheduled normally in the summer and can take the same form as the missing/ failed component of the assessment (e.g. essay) or other form, as decided by the School.</p></div>',
assessmentFurtherActivityDetail: '<br>',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '10 weeks',
numberOfSessions: '1 week',
duration: '1 hour and 30 minutes'
}, {
activity: 'Seminar',
numberOfWeeks: '10 weeks',
numberOfSessions: '1 week',
duration: '1 hour and 30 minutes'
}],
assessmentTable: [{
type: 'Coursework',
weight: '100.00',
requirements: 'One 3,500-word project/essay'
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
