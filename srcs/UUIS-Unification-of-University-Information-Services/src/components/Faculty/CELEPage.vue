<!--
 * @Descripttion: The Page for CELE, mainly include a filter for modules
 * and tables to demonstrate the modules filtered by user input
 * @Author: Yongjing Qi
 * @Date: 2022-03-01 23:36:00
 * @LastEditTime: 2022-03-15 10:51:12
-->

<template>
    <div class ="cele">
        <h1 class="title">Centre for English Language Education</h1>
        <el-divider></el-divider>
        <span class="introduction">The Centre for English Language Education (CELE) at UNNC is one of the largest and most well-established English language teaching departments in the world.</span><br><br><br>
        <span class="introduction">CELE runs a wide range of Preliminary Year, Pre-sessional and Academic literacy Development courses which form an integral part of the student experience at UNNC</span><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">Search</div>
                </span>
            </div>
            <div>
                <!-- ref="selector"  v-model="data"-->
                <el-cascader
                    v-model="value"
                    style = "width:60%; margin-left:15%;"
                    placeholder="Choose any faculty or course"
                    :options="options"
                    clearable
                    :props="{ expandTrigger: 'hover', checkStrictly: true, value: 'value', label: 'label'}"
                    popper-class="searchCascader"
                    @change="handleSelectorChange">
                </el-cascader>
                <span><el-button type="primary" plain icon="el-icon-search" @click="clickSearch"></el-button></span>
            </div>
        </div>
        <br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">{{Modules}}</div>
                </span>
            </div>
        </div>
        <br><br><br>
        <el-collapse v-model="activeSemester"  style="width:90%;margin-left:50px">
            <el-collapse-item name="s1">
                <template slot="title">
                    <div class = "foldPanel">Semester 1</div>
                </template>
                <el-table
                    :data="S1Module"
                    height="400"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="module"
                    label="module Title"
                    width="400">
                    <template slot-scope="scope">
                        <!-- <a :href="'http:'+'//www.baidu.com'" target="_blank" class="buttonText">{{scope.row.module}}</a> -->
                        <!-- <router-link v-bind:to="'/abc/' + scope.row.code">{{scope.row.module}}</router-link> -->
                        <router-link :to="{name:'module', params:{ModuleCode: scope.row.code}}">{{scope.row.module}}</router-link>
                        <!-- <span @click="toModulePage(scope.row.code)" >{{scope.row.module}}</span> -->
                    </template>
                    </el-table-column>
                    <el-table-column
                    prop="code"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="course"
                    label="Schoole/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
            <el-collapse-item name="s2">
                <template slot="title">
                    <div class = "foldPanel">Semester 2</div>
                </template>
                <el-table
                    :data="S2Module"
                    height="400"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="module"
                    label="Module Title"
                    width="400">
                    <template slot-scope="scope">
                        <!-- <a :href="'http:'+'//www.baidu.com'" target="_blank" class="buttonText">{{scope.row.module}}</a> -->
                        <!-- <router-link v-bind:to="'/abc/' + scope.row.code">{{scope.row.module}}</router-link> -->
                        <router-link :to="{name:'module', params:{ModuleCode: scope.row.code}}">{{scope.row.module}}</router-link>
                        <!-- <span @click="toModulePage(scope.row.code)" >{{scope.row.module}}</span> -->
                    </template>
                    </el-table-column>
                    <el-table-column
                    prop="code"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="course"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
            <el-collapse-item name="fullYear">
                <template slot="title">
                    <div class = "foldPanel">Full Year</div>
                </template>
                <el-table
                    :data="FullYearModule"
                    height="300"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="module"
                    label="Module Title"
                    width="400">
                    <template slot-scope="scope">
                        <!-- <a :href="'http:'+'//www.baidu.com'" target="_blank" class="buttonText">{{scope.row.module}}</a> -->
                        <!-- <router-link v-bind:to="'/abc/' + scope.row.code">{{scope.row.module}}</router-link> -->
                        <router-link :to="{name:'module', params:{ModuleCode: scope.row.code}}">{{scope.row.module}}</router-link>
                        <!-- <span @click="toModulePage(scope.row.code)" >{{scope.row.module}}</span> -->
                    </template>
                    </el-table-column>
                    <el-table-column
                    prop="code"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="course"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
        </el-collapse><br><br><br>
        <div class="block">
            <div style="position: relative;">
                <img class="square" src="../../assets/square.png" alt="">
                <span class="squareTitle" style="position: absolute; bottom: 20px; left: 50px;">
                    <div class="normalTitle">English Language Modules</div>
                </span>
            </div>
        </div>
        <br><br><br>
        <el-collapse v-model="activeSemesterEnglish" style="width:90%;margin-left:50px">
            <el-collapse-item name="s1">
                <template slot="title">
                    <div class = "foldPanel">Semester 1</div>
                </template>
                <el-table
                    :data="engS1Module"
                    height="300"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="module"
                    label="Module Title"
                    width="400">
                    <template slot-scope="scope">
                        <!-- <a :href="'http:'+'//www.baidu.com'" target="_blank" class="buttonText">{{scope.row.module}}</a> -->
                        <!-- <router-link v-bind:to="'/abc/' + scope.row.code">{{scope.row.module}}</router-link> -->
                        <router-link :to="{name:'module', params:{ModuleCode: scope.row.code}}">{{scope.row.module}}</router-link>
                        <!-- <span @click="toModulePage(scope.row.code)" >{{scope.row.module}}</span> -->
                    </template>
                    </el-table-column>
                    <el-table-column
                    prop="code"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="course"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
            <el-collapse-item name="s2">
                <template slot="title">
                    <div class = "foldPanel">Semester 2</div>
                </template>
                <el-table
                    :data="engS2Module"
                    height="300"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="module"
                    label="Module Title"
                    width="400">
                    <template slot-scope="scope">
                        <!-- <a :href="'http:'+'//www.baidu.com'" target="_blank" class="buttonText">{{scope.row.module}}</a> -->
                        <!-- <router-link v-bind:to="'/abc/' + scope.row.code">{{scope.row.module}}</router-link> -->
                        <router-link :to="{name:'module', params:{ModuleCode: scope.row.code}}">{{scope.row.module}}</router-link>
                        <!-- <span @click="toModulePage(scope.row.code)" >{{scope.row.module}}</span> -->
                    </template>
                    </el-table-column>
                    <el-table-column
                    prop="code"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="course"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
        </el-collapse><br><br><br>
    </div>
</template>

<script>
    import options from './CELEdb/filter'
    import {modulesS1, modulesS2, modulesFullYear, engModuleS1, engModuleS2} from './CELEdb/module'
    import {FOB_FAM, FOB_IB, FOB_IB_INTL, FHSS_IET, FHSS_ECO, FHSS_IC, FHSS_IS, FHSS_ES, FOSE_CS, FOSE_CS_INTL,
    FOSE_EG, FOSE_EG_INTL, FOSE_ARCH, FOSE_ENS, FOSE_CHEM, FOSE_MAM, FOSE_MAM_INTL, FOSE_STA, FOSE_AE} from './CELEdb/facultyCourseModule'
    import {FOB, FHSS, FOSE} from './CELEdb/facultyModule'
    // let selectedValue = this.$refs['selector'].inputValue
    let newModules = [{name: 'FOSE', item: FOSE}, {name: 'FOB', item: FOB}, {name: 'FHSS', item: FHSS}, {name: 'FOB_FAM', item: FOB_FAM},
    {name: 'FOB_IB', item: FOB_IB}, {name: 'FOB_IB_INTL', item: FOB_IB_INTL}, {name: 'FHSS_IET', item: FHSS_IET}, {name: 'FHSS_ECO', item: FHSS_ECO},
    {name: 'FHSS_IC', item: FHSS_IC}, {name: 'FHSS_IS', item: FHSS_IS}, {name: 'FHSS_ES', item: FHSS_ES}, {name: 'FOSE_CS_INTL', item: FOSE_CS_INTL},
    {name: 'FOSE_EG', item: FOSE_EG}, {name: 'FOSE_CS', item: FOSE_CS}, {name: 'FOSE_EG_INTL', item: FOSE_EG_INTL}, {name: 'FOSE_ARCH', item: FOSE_ARCH},
    {name: 'FOSE_ENS', item: FOSE_ENS}, {name: 'FOSE_CHEM', item: FOSE_CHEM}, {name: 'FOSE_MAM', item: FOSE_MAM}, {name: 'FOSE_MAM_INTL', item: FOSE_MAM_INTL},
    {name: 'FOSE_STA', item: FOSE_STA}, {name: 'FOSE_AE', item: FOSE_AE}]
    let selectedValue = null
    export default {
        name: 'cele',
        data () {
            return {
                Msg: 'Welcome to CELE !',
                Modules: 'Module List',
                activeSemester: [],
                activeSemesterEnglish: [],
                note: {
                    backgroundImage: 'url(' + require('../../assets/square.png') + ')',
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: '40px',
                    marginTop: '5px',
                    width: 100,
                    height: 200
                },
                value: null,
                options: options,
                S1Module: modulesS1,
                S2Module: modulesS2,
                FullYearModule: modulesFullYear,
                engS1Module: engModuleS1,
                engS2Module: engModuleS2
            }
        },
        methods: {
        handleSelectorChange(value) {
            if (value[1] == null & value[0] != null) { // user choosed just faculty as selector
                selectedValue = value[0]
            } else if (value[0] != null & value[1] != null) { // user choosed faculty & course as selector
                selectedValue = value[1]
                // console.log(value[1])
            } else { // user choosed nothing
                selectedValue = null
            }
            console.log(selectedValue)
        },
        clickSearch() {
            if (selectedValue === null) {
                this.S1Module = modulesS1
                this.S2Module = modulesS2
                this.FullYearModule = modulesFullYear
                this.Modules = 'Modules List'
            } else {
                var newModuleS1 = []
                var newModuleS2 = []
                var newModuleFullYear = []
                for (let i = 0; i < newModules.length; i++) {
                        if (newModules[i].name === selectedValue) {
                            console.log(newModules[i].name)
                            for (let j = 0; j < newModules[i].item.length; j++) {
                                if (newModules[i].item[j].semester === '1') {
                                    newModuleS1.push(newModules[i].item[j])
                                } else if (newModules[i].item[j].semester === '2') {
                                    newModuleS2.push(newModules[i].item[j])
                                } else {
                                    newModuleFullYear.push(newModules[i].item[j])
                                }
                            }
                            this.S1Module = newModuleS1
                            this.S2Module = newModuleS2
                            this.FullYearModule = newModuleFullYear
                            break;
                        }
                }
                this.Modules = 'Modules for ' + selectedValue
            }
        },
        toModulePage(e) {
            this.$router.push({name: 'module', params: {ModuleCode: e}});
            console.log(e)
        }
    }
}
</script>
<style rel="stylesheet/scss" lang="scss" scoped>
.title {
    margin-left: 20px;
    margin-top: 0px;
    font-size: 50px;
}
.introduction {
    margin-left: 600px;
    margin-right: 100px;
    float: right;
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
.normalTitle {
    color:rgb(0, 0, 0);
    font-size:25px;
    font-weight: bolder;
}
.square{
    margin-left: 20px;
    width: 90px;
    height: 90px;
}
.foldPanel {
    margin-right: -30px;
    background-color: #116996;
    color:white;
    font-size:25px;
    margin-left:0px;
    padding-left:5px;
    font-weight: bolder;
    width:100%;
}

.searchCascader {
    background-color: #F7F7F8;
}
.el-input__inner{
      border:1px solid #F7F7F8;
      background-color: #F7F7F8;
    }
</style>
