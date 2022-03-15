<!--
 * @Descripttion: This is the search function for any details of the web system,
 * this search filter is capable for searching for faculty page, course page, modules page
 * of UNNC undergraduate school
 * @Author: Yongjing Qi
 * @Date: 2022-03-08 09:04:40
 * @LastEditTime: 2022-03-15 10:47:24
-->

<template>
    <div>
        <h1 class="Title">Search Functions</h1>
        <el-divider></el-divider>
        <br>
        <div class="introduction">{{ generalIntroForSearchFunction }} <span><router-link to="/cele">CELE</router-link></span></div>
        <br><br><br><br>
        <div>
            <el-card :body-style="{ padding: '20px'}" el-card shadow="always">
            <el-row>
                <el-col :span="6">
                <div class="title">Faculty</div>
                <br>
                <el-select style="width: 90%" @change="selectedFaculty" @clear="clearFaculty" clearable v-model="faculty" placeholder="Faculty">
                    <el-option
                    v-for="item in Faculty"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="6">
                <div class="title">Course</div>
                <br>
                <el-select style="width: 90%" @change="selectedCourse" @clear="clearCourse" clearable v-model="course" :disabled = "isDisableCourse" placeholder="Course">
                    <el-option
                    v-for="item in Course"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="6">
                <div class="title">Year</div>
                <br>
                <el-select style="width: 90%" @change="selectedYear" @clear="clearYear" :disabled = "isDisableYear" clearable v-model="year" placeholder="Year">
                    <el-option
                    v-for="item in Year"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="6">
                <div class="title">Module</div>
                <br>
                <el-select style="width: 90%" @change="selectedModule" @clear="clearModule" :disabled = "isDisableModule" clearable v-model="module" placeholder="Module">
                    <el-option
                    v-for="item in Module"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                    </el-option>
                </el-select>
                </el-col>
            </el-row>
            <br><br><br>
            <div class="searchButton" align = "center">
                    <span><el-button type="primary" plain style="width: 30%" icon="el-icon-search" @click="clickSearch"><span class="search">Click To Search</span></el-button></span>
                </div>
            </el-card>
            <br><br><br><br><br><br><br><br>
        </div>
    </div>
</template>

<script>
import {FOSE, FOB, FHSS} from './Faculty/threeFacultydb/3Facultydb'
import {request} from '../router/request'
  export default {
    data() {
      return {
        generalIntroForSearchFunction: 'Using the filter below you can corresponding detail pages, For Year 1 modules, please go to to ',
        Faculty: [
            {
                value: 'FOSE',
                label: 'Faculty of Science and Engineering'
            }, {
                value: 'FHSS',
                label: 'Faculty of Humanities and Social Sciences'
            }, {
                value: 'FOB',
                label: 'Faculty of Business'
            }],
        Course: null,
        Year: [
            {
                value: 'Level 1',
                label: 'Year 2'
            }, {
                value: 'Level 2',
                label: 'Year 3'
            }, {
                value: 'Level 3',
                label: 'Year 4'
            }],
        Module: [],
        faculty: null,
        course: null,
        year: null,
        module: null,
        isDisableCourse: true,
        isDisableYear: true,
        isDisableModule: true,
        options: [],
        value1: [],
        value2: []
      }
    },
    methods: {
        clickSearch() {
            if (this.faculty != null && this.course == null && this.year == null && this.module == null) {
                this.goToFacultyPage()
            }
            if (this.faculty != null && this.course != null && this.year == null && this.module == null) {
                this.goToCoursePage()
            }
            if (this.faculty != null && this.course != null && this.year != null && this.module == null) {
                this.goToCoursePage()
            }
            if (this.faculty != null && this.course != null && this.year != null && this.module != null) {
            this.$router.push({ name: 'module', params: {ModuleCode: this.module} })
            }
        },
        goToFacultyPage() {
            if (this.faculty === 'FOSE') {
                this.$router.push({ name: 'fose' })
            } else if (this.faculty === 'FHSS') {
                this.$router.push({ name: 'fhss' })
            } else if (this.faculty === 'FOB') {
                this.$router.push({ name: 'fob' })
            }
        },
        goToCoursePage() {
            this.$router.push({ name: 'course', params: {Faculty: this.faculty, CourseName: this.course} })
        },
        selectedFaculty(value) {
            this.$forceUpdate()
            this.faculty = value
            this.isDisableCourse = false
            this.isDisableModule = true
            this.isDisableYear = true
            this.course = null
            this.year = null
            this.module = null
            if (value === 'FOSE') {
                this.Course = FOSE
                console.log(value)
            } else if (value === 'FHSS') {
                this.Course = FHSS
            } else if (value === 'FOB') {
                this.Course = FOB
            }
            // array clear
            this.Module = []

            // console.log(value)
        },
        clearFaculty() {
            this.$forceUpdate()
            this.faculty = null
            this.course = null
            this.year = null
            this.module = null

            this.Course = null
            this.Module = []

            this.isDisableCourse = true
            this.isDisableYear = true
            this.isDisableModule = true
        },
        selectedCourse(value) {
            this.$forceUpdate()
            this.course = this.Course.find(function(item) {
                return item.value === value
            }).label
            this.isDisableYear = false
            this.isDisableModule = true

            this.Module = []
            this.year = null
            this.module = null
        },
        clearCourse() {
            this.course = null
            this.year = null
            this.module = null

            // this.Course = null
            this.Module = []

            this.isDisableYear = true
            this.isDisableModule = true
        },
        selectedYear(value) {
            this.$forceUpdate()
            this.year = value
            this.module = null
            this.isDisableModule = false
            this.Module = []
            var para = {facultyname: this.faculty, coursename: this.course}
            var returnVal = request.post(para)
            var returnValue = null
            returnVal.then((result) => {
                returnValue = result.data
                console.log(returnValue.modulecodes[0])
                this.processReturnValue(returnValue)
            })
        },
        clearYear() {
            this.year = null
            this.module = null

            this.Module = []
            this.isDisableModule = true
        },
        selectedModule(value) {
            this.$forceUpdate()
            this.module = value
        },
        clearModule() {
            this.module = null
            // this.Module = []
        },
        processReturnValue(returnValue) {
            var allModules = returnValue
            // this.Module = []
            for (let i = 0; i < allModules.modulecodes.length; i++) {
                if (allModules.modulelevels[i] === this.year) {
                    var element = {'value': allModules.modulecodes[i], 'label': allModules.modulenames[i]}
                    this.Module.push(element)
                }
            }
        }
    }
  }
</script>
<style scoped>
.Title {
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
.searchTitle {
    font-weight: bolder;
    font-size: 20px;
}
.searchButton {
    margin-top: 20%;
    margin-top: 0%;
    width:100%;
}
.title {
    font-weight: bolder;
    font-size: 20px;
    color:#116996
}
.search {
    font-weight: normal;
    font-size: 20px;
}
.introduction {
        margin-left: 60%;
        margin-right: 10%;
        float: right;
}
</style>
