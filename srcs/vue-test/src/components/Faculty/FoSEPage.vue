<template>
    <div class ="fose">
        <h1 class="title">Faculty of Science and Engineering</h1>
        <div class = "courses">
        <el-row>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
            <!-- <el-col :span="9">
                <el-table
                :row-style="{height:'80px'}"
                :data="courses.slice((currentPage-1)*pageSize,currentPage*pageSize)"
                style="width: 100%; font-size: 18px; font-weight:bolder">
                <el-table-column
                    align="center">
                    <template slot-scope="scope">
                    <img :src="scope.row.img" alt="" width="300" height="300">
                    </template>
                </el-table-column>
                </el-table>
            </el-col>
            <el-col :span="13">
                <el-table
                :data="courses.slice((currentPage-1)*pageSize,currentPage*pageSize)"
                style="width: 100%; font-size: 18px; font-weight:bolder">
                <el-table-column
                align="center">
                <template slot-scope="scope">
                <a :href="scope.row.url" target="_blank" class="buttonText">{{scope.row.label}}</a>
                </template>
                </el-table-column>
                </el-table>
            </el-col> -->
            <el-table
                :row-style="{height:'80px'}"
                :data="courses.slice((currentPage-1)*pageSize,currentPage*pageSize)"
                style="width: 100%; font-size: 18px; font-weight:bolder">
            <el-col :span="9"></el-col>
                <el-table-column
                    align="center">
                    <template slot-scope="scope">
                    <img :src="scope.row.img" alt="" width="300" height="300">
                    </template>
                </el-table-column>
            <el-col :span="13">
                <el-table-column
                align="center">
                <template slot-scope="scope">
                <a :href="scope.row.url" target="_blank" class="buttonText">{{scope.row.label}}</a>
                </template>
                </el-table-column>
            </el-col>
            </el-table>
            <el-col :span="1"><div class="grid-content bg-purple-white"></div></el-col>
        </el-row>
        <nav style="text-align: center">
        <el-pagination
            @size-change = "handleSizeChange"
            @current-change = "handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="5"
            :page-size="pageSize"
            small
            layout="prev, pager, next"
            :total="courses.length">
        </el-pagination></nav>
        <!-- <el-row><el-table
            :row-style="{height:'80px'}"
            :data="courses.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%; font-size: 18px; font-weight:bolder">
            <el-col :span="10">
            <el-table-column
                align="center">
                <template slot-scope="scope">
                <img :src="scope.row.img" alt="" width="300" height="300">
                </template>
            </el-table-column>
            </el-col>
            <el-col :span="14">
            <el-table-column
                align="center">
                <template slot-scope="scope">
                <a :href="scope.row.url" target="_blank" class="buttonText">{{scope.row.label}}</a>
                </template>
            </el-table-column>
            </el-col>
        </el-table>

        <nav style="text-align: center">
        <el-pagination
            @size-change = "handleSizeChange"
            @current-change = "handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="5"
            :page-size="pageSize"
            small
            layout="prev, pager, next"
            :total="courses.length">
        </el-pagination></nav>
        </el-row> -->
        </div>
        <router-link to="/">Back to Main</router-link>
    </div>
</template>
<script>
    export default {
        name: 'fose',
        data () {
            return {
                Msg: 'Welcome to FoSE !',
                userList: [],
                currentPage: 1,
                pageSize: 5,
                courses: [{
                    value: 'AE',
                    label: 'Aerospace Engineering',
                    url: '/#/module',
                    img: '../../assets/ME.jpg'
                },
                {
                    value: 'AEE',
                    label: 'Architectural Environmental Engineering',
                    url: '/#/module'
                },
                {
                    value: 'Arch',
                    label: 'Architecture',
                    url: '/#/module'
                },
                {
                    value: 'Chem',
                    label: 'Chemistry',
                    url: '/#/module'
                },
                {
                    value: 'CE',
                    label: 'Civil Engineering',
                    url: '/#/module'
                },
                {
                    value: 'CS',
                    label: 'Computer Science',
                    url: '/#/module'
                },
                {
                    value: 'CSAI',
                    label: 'Computer Science with Articifcial Intelligence',
                    url: '/#/module'
                },
                {
                    value: 'EEE',
                    label: 'Electrical and Electronic Engineering',
                    url: '/#/module'
                },
                {
                    value: 'Ens',
                    label: 'Environmental Engineering',
                    url: '/#/module'
                },
                {
                    value: 'Math',
                    label: 'Mathematics with Applied Mathematics',
                    url: '/#/module'
                },
                {
                    value: 'ME',
                    label: 'Mechenical Engineering',
                    url: '/#/module'
                },
                {
                    value: 'PDM',
                    label: 'Product Design and Manufacture',
                    url: '/#/module'
                },
                {
                    value: 'Sta',
                    label: 'Statistics',
                    url: '/#/module'
                }]
            }
        },
        created() {
        this.handleUserList()
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
</style>
