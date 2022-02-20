<template>
    <div class ="fose">
        <h1 class="title">Faculty of Science and Engineering</h1>
        <span class="introduction">The Faculty of Science and Engineering (FoSE) at UNNC is ...</span>
        <div class = "courses">
        <el-table
            :row-style="{height:'80px'}"
            :data="courses.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%; font-size: 18px; font-weight:bolder">
            <el-table-column
                prop="label"
                width="1400"
                align="center">
            </el-table-column>
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
                    label: 'Aerospace Engineering'
                },
                {
                    value: 'AEE',
                    label: 'Architectural Environmental Engineering'
                },
                {
                    value: 'Arch',
                    label: 'Architecture'
                },
                {
                    value: 'Chem',
                    label: 'Chemistry'
                },
                {
                    value: 'CE',
                    label: 'Civil Engineering'
                },
                {
                    value: 'CS',
                    label: 'Computer Science'
                },
                {
                    value: 'CSAI',
                    label: 'Computer Science with Articifcial Intelligence'
                },
                {
                    value: 'EEE',
                    label: 'Electrical and Electronic Engineering'
                },
                {
                    value: 'Ens',
                    label: 'Environmental Engineering'
                },
                {
                    value: 'Math',
                    label: 'Mathematics with Applied Mathematics'
                },
                {
                    value: 'ME',
                    label: 'Mechenical Engineering'
                },
                {
                    value: 'PDM',
                    label: 'Product Design and Manufacture'
                },
                {
                    value: 'Sta',
                    label: 'Statistics'
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
