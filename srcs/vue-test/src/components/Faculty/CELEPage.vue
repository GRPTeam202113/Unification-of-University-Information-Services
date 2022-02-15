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
                    <div class="squareTitle">Search</div>
                    <div>
                        <el-cascader
                            style = "width:50%; margin-left:300px;"
                            v-model="value"
                            placeholder="Choose any faculty or course"
                            :options="options"
                            :props="{ expandTrigger: 'hover', checkStrictly: true}"
                            popper-class="searchCascader"
                            @change="handleChange">
                        </el-cascader>
                        <el-divider direction="vertical"></el-divider>
                        <span><el-button type="primary" icon="el-icon-search"></el-button></span>
                    </div>
                </span>
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
        <el-collapse v-model="activeSemester" @change="handleChange" style="width:90%;margin-left:50px">
            <el-collapse-item name="s1">
                <template slot="title">
                    <div class = "foldPanel">Semester 1</div>
                </template>
                <el-table
                    :data="S1Module"
                    height="500"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="Moduletitle"
                    label="Module Title"
                    width="400">
                    </el-table-column>
                    <el-table-column
                    prop="Modulecode"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="school"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
            <el-collapse-item name="s2">
                <template slot="title">
                    <div class = "foldPanel">Semester 2</div>
                </template>
                <el-table
                    :data="S1Module"
                    height="500"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="Moduletitle"
                    label="Module Title"
                    width="400">
                    </el-table-column>
                    <el-table-column
                    prop="Modulecode"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="school"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
            <el-collapse-item name="fullYear">
                <template slot="title">
                    <div class = "foldPanel">Full Year</div>
                </template>
                <el-table
                    :data="S1Module"
                    height="500"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="Moduletitle"
                    label="Module Title"
                    width="400">
                    </el-table-column>
                    <el-table-column
                    prop="Modulecode"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="school"
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
        <el-collapse v-model="activeSemesterEnglish" @change="handleChange" style="width:90%;margin-left:50px">
            <el-collapse-item name="s1">
                <template slot="title">
                    <div class = "foldPanel">Semester 1</div>
                </template>
                <el-table
                    :data="S1Module"
                    height="500"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="Moduletitle"
                    label="Module Title"
                    width="400">
                    </el-table-column>
                    <el-table-column
                    prop="Modulecode"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="school"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
            <el-collapse-item name="s2">
                <template slot="title">
                    <div class = "foldPanel">Semester 2</div>
                </template>
                <el-table
                    :data="S1Module"
                    height="500"
                    border
                    style="width: 100%">
                    <el-table-column
                    prop="Moduletitle"
                    label="Module Title"
                    width="400">
                    </el-table-column>
                    <el-table-column
                    prop="Modulecode"
                    label="Module Code"
                    width="280">
                    </el-table-column>
                    <el-table-column
                    prop="credit"
                    label="Credites"
                    width="150">
                    </el-table-column>
                    <el-table-column
                    prop="school"
                    label="School/Degree">
                    </el-table-column>
                </el-table>
            </el-collapse-item><br><br>
        </el-collapse><br><br><br>
        <p>{{Msg}}</p>
    </div>
</template>

<script>
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
                options: [{
                    value: 'fob',
                    label: 'Faculty of Business',
                    children: [{
                        value: 'FAM',
                        label: 'Finance Accounting and Management'
                    }, {
                        value: 'IB',
                        label: 'International Business'
                    }]
                    }, {
                    value: 'fhss',
                    label: 'Faculty of Humanities and Social Sciences',
                    children: [{
                        value: 'IET',
                        label: 'International Economics and Trade'
                    }, {
                        value: 'Eco',
                        label: 'Economics'
                    }, {
                        value: 'IC',
                        label: 'International Communications'
                    }, {
                        value: 'IS',
                        label: 'International Studies'
                    }, {
                        value: 'ES',
                        label: 'Education and English'
                    }]
                    }, {
                    value: 'fose',
                    label: 'Faculty of Science and Engineering',
                    children: [{
                        value: 'CS',
                        label: 'Computer Science'
                    }, {
                        value: 'EG',
                        label: 'Engineering'
                    }, {
                        value: 'Arch',
                        label: 'Architecture'
                    }, {
                        value: 'Ens',
                        label: 'Environmental Sciences'
                    }, {
                        value: 'Chem',
                        label: 'Chemistry'
                    }, {
                        value: 'MAM',
                        label: 'Mathematics with Applied Mathematics'
                    }, {
                        value: 'Sta',
                        label: 'Statistics'
                    }, {
                        value: 'AE',
                        label: 'Aerospace Engineering'
                    }]
                }],
                S1Module: [{
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }, {
                    Moduletitle: 'Oral Communication Skills A',
                    Modulecode: 'CELEN069',
                    credit: '10',
                    school: 'IB, ECO, IC, IS, ELAL, ELL, EG, CS, MAM, Ens, EIB, Arch'
                    }]

            }
        },
        methods: {
      handleChange(val) {
        console.log(val)
      }
    }
    }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.title {
    margin-left: 20px;
    margin-top: 0px;
    font-size: 70px;
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
</style>
<style>
.searchCascader {
    background-color: #F7F7F8;
}
.el-input__inner{
      border:1px solid #F7F7F8;
      background-color: #F7F7F8;
    }
</style>
