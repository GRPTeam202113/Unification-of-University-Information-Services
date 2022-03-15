<!--
 * @Descripttion: The page for faculty FHSS, mainly demonstrate the
 * courses(with linking to corresponding course page) under FHSS faculty
 * @Author: Yongjing Qi
 * @Date: 2022-03-01 23:36:00
 * @LastEditTime: 2022-03-15 10:49:50
-->
<template>
    <div class ="fhss">
        <h1 class="title">Faculty of Humanities and Social Sciences</h1>
         <el-divider></el-divider>
         <span class="introduction">{{Intro}}</span>
        <br><br><br><br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">{{Title}}</div>
                </span>
            </div>
        </div>
        <br><br><br>
        <div class = "courses">
                <el-table
                    :show-header="false"
                    :data="courses"
                    margin="10%"
                    height="500"
                    border
                    style="width: 100%"
                    width="400">
                    <el-table-column
                    prop="moduleName">
                    <template slot-scope="scope">
                        <!-- <a :href="'http:'+'//www.baidu.com'" target="_blank" class="buttonText">{{scope.row.module}}</a> -->
                        <!-- <router-link v-bind:to="'/abc/' + scope.row.code">{{scope.row.module}}</router-link> -->
                        <el-card class="box-card" shadow="hover">
                            <div class="subTitle"><span><router-link :to="{name:'course', params:{Faculty:'FHSS', CourseName: scope.row.label}}">{{scope.row.label}}</router-link></span></div><br>
                            <br><br>
                        </el-card>
                        <!-- <span @click="toModulePage(scope.row.code)" >{{scope.row.module}}</span> -->
                    </template>
                    </el-table-column>
                </el-table>
        </div>
    </div>
</template>
<script>
    import { FHSS } from './threeFacultydb/3Facultydb'
    export default {
        name: 'fose',
        data () {
            return {
                Msg: 'Welcome to FoSE !',
                userList: [],
                currentPage: 1,
                pageSize: 5,
                Title: 'Course',
                Intro: 'We have four schools, including the School of Economics, School of Education and English, School of International Communications and the School of International Studies, and a Language Centre.',
                courses: FHSS
            }
        },
        mounted() {
            console.log(this.courses)
        // this.handleUserList()
    },
    methods: {
        // initialize currentPage,pagesize and data
        handleSizeChange: function (size) {
                this.pagesize = size
                console.log(this.pagesize)
        },
        handleCurrentChange: function(currentPage) {
                this.currentPage = currentPage
                console.log(this.currentPage)
        }
    }
}
</script>

<style rel="stylesheet/scss" lang="css" scoped>
    .courses-list{
        font-size: 200px;
    }
    .title{
        margin-left: 30px;
        font-size:50px;
        font-weight:bolder;
        color: black;
    }
    .subTitle{
        font-size:20px;
        font-weight: bold;
        margin-left: 30px;
    }
    .box-card{
        height: 70px;
    }
    .square{
        margin-left: 20px;
        width: 90px;
        height: 90px;
    }
    .squareTitle{
        position: absolute;
        color:rgb(0, 0, 0);
        background-color: #F7F7F8;
        width:90%;
        padding-left:5px;
        padding-top:6px;
        padding-bottom: 6px;
        font-size:25px;
        font-weight: bolder;
    }
    .normalTitle{
        color:rgb(0, 0, 0);
        font-size:25px;
        font-weight: bolder;
    }
    .introduction {
        margin-left: 40%;
        margin-right: 10%;
        float: right;
    }
</style>
