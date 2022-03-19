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
    return {moduleName: 'Big Data',
year: 'Academic Year 2022',
credit: '10.00',
level: '4',
targetStudents: 'Part II and III undergraduate students and MSc students in the School of Computer Science. This module is part of the AI, Modelling and Optimisation theme and the Operating systems and Networks theme in CS. Available to JYA/Erasmus students.',
offeringSchool: 'School of Computer Science',
taughtSemesters: 'Spring China',
requisites: 'N/A',
additionalRequirements: 'N/A',
staffName: 'Dr Saeid Pourroostaei Ardakan',
generalFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
educationAims: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_AIMS$0" style="word-wrap: break-word;"><br></div>',
learningOutcome: '<div class="PSLONGEDITBOX" id="UN_QAA_CRSE_OUT_UN_LEARN_OUTCOME$0" style="word-wrap: break-word;"><br><p style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><b><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Knowledge and Understanding:</span></span></span></b></span></span></span></span></p><ul> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Understand the role and importance of data, information and knowledge.</span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Understand the principles of big data storage, retrieval and processing.</span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Learn to use the key tools and new technologies of big data ecosystem.</span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Learn to define and achieve high quality big data sets.</span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Understand the features of large-scale data computing frameworks. </span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Learn the principals of machine learning algorithms capable of handling big data.</span></span></span></span></span></span></span></li> <li style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Understand cloud computing components to provide big data services.</span></span></span></span></span></span></span></li></ul><p style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><b><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Intellectual Skills:</span></span></span></b></span></span></span></span></p><ul> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Understand complex ideas and relate them to specific problems or questions in the area of big data.</span></span></span></span></span></span></span></li> <li style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Be able to identify</span></span></span> <span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">distributed solutions/approaches to handle big datasets with existing technologies.</span></span></span></span></span></span></span></li></ul><p style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><b><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Professional/Practical Skills:</span></span></span></b></span></span></span></span></p><ul> <li style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Hands-on experience with state-of-the-art technologies to handle big data.</span></span></span></span></span></span></span></li></ul><p style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><b><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Transferable/Key Skills:</span></span></span></b></span></span></span></span></p><ul> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Experience in problem solving.</span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Experience in working in groups.</span></span></span></span></span></span></span></li> <li><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Retrieve information from appropriate sources (e.g. Spark API).</span></span></span></span></span></span></span></li> <li style="margin-bottom:11px"><span style="color:#000000;"><span style="font-size:12px;"><span style="line-height:107%"><span style="font-family:Calibri,sans-serif"><span lang="EN-US"><span style="line-height:107%"><span style="font-family:"Arial",sans-serif">Experience in working with Big Data ecosystems (e.g. Hadoop)</span></span></span></span></span></span></span></li></ul></div>',
summaryOfContent: '<div class="PSLONGEDITBOX" id="UN_PAM_CRSE_DTL_UN_SUMMARY_CONTENT$0" style="word-wrap: break-word;"><br><p><span style="font-size:12px;">Prerequsite: AE3MLE Machine Learning </span></p><p class="western"><span style="color:#000000;"><span style="font-size:12px;"><span style="background:white"><span style="line-height:12.0pt"><span style="font-family:"Times New Roman",serif"><span lang="EN-US" style="font-family:"Arial",sans-serif">“Big Data” involves data whose volume, diversity and complexity requires new technologies, algorithms and analyses to extract valuable knowledge, which go beyond the normal processing capabilities of a single computer. The field of Big Data has many different faces such as databases, security and privacy, visualisation, computational infrastructure or data analytics/mining.</span> <span lang="EN-US" style="font-family:"Arial",sans-serif">This module will provide the following concepts:</span></span></span></span></span></span></p><p class="western"><span style="color:#000000;"><span style="font-size:12px;"><span style="background:white"><span style="line-height:12.0pt"><span style="font-family:"Times New Roman",serif"><span lang="EN-US" style="font-family:"Arial",sans-serif">1. Introduction to Big data: introducing the main principles behind distributed/parallel systems with data intensive applications, identifying key challenges: capture, store, search, analyse and visualise the data.</span></span></span></span></span></span></p><p class="western"><span style="color:#000000;"><span style="font-size:12px;"><span style="background:white"><span style="line-height:12.0pt"><span style="font-family:"Times New Roman",serif"><span lang="EN-US" style="font-family:"Arial",sans-serif">2. SQL Databases vs. NoSQL Databases: understand the growing amounts of data; the relational database management systems (RDBMS); overview of Structured Query Languages (e.g. SQL); introduction to NoSQL databases; understanding the difference between a relational DBMS and a NoSQL database; Identifying the need to employ a NoSQL DB.</span></span></span></span></span></span></p><p class="western"><span style="color:#000000;"><span style="font-size:12px;"><span style="background:white"><span style="line-height:12.0pt"><span style="font-family:"Times New Roman",serif"><span lang="EN-US" style="font-family:"Arial",sans-serif">3. Big Data frameworks and how to deal with big data: this includes the MapReduce programming model, as well as an overview of recent technologies (Hadoop ecosystem, and Apache Spark). Then, you will learn how to interact with the latest APIs of Apache Spark (RDDs, DataFrames and Datasets) to create distributed programs capable of dealing with big datasets (using Python and/or Scala)</span></span></span></span></span></span></p><p class="western"><span style="color:#000000;"><span style="font-size:12px;"><span style="background:white"><span style="line-height:12.0pt"><span style="font-family:"Times New Roman",serif"><span lang="EN-US" style="font-family:"Arial",sans-serif">4. Finally, we will dive into the</span> <span lang="EN-US" style="font-family:"Arial",sans-serif">data mining and machine learning</span> <span lang="EN-US" style="font-family:"Arial",sans-serif">part of the course, including data preprocessing approaches</span> <span lang="EN-US" style="font-family:"Arial",sans-serif">(to obtain quality data), distributed machine learning algorithms and data stream algorithms. To do so, you will use the Machine learning library of Apache Spark (MLlib) to understand how some machine learning algorithms (e.g. Decision Trees, Random Forests, k-means) can be deployed at a scale.</span></span></span></span></span></span></p></div>',
assessmentFurtherActivityDetail: '<br>Activities may take place every teaching week of the Semester or only in specified weeks. It is usually specified above if an activity only takes place in some weeks of a Semester',
methodAndFrequency: [{
activity: 'Computing',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '1 hour'
}, {
activity: 'Lecture',
numberOfWeeks: '12 weeks',
numberOfSessions: '1 week',
duration: '2 hours'
}],
assessmentTable: [{
type: 'Group project',
weight: '50.00',
requirements: 'Programming project in groups'
}, {
type: 'Exam',
weight: '50.00',
requirements: 'Two hours written exam'
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
