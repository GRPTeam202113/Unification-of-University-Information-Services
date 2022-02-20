<template>
    <div class ="fob">
        <h1 class="title">Faculty of Business</h1>x
        <span class="introduction">The Faculty of Business (FoB) at UNNC is ...</span>
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
        <!-- <p>{{Msg}}</p> -->
    </div>
</template>

<script>
    export default {
        name: 'fob',
        data () {
            return {
                Msg: 'Welcome to FoB !',
                userList: [],
                currentPage: 1,
                pageSize: 5,
                courses: [{
                    value: 'FAM',
                    label: 'Finance, Accounting and Management'
                },
                {
                    value: 'IBE',
                    label: 'International Business Economics'
                },
                {
                    value: 'IBM',
                    label: 'INternational Business Management'
                },
                {
                    value: 'IBC',
                    label: 'International Business with Communication Studies'
                },
                {
                    value: 'IBL',
                    label: 'International Business with Language'
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
