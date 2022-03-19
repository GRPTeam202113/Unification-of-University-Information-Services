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
    return {moduleName: 'Air Pollution',
year: 'Academic Year 2022',
credit: '10.00',
level: '3',
targetStudents: 'Students registered in the Department of Chemical and Environmental Engineering only. Available to JYA/Erasmus students',
offeringSchool: 'Department of Chemical and Environmental Engineeri',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: '',
generalFurtherActivityDetail: '<br>This module to run concurrent with J1CAPC Air Pollution Control Technology',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>To provide students with knowledge of the range of air pollution problems in modern society and to the design models that may be used to estimate the dispersion and deposition of pollutants within the atmosphere. To introduce students to the the various end of pipe control techniques that are available to mitigate controlled pollutant emissions from industrial processes.</p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">To provide students with knowledge of the range of air pollution problems in modern society and to the design models that may be used to estimate the dispersion and deposition of pollutants within the atmosphere.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">To introduce students to the various end of pipe control techniques that are available to mitigate controlled pollutant emissions from industrial processes.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">Learning Outcomes:  </span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">A2.4.1 Understand and be able to apply methods to analyze the characteristics and performance of a range of typical mixing, separation, and similar processing steps for fluids, particles and mult-phases to assist in the mitigation or capture of gaseous and particulate emissions from a given process to atmosphere.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the ability to select the appropriate type, and determine the size and performance of an integrated application of individual unit operations to either modify and/or mitigate gaseous or particulate process emissions to atmosphere.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">A2.4.2 Understand the principles on which processing equipment operates, and be able to apply methods to determine equipment size and performance of common items that both mitigate the production of and capture the gaseous and particulate emissions of processes to atmosphere.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the ability to select the appropriate type , and determine the size and performance of an integrated application of individual unit operations to either modify and/or mitigate gaseous or particulate process emissions to atmosphere.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">A2.6.0.1 Understand the inherent nature of safety and loss prevention, and the principal hazards sources in chemical and related processes – including flammability, explosively, toxicity and biological hazards.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the ability to identify and rank the potential gaseous and particulate (multi-phase) hazards that may be emitted from the analysis of a given process using a standard hazard identification (HAZID, MSDS) tools.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrate the ability to select the appropriate measurement instrumentation to detect and inform the presence and level of the gaseous and particulate hazards present within the process.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">A2.6.0.2 Understand the principles or risk assessment and of safety management, and be able to apply techniques for the assessment and abatement of process and product hazards.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the ability to identify and rank the potential gaseous and particulate (multi-phase) hazards that may be emitted from the analysis of a given process using a standard hazard identification (HAZID, MSDS) tools.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the ability to select unit modifications to the initial process to minimize the identified principal hazards, or to include appropriate mitigation unit operations to minimize such hazardous emissions to atmosphere.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">A2.7.0.1 Understand the principles of sustainability (environmental, social and economic) and be able to apply techniques to analyze, throughout the life cycle, the interaction of process, product and plant with the environment.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the ability to identify sensitive receptor populations from an analysis of the local meteorological and topographical record, and the ability to rank gaseous and particulate emission species according to their potential harm, identified by a preliminary hazard identification, subsequently supported by a detailed identification of the permitted maximum emission flow rates and receptor threshold exposure limits of these principal hazard species.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">A2.7.0.2 Understand and be able to apply the main methods of minimizing the environmental impact on air, water, land and integrated eco-systems, including waste minimization at source and ‘end-0f-pipe’ methods.</span></span></span></p><p style="margin: 0in 0in 8pt;"> </p><p style="margin: 0in 0in 8pt;"><span style="background: yellow;"><span style="font-size: medium;"><span style="font-family: calibri;">  Demonstrated by the application of Gaussian plume dispersion modelling to the environmental impact assessment (EIA) of process emissions to atmosphere. Computational environmental risk assessment method used to determine the height and location of process stacks to minimize the impact of emissions to sensitive receptors located in the vicinity of a planned or existing plant operation.</span></span></span></p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p>The module delivers an overview of air pollution problems and range of techniques which are available for its control; sources and effects of air pollutants of major concern; and the development of air quality criteria. The behaviour of the atmosphere and the dispersion of air pollutants are studied. Students are introduced to techniques of air pollution measurement and their use in the assessment of the effects that industrial activity may have. An overview of current EU and UK environmental legislation is provided, and the role of the assessment and control of air pollution in the planning application of existing and new industrial process is discussed. The duties of process managers, local authorities and the Environment Agency are discussed in light of the current and proposed legislation. This module gives knowledge and understanding of air pollution problems, including a categorization of the types of natural and anthropogenic air pollution sources, sinks, and the effects that air pollutants may produce within the natural and manmade environments. The physiological effects and HSE aspects of air pollution are discussed. A review of national and international standards of permitted emission release and exposure levels of pollution is presented. The student is introduced to the processes of selection and design of pollutant monitoring and control technologies that may be applied to control atmospheric emissions from industrial processes.</p></div>',
assessmentFurtherActivityDetail: '<br>This module to run concurrent with J1CAPC Air Pollution Control Technology',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}, {
activity: 'Seminar',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '30.00',
requirements: 'Design Exercise Sheet'
}, {
type: 'Exam 1',
weight: '70.00',
requirements: '2 Hours Exam'
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
