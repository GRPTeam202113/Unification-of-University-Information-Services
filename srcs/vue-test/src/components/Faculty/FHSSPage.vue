<template>
    <div class ="fhss">
        <h1 class="title">Faculty of Humanities and Social Sciences</h1>x
        <span class="introduction">The Faculty of Humanities and Social Sciences (FHSS) at UNNC is ...</span>
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
        name: 'fhss',
        data () {
            return {
                Msg: 'Welcome to FHSS !',
                userList: [],
                currentPage: 1,
                pageSize: 5,
                courses: [{
                    value: 'Eco',
                    label: 'Economics'
                },
                {
                    value: 'EGA',
                    label: 'English Language and Applied Linguistics'
                },
                {
                    value: 'EGL',
                    label: 'English Language and Literature'
                },
                {
                    value: 'IC',
                    label: 'International Communication Studies'
                },
                {
                    value: 'ICL',
                    label: 'International Communication Studies with Chinese'
                },
                {
                    value: 'IET',
                    label: 'International Economics and Trade'
                },
                {
                    value: 'IS',
                    label: 'International Studies'
                },
                {
                    value: 'ISL',
                    label: 'International Studies with Spanish/German/French/Japanese/Chinese'
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
