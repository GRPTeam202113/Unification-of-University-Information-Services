<template>
    <div class ="fhss">
        <h1 class="title">Faculty of Humanities and Social Sciences</h1>
        <span class="introduction">The Faculty of Humanities and Social Sciences (FHSS) at UNNC is ...</span>
        <div class = "courses">
        <el-table
            :row-style="{height:'80px'}"
            :data="courses.slice((currentPage-1)*pageSize,currentPage*pageSize)"
            style="width: 100%; font-size: 18px; font-weight:bolder">
            <el-table-column
                width="300"
                align="center">
                <template slot-scope="scope">
                <img :src="scope.row.img" alt="" width="300" height="300">
                </template>
            </el-table-column>
            <el-table-column
                width="1400"
                align="center">
                <template slot-scope="scope">
                <a :href="scope.row.url" target="_blank" class="buttonText">{{scope.row.label}}</a>
                </template>
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
                    label: 'Economics',
                    url: '/#/module'
                },
                {
                    value: 'EGA',
                    label: 'English Language and Applied Linguistics',
                    url: '/#/module'
                },
                {
                    value: 'EGL',
                    label: 'English Language and Literature',
                    url: '/#/module'
                },
                {
                    value: 'IC',
                    label: 'International Communication Studies',
                    url: '/#/module'
                },
                {
                    value: 'ICL',
                    label: 'International Communication Studies with Chinese',
                    url: '/#/module'
                },
                {
                    value: 'IET',
                    label: 'International Economics and Trade',
                    url: '/#/module'
                },
                {
                    value: 'IS',
                    label: 'International Studies',
                    url: '/#/module'
                },
                {
                    value: 'ISL',
                    label: 'International Studies with Spanish/German/French/Japanese/Chinese',
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
