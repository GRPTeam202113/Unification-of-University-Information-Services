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
    return {moduleName: 'Marketing Strategy',
year: 'Academic Year 2022',
credit: '20.00',
level: '4',
targetStudents: 'Business School MSc students subject to compliance with module choice requirements, as listed in the degree programme specification. In addition, other MA/MSc students subject to the discretion of the Director of MSc Programmes&rsquo;',
offeringSchool: 'Nottingham University Business School China',
taughtSemesters: 'Autumn China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Miss Maria Luo',
generalFurtherActivityDetail: '<br>44 hours of lectures; 20 hours of simulation preparation and playing; 50 hours of support reading and lecture / small group work preparation; 50 hours of coursework preparation; 36 hours of examination revision',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br><p>On completion of this module students will be able to: To evaluate the importance and application of strategic marketing tools and techniques. To examine the relative merits of marketing strategies in different marketing environments. To examine the importance of Marketing Analytics and understand the different notions related to marketing analytics.  To successfully participate in a Marketing Simulation Game where knowledge will be tested in practice. </p></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin: 9pt 0in 0pt;"><strong><span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Knowledge and understanding</span></span></span></span></strong>: <span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">This module develops a knowledge and understanding of:</span></span></span></span></p><p style="margin: 9pt 0in 0pt;">•<span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">The dynamics of the global economy and international business &amp;/or an awareness <span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">of cultural, legal/regulatory, political, and economic differences across countries &amp;/or </span></span></span><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">an appreciation of management issues from a global perspective.</span></span></span></span></span></span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Markets - the development and operation of markets for resources, goods and services </span></p><p>•<span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Marketing and sales – different approaches for segmentation, targeting, positioning, generating sales, and the need for innovation in product and service design</span></span></span></span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Customers and stakeholders - customer expectations, service and orientation</span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Tools and techniques for transforming (big) data into useful information for business analysis and decision support</span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Communications – the comprehension and use of relevant communications for application in business and management, including the use of digital tools</span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Digital business – the development of strategic priorities to deliver business at speed in an environment where digital technology is reshaping traditional revenue and business models, associated risk management</span></p><p>•<span lang="EN-GB" style="font-family: "Verdana",sans-serif; font-size: 8pt; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-GB; mso-bidi-language: AR-SA;"><font color="#000000">Strategic management - the development and implementation of appropriate strategies within a changing environment</font></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Intellectual Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Being able to think critically and be creative: manage the creative processes in self and others; organise thoughts, analyse, synthesise and critically appraise. This includes the capability to identify assumptions, evaluate statements in terms of evidence, detect false logic or reasoning, identify implicit values, define terms adequately and generalise appropriately</span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Being able to solve complex problems and make decisions: establish criteria, using appropriate decision-making techniques including identifying, formulating and solving business problems; and the ability to create, identify and evaluate options; the ability to implement and review decisions</span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Using information and knowledge effectively in order to abstract meaning from information and to share knowledge, including the use of quantitative skills</span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Professional Practical Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of qualitative data, synthesis and reporting</span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">The ability to conduct research and enquiry into business and management issues either individually or as part of a team through research design, the collection and analysis of quantitative data, synthesis and reporting</span></p><p>•<span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">Effective performance within team environments and the ability to recognise and utilise individuals" contributions in group processes and to negotiate and persuade or influence others; team selection, delegation, development and management.  </span></span></span></span></p><p><strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">Transferable (key) Skills: </span></span></strong><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;">This module develops:</span></span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Effective communication: networking, listening, oral and written communication of complex ideas and arguments, using a range of media, including the preparation of business reports</span></p><p>•<span style="-ms-layout-grid-mode: line;"><span style="font-size: 8pt;"><span style="font-family: verdana,sans-serif;"><span style="color: black;">High personal effectiveness: critical self-awareness, self-reflection and self-management; time management; conflict  resolution, displaying commercial acumen, the ability to continue to learn through reflection on practice and experience</span></span></span></span></p><p>•<span lang="EN-GB" style="color: black; font-family: "Verdana",sans-serif; font-size: 8pt; -ms-layout-grid-mode: line; mso-fareast-font-family: SimSun; mso-bidi-font-family: "Times New Roman"; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA; mso-bidi-font-size: 10.0pt;">Soft skills: understanding the needs of others and empathy towards them; sensitivity to diversity in people and in different situations</span></p><p> </p></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p>Lecture topics to include: Marketing strategy and business performance, strategic marketing planning, understanding the market environment, market segmentation, targeting and positioning, strategic choices, developing and analysing strategic options, implementing marketing strategies, strategic marketing thinking, Marketing Analytics, Big Data, Behavioural Data, Marketing Simulation Game.</p></div>',
assessmentFurtherActivityDetail: '<br>44 hours of lectures; 20 hours of simulation preparation and playing; 50 hours of support reading and lecture / small group work preparation; 50 hours of coursework preparation; 36 hours of examination revision',
methodAndFrequency: [{
activity: 'Lecture',
numberOfWeeks: '11 weeks',
numberOfSessions: '2 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Coursework 1',
weight: '50.00',
requirements: 'Group Project Written Report (3,000 words)'
}, {
type: 'Presentation 1',
weight: '10.00',
requirements: 'Group Project Presentation (10 mins plus 10 mins Q&amp;A)'
}, {
type: 'Exam 1',
weight: '40.00',
requirements: '1.5 Hour Exam'
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
